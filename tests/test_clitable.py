import clitable
from unittest import TestCase


class ClitableTest(TestCase):
    def test_len_title(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        test_dict['int'] = 123456789
        test_dict['array'] = ['test', 'hoge']
        test_dict['dict'] = {'test': 'hoge'}

        result = clitable.len_title(test_dict)
        self.assertEqual(3, result['bar'])
        self.assertEqual(4, result['hoge'])
        self.assertEqual(9, result['int'])
        self.assertEqual(16, result['array'])
        self.assertEqual(16, result['dict'])

    def test_to_line(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        len_title = clitable.len_title(test_dict)
        result = clitable.to_line(len_title)

        self.assertEqual('+----------+-----+------+', result)

    def test_to_header(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        len_title = clitable.len_title(test_dict)
        result = clitable.to_header(len_title)

        self.assertEqual('| foo      | bar | hoge |', result)

    def test_to_body(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        len_title = clitable.len_title(test_dict)
        result = clitable.to_body(len_title, test_dict)

        self.assertEqual('| fighters | on  | piyo |', result)

    def test_diff_header_and_line(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        len_title = clitable.len_title(test_dict)
        line = clitable.to_line(len_title)
        header = clitable.to_header(len_title)

        self.assertEqual(len(line), len(header))

    def test_diff_header_and_body(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        len_title = clitable.len_title(test_dict)
        header = clitable.to_header(len_title)
        body = clitable.to_body(len_title, test_dict)

        self.assertEqual(len(header), len(body))

    def test_to_table(self):
        test_dict = {}
        test_dict['foo'] = 'fighters'
        test_dict['bar'] = 'on'
        test_dict['hoge'] = 'piyo'
        result = clitable.to_table(test_dict)

        expected = '+----------+-----+------+\n'
        expected += '| foo      | bar | hoge |\n'
        expected += '+----------+-----+------+\n'
        expected += '| fighters | on  | piyo |\n'
        expected += '+----------+-----+------+\n'
        self.assertEqual(expected, result)


        test_list = []
        test_list.append(['foo', 'fighters'])
        test_list.append(['bar', 'on'])
        test_list.append(['hoge', 'piyo'])
        result = clitable.to_table(test_list)

        self.assertEqual(expected, result)
