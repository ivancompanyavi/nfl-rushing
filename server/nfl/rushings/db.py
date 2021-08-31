import json
import os
from typing import Type, Tuple

from .entities import Paginator, PlayerRushing, Sorter, Db, Filter


class JsonDb(Db):
    """JSON implementation of Db"""

    def _build_player_rushing(self, raw_data: object) -> PlayerRushing:
        return PlayerRushing(
            raw_data.get('Player', None),
            raw_data.get('Team', None),
            raw_data.get('Pos', None),
            raw_data.get('Att/G', None),
            raw_data.get('Att', None),
            raw_data.get('Yds', None),
            raw_data.get('Avg', None),
            raw_data.get('Yds/G', None),
            raw_data.get('TD', None),
            raw_data.get('Lng', None),
            raw_data.get('1st', None),
            raw_data.get('1st%', None),
            raw_data.get('20+', None),
            raw_data.get('40+', None),
            raw_data.get('FUM', None)
        )

    def _sort_data(self, players: list[PlayerRushing]) -> list[PlayerRushing]:
        if len(self.sorters) == 0:
            return players

        def sort_func(field):
            def wrapper(x):
                value = str(getattr(x, field))
                try:
                    # I prioritize the values of Lng if ended up in touchdown
                    if 'T' in value:
                        return float(value[:-1]) + 0.1
                    return float(value)
                except ValueError:  # The value is a string
                    return value

            return wrapper
        for sorter in self.sorters:
            players = sorted(players, key=sort_func(sorter.field),
                             reverse=not sorter.ascending)
        return players

    def _paginate_data(self, players: list[PlayerRushing]) -> list[PlayerRushing]:
        if not self.paginator or (self.paginator.page == 0 and self.paginator.offset == 0):
            return players

        page, offset = self.paginator.page, self.paginator.offset
        return players[page * offset:page * offset + offset]

    def _filter_data(self, players: list[PlayerRushing]) -> list[PlayerRushing]:
        if not self.filter:
            return players

        def filter_fn(p): return self.filter.field.lower() in p.name.lower()
        return list(filter(filter_fn, players))

    def query(self) -> Tuple[list[PlayerRushing], int]:
        file_path = os.path.join(os.path.dirname(
            __file__), '..', '..', 'data', 'rushings.json')
        total_results = 0
        with open(file_path) as f:
            data = json.load(f)
            result = [self._build_player_rushing(p) for p in data]
            result = self._filter_data(result)
            total_results = len(result)
            result = self._sort_data(result)
            result = self._paginate_data(result)

            return (result, total_results)


def get_db(filter: Filter, paginator: Paginator, sorters: list[Sorter]) -> Type[Db]:
    return JsonDb(filter, paginator, sorters)
