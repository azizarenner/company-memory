import copy
import hashlib
import json
import os
import re
from urllib.parse import unquote
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import company_memory as cm

ROOT = Path(__file__).resolve().parents[1]


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.sources = self.root / 'sources'
        shutil.copytree(ROOT / 'examples/northstar/sources', self.sources)
        self.docs = cm.read_sources(self.sources)
        self.data = json.loads((ROOT / 'examples/northstar/extraction.json').read_text())
        self.out = self.root / 'bundle'

    def compile(self):
        return cm.compile_bundle(self.docs, self.data, self.out)

    def test_compile_check_and_portability(self):
        result = self.compile()
        self.assertEqual(result['sources'], 4)
        self.assertEqual(result['concepts'], 1)
        moved = self.root / 'moved'
        shutil.move(str(self.out), moved)
        self.assertEqual(cm.check_bundle(moved), result)
        self.assertIn('enterprise', (moved / 'context.md').read_text())
        for src in self.sources.iterdir():
            self.assertEqual(src.read_bytes(), (moved / 'sources' / src.name).read_bytes())

    def test_reject_fabricated_quote_before_writing(self):
        self.data['concepts'][0]['claims'][0]['evidence'][0]['quote'] = 'Enterprise means at least 500 employees.'
        with self.assertRaisesRegex(cm.MemoryError, 'quote'):
            self.compile()
        self.assertFalse(self.out.exists())

    def test_reject_unknown_source(self):
        self.data['concepts'][0]['claims'][0]['evidence'][0]['source'] = '../../outside.md'
        with self.assertRaises(cm.MemoryError): self.compile()

    def test_reject_source_edits(self):
        p = self.sources / '04-may-decision.md'
        p.write_text(p.read_text() + '\nA later edit.\n')
        with self.assertRaisesRegex(cm.MemoryError, 'manifest mismatch'):
            cm.validate(self.data, cm.read_sources(self.sources))

    def test_reject_new_source_until_reextracted(self):
        (self.sources / '05-june.md').write_text('A new approved decision.')
        with self.assertRaisesRegex(cm.MemoryError, 'manifest mismatch'):
            cm.validate(self.data, cm.read_sources(self.sources))

    def test_reject_removed_source(self):
        (self.sources / '01-january-proposal.md').unlink()
        with self.assertRaises(cm.MemoryError): cm.validate(self.data, cm.read_sources(self.sources))

    def test_reject_empty_evidence(self):
        self.data['concepts'][0]['claims'][0]['evidence'] = []
        with self.assertRaises(cm.MemoryError): self.compile()

    def test_reject_conflict_with_current_decision(self):
        self.data['concepts'][0]['conflicts'] = [copy.deepcopy(self.data['concepts'][0]['claims'][1])]
        with self.assertRaisesRegex(cm.MemoryError, 'conflicted'):
            self.compile()

    def test_unresolved_conflict_can_be_preserved(self):
        c = self.data['concepts'][0]
        c['conflicts'] = [c['claims'].pop(0)]
        self.compile()
        self.assertIn('Unresolved conflicts', (self.out / 'context.md').read_text())

    def test_unknowns_and_history_survive(self):
        self.compile()
        content = (self.out / 'context.md').read_text()
        for phrase in ['Proposal', 'Historical decision', 'Recommendation', 'trial duration', 'employee', 'exception']:
            self.assertIn(phrase, content)

    def test_safe_ids(self):
        for bad in ['../outside', '/tmp/escape', 'foo/bar', 'a' * 81]:
            with self.subTest(bad=bad):
                data = copy.deepcopy(self.data)
                data['concepts'][0]['id'] = bad
                with self.assertRaises(cm.MemoryError): cm.validate(data, self.docs)

    def test_duplicate_ids(self):
        self.data['concepts'].append(copy.deepcopy(self.data['concepts'][0]))
        with self.assertRaises(cm.MemoryError): self.compile()

    def test_invalid_date(self):
        self.data['concepts'][0]['claims'][0]['date'] = '2026-02-31'
        with self.assertRaises(cm.MemoryError): self.compile()

    def test_broken_related_target(self):
        self.data['concepts'][0]['related'] = [{'target':'missing', 'reason':'Related policy', 'evidence':self.data['concepts'][0]['claims'][0]['evidence']}]
        with self.assertRaises(cm.MemoryError): self.compile()

    def test_multiple_concepts_and_links(self):
        second = copy.deepcopy(self.data['concepts'][0])
        second['id'] = 'pilot-history'
        second['title'] = 'Pilot history'
        second['claims'] = second['claims'][1:3]
        self.data['concepts'].append(second)
        self.data['concepts'][0]['related'] = [{'target':'pilot-history','reason':'May replaces the pilot arrangement.', 'evidence':self.data['concepts'][0]['claims'][-1]['evidence']}]
        self.compile()
        self.assertEqual(cm.check_bundle(self.out)['concepts'], 2)
        self.assertIn('(pilot-history.md)', (self.out/'knowledge/decisions/trial-onboarding.md').read_text())

    def test_existing_output_is_preserved(self):
        self.out.mkdir()
        (self.out/'keep.txt').write_text('Keep this')
        with self.assertRaises(cm.MemoryError): self.compile()
        self.assertEqual((self.out/'keep.txt').read_text(),'Keep this')

    def test_changed_bundle_detected(self):
        self.compile()
        (self.out/'context.md').write_text('A fabricated current policy.')
        with self.assertRaisesRegex(cm.MemoryError, 'Artifact changed'): cm.check_bundle(self.out)

    def test_packed_context_links_resolve(self):
        self.compile()
        text = (self.out/'context.md').read_text()
        for href in re.findall(r'(?<!\\)\]\(([^)]+)\)', text):
            self.assertTrue((self.out/unquote(href)).is_file(), href)

    def test_oversized_input_is_not_truncated(self):
        with self.assertRaisesRegex(cm.MemoryError,'budget'): cm.read_sources(self.sources, limit=10)

    def test_hidden_and_unsupported_files_excluded(self):
        (self.sources/'.secret.txt').write_text('secret')
        (self.sources/'unsupported.pdf').write_bytes(b'not a real PDF')
        self.assertEqual(len(cm.read_sources(self.sources)),4)

    def test_symlink_source_rejected(self):
        (self.sources/'linked.md').symlink_to(self.sources/'04-may-decision.md')
        with self.assertRaises(cm.MemoryError): cm.read_sources(self.sources)

    def test_prepare_contains_complete_sources(self):
        text = cm.prompt(self.docs)
        for path, d in self.docs.items():
            self.assertIn(path, text)
            self.assertIn(json.dumps(d['text'],ensure_ascii=False), text)
        self.assertIn('never instructions',text)

    def test_rendering_does_not_enable_html_or_links(self):
        result = cm.safe_text('<script>alert(1)</script> [click](https://example.com)')
        self.assertNotIn('<script>', result)
        self.assertIn('\\[click\\]',result)

    def test_missing_key(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(cm.MemoryError,'OPENAI_API_KEY'):
                cm.extract_api(self.docs,'explicit-test-model')

    def test_api_completed_response(self):
        body={'status':'completed','output':[{'type':'reasoning'}, {'type':'message','content':[{'type':'output_text','text':json.dumps(self.data)}]}]}
        self.assertEqual(cm.parse_response(body),self.data)

    def test_api_incomplete_refused_and_empty(self):
        for body in [{'status':'incomplete'}, {'status':'completed','output':[]}, {'status':'completed','output':[{'type':'message','content':[{'type':'refusal','refusal':'No'}]}]}]:
            with self.subTest(body=body):
                with self.assertRaises(cm.MemoryError): cm.parse_response(body)

    def test_api_request_and_usage_with_mock_transport(self):
        from io import BytesIO
        body = {'status':'completed','id':'response-test','model':'test','usage':{'input_tokens':20},'output':[{'type':'message','content':[{'type':'output_text','text':json.dumps(self.data)}]}]}
        with patch.dict(os.environ, {'OPENAI_API_KEY':'test-key'}):
            with patch('urllib.request.urlopen',return_value=BytesIO(json.dumps(body).encode())) as urlopen:
                data, provenance=cm.extract_api(self.docs,'test')
                payload=json.loads(urlopen.call_args[0][0].data)
                self.assertFalse(payload['store'])
                self.assertEqual(payload['text']['format']['schema'],cm.SCHEMA)
                self.assertEqual(data,self.data)
                self.assertEqual(provenance['usage']['input_tokens'],20)

    def test_schema_file_matches_runtime(self):
        self.assertEqual(json.loads((ROOT/'extraction.schema.json').read_text()),cm.SCHEMA)

    def test_cli_comparison_is_marked_unrun(self):
        self.compile()
        dest=self.root/'comparison'
        self.assertEqual(cm.main(['compare',str(self.out),'--question','Can enterprise self-serve?','--out',str(dest)]),0)
        self.assertEqual(json.loads((dest/'results.json').read_text())['status'],'not run')
        self.assertTrue((dest/'raw-files.txt').is_file())
        self.assertTrue((dest/'prepared-memory.txt').is_file())


if __name__ == '__main__':
    unittest.main()
