from unittest import TestCase

import clitable


class ClitableTest(TestCase):
    def test_len_title(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]

        result = clitable._len_title(test_list)
        self.assertEqual(2, result['id'])
        self.assertEqual(10, result['time'])
        self.assertEqual(4, result['name'])
        self.assertEqual(9, result['do'])

    def test_to_line(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]
        len_title = clitable._len_title(test_list)
        result = clitable._to_line(len_title)

        self.assertEqual('+----+------------+------+-----------+', result)

    def test_to_header(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]
        len_title = clitable._len_title(test_list)
        result = clitable._to_header(len_title)

        self.assertEqual('| id | time       | name | do        |', result)

    def test_to_body(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]
        len_title = clitable._len_title(test_list)
        result = clitable._to_body(len_title, test_list)

        expected = [
            '| 1  | 1586995200 | kota | breakfast |',
            '| 2  | 1587006000 | kota | lunch     |',
            '| 3  | 1587016800 | kota | teatime   |',
            '| 4  | 1587031200 | kota | dinner    |',
        ]
        self.assertEqual(expected, result)

    def test_to_table_default(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]
        result = clitable._to_table(test_list)

        expected = ''
        expected += '+----+------------+------+-----------+\n'
        expected += '| id | time       | name | do        |\n'
        expected += '+----+------------+------+-----------+\n'
        expected += '| 1  | 1586995200 | kota | breakfast |\n'
        expected += '| 2  | 1587006000 | kota | lunch     |\n'
        expected += '| 3  | 1587016800 | kota | teatime   |\n'
        expected += '| 4  | 1587031200 | kota | dinner    |\n'
        expected += '+----+------------+------+-----------+\n'
        self.assertEqual(expected, result)

    def test_to_table_zero_margin(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]

        result = clitable._to_table(test_list, margin=0)

        expected = ''
        expected += '+--+----------+----+---------+\n'
        expected += '|id|time      |name|do       |\n'
        expected += '+--+----------+----+---------+\n'
        expected += '|1 |1586995200|kota|breakfast|\n'
        expected += '|2 |1587006000|kota|lunch    |\n'
        expected += '|3 |1587016800|kota|teatime  |\n'
        expected += '|4 |1587031200|kota|dinner   |\n'
        expected += '+--+----------+----+---------+\n'
        self.assertEqual(expected, result)

    def test_to_table_wide_margin(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]

        result = clitable._to_table(test_list, margin=2)

        expected = ''
        expected += '+------+--------------+--------+-------------+\n'
        expected += '|  id  |  time        |  name  |  do         |\n'
        expected += '+------+--------------+--------+-------------+\n'
        expected += '|  1   |  1586995200  |  kota  |  breakfast  |\n'
        expected += '|  2   |  1587006000  |  kota  |  lunch      |\n'
        expected += '|  3   |  1587016800  |  kota  |  teatime    |\n'
        expected += '|  4   |  1587031200  |  kota  |  dinner     |\n'
        expected += '+------+--------------+--------+-------------+\n'
        self.assertEqual(expected, result)

    def test_print_table(self):
        test_list = [
            {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
            {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
            {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
            {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
        ]

        #clitable.print_table(test_list)
        self.assertTrue(True)
