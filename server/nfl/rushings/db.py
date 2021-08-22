import json
import os
from typing import Type

from .entities import Paginator, PlayerRushing, Sorter, Db, Filter


class JsonDb(Db):
    """JSON implementation of Db"""

    def _build_player_rushing(self, raw_data: object) -> PlayerRushing:
        return PlayerRushing(
            raw_data['Player'],
            raw_data['Team'],
            raw_data['Pos'],
            raw_data['Att/G'],
            raw_data['Att'],
            raw_data['Yds'],
            raw_data['Avg'],
            raw_data['Yds/G'],
            raw_data['TD'],
            raw_data['Lng'],
            raw_data['1st'],
            raw_data['1st%'],
            raw_data['20+'],
            raw_data['40+'],
            raw_data['FUM']
        )

    def _sort_data(self, players: list[PlayerRushing]) -> list[PlayerRushing]:
        if len(self.sorters) == 0:
            return players

        def sort_func(field):
            def wrapper(x):
                value = str(getattr(x, field))
                if 'T' in value:
                    return float(value[:-1]) + 0.1
                return float(value)

            return wrapper
        for sorter in self.sorters:
            players = sorted(players, key=sort_func(sorter.field),
                             reverse=not sorter.ascending)
        return players

    def _paginate_data(self, players: list[PlayerRushing]) -> list[PlayerRushing]:
        if self.paginator.page == 0 and self.paginator.offset == 0:
            return players

        page, offset = self.paginator.page, self.paginator.offset
        return players[page * offset:page * offset + offset]

    def query(self) -> list[PlayerRushing]:
        file_path = os.path.join(os.path.dirname(
            __file__), '..', '..', 'data', 'rushings.json')
        with open(file_path) as f:
            data = json.load(f)
            result = []
            for player in data:
                if not self.filter.field or self.filter.field in player['Player']:
                    result.append(self._build_player_rushing(player))
            result = self._sort_data(result)
            result = self._paginate_data(result)

            return result


def get_db(filter: Filter, paginator: Paginator, sorters: list[Sorter]) -> Type[Db]:
    return JsonDb(filter, paginator, sorters)
