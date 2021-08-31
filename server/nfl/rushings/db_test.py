import json
import unittest
from unittest.mock import DEFAULT, MagicMock, patch, mock_open
from .entities import Paginator, PlayerRushing, Sorter
from .db import JsonDb


class TestSorting(unittest.TestCase):
    def test_sort_data_no_sorter(self):
        sorters = []
        players = [PlayerRushing()]
        db = JsonDb(None, None, sorters)
        result = db._sort_data(players)
        self.assertEqual(players, result)

    def test_sort_data_ints(self):
        sorters = [Sorter('attempts', False)]
        players = [
            PlayerRushing(attempts=0),
            PlayerRushing(attempts=4),
        ]
        db = JsonDb(None, None, sorters)
        result = db._sort_data(players)
        self.assertEqual(result[0].attempts, 4)
        self.assertEqual(result[1].attempts, 0)

    def test_sort_data_strings(self):
        sorters = [Sorter('name', True)]
        players = [
            PlayerRushing(name='Foo'),
            PlayerRushing(name='Bar'),
        ]
        db = JsonDb(None, None, sorters)
        result = db._sort_data(players)
        self.assertEqual(result[0].name, 'Bar')
        self.assertEqual(result[1].name, 'Foo')

    def test_sort_data_touchdowns(self):
        sorters = [Sorter('longest_rush', True)]
        players = [
            PlayerRushing(longest_rush='20'),
            PlayerRushing(longest_rush='20T'),
            PlayerRushing(longest_rush='15'),
        ]
        db = JsonDb(None, None, sorters)
        result = db._sort_data(players)
        self.assertEqual(result[0].longest_rush, '15')
        self.assertEqual(result[1].longest_rush, '20')
        self.assertEqual(result[2].longest_rush, '20T')


class TestPagination(unittest.TestCase):
    def test_paginate_no_paginator(self):
        paginator = None
        players = [
            PlayerRushing(name='Foo'),
            PlayerRushing(name='Bar'),
        ]
        db = JsonDb(None, paginator, None)
        result = db._paginate_data(players)
        self.assertEqual(result, players)

    def test_paginate_empty_paginator(self):
        paginator = Paginator(0, 0)
        players = [
            PlayerRushing(name='Foo'),
            PlayerRushing(name='Bar'),
        ]
        db = JsonDb(None, paginator, None)
        result = db._paginate_data(players)
        self.assertEqual(result, players)

    def test_paginate_first_page(self):
        paginator = Paginator(0, 2)
        players = [
            PlayerRushing(name='Foo'),
            PlayerRushing(name='Bar'),
            PlayerRushing(name='Spam'),
            PlayerRushing(name='Eggs'),
        ]
        db = JsonDb(None, paginator, None)
        result = db._paginate_data(players)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, 'Foo')
        self.assertEqual(result[1].name, 'Bar')

    def test_paginate_second_page(self):
        paginator = Paginator(1, 2)
        players = [
            PlayerRushing(name='Foo'),
            PlayerRushing(name='Bar'),
            PlayerRushing(name='Spam'),
            PlayerRushing(name='Eggs'),
        ]
        db = JsonDb(None, paginator, None)
        result = db._paginate_data(players)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, 'Spam')
        self.assertEqual(result[1].name, 'Eggs')


def same_data_return(x): return x


class TestQuery(unittest.TestCase):
    @patch.multiple(
        JsonDb,
        _filter_data=MagicMock(side_effect=same_data_return),
        _paginate_data=MagicMock(side_effect=same_data_return),
        _sort_data=MagicMock(side_effect=same_data_return))
    def test_query(self):
        file_data = json.dumps(
            [
                {'Player': 'Foo'},
                {'Player': 'Bar'},
            ]
        )
        with patch('builtins.open', mock_open(read_data=file_data)) as f:
            db = JsonDb(None, None, None)
            result, total = db.query()
            self.assertEqual(total, 2)
            self.assertEqual(result[0].name, 'Foo')
            self.assertEqual(result[1].name, 'Bar')
