# -*- coding: utf-8 -*-

import unittest
import logging

from pyutil_json import util


class TestUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_json_dumps_e(self):
        a = ['a', 'b', 'c']
        err, a_str = util.json_dumps_e(a)
        self.assertIsNone(err)
        self.assertEqual('["a","b","c"]', a_str)

        b = {'c': 'd', 'a': 'b'}
        err, b_str = util.json_dumps_e(b, sort_keys=True)
        self.assertIsNone(err)
        self.assertEqual('{"a":"b","c":"d"}', b_str)

        c = [{'a': 'b', 'c': 'd'}]
        err, c_str = util.json_dumps_e(c, sort_keys=True)
        self.assertIsNone(err)
        self.assertEqual('[{"a":"b","c":"d"}]', c_str)

        c = [{'a': 'b', 'c': 'd'}]
        err, c_str = util.json_dumps_e(c, indent=2, sort_keys=True)
        self.assertIsNone(err)
        expect_str =\
            '''[
  {
    "a": "b",
    "c": "d"
  }
]'''
        self.assertEqual(expect_str, c_str)

    def test_json_loads_e(self):
        a_str = '["a","b","c"]'
        err, a = util.json_loads_e(a_str)
        self.assertIsNone(err)
        self.assertEqual(['a', 'b', 'c'], a)

        b_str = '["a",,"b","c"]'
        err, b = util.json_loads_e(b_str)
        self.assertIsNotNone(err)
