import unittest
from unittest.mock import patch

from nfl.rushings.entities import Paginator, Sorter
from nfl.rushings import routes


class TestBuildSorters(unittest.TestCase):
    def test_no_data(self):
        self.assertEqual(routes.build_sorters(None), [])

    def test_right_amount(self):
        sorters = routes.build_sorters('foo,-bar')
        self.assertEqual(len(sorters), 2)

    def test_right_sortings(self):
        sorters = routes.build_sorters('foo,-bar')
        self.assertEqual(sorters[0], Sorter('foo', True))
        self.assertEqual(sorters[1], Sorter('bar', False))


class TestBuildPaginator(unittest.TestCase):
    def test_no_data(self):
        self.assertEqual(routes.build_paginator(None, None), Paginator(0, 0))

    def test_format_data(self):
        self.assertEqual(routes.build_paginator('1', '10'), Paginator(1, 10))

    @patch('nfl.rushings.routes.abort')
    def test_abort_when_wrong_data(self, abort_mock):
        routes.build_paginator('foo', 'bar')
        assert abort_mock.called
