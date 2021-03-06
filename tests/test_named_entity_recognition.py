"""Test Named Entity Recognition module"""

import unittest

from pororo import Pororo


class PororoNERTester(unittest.TestCase):

    def test_modules(self):
        ner = Pororo(task="ner", lang="ko")
        ner_res = ner("[UCL 리뷰] '디마리아 1골 2도움' PSG, 라이프치히 3-0 제압...사상 첫 결승행")
        self.assertIsInstance(ner_res, list)


if __name__ == "__main__":
    unittest.main()
