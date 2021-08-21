import json
import os
from typing import Type

from .entities import Paginator, PlayerRushing, Sorter, Db, Filter


class JsonDb(Db):
    """JSON implementation of Db"""

    def query(self) -> list[PlayerRushing]:
        file_path = os.path.join(os.path.dirname(
            __file__), '..', '..', 'data', 'rushings.json')
        with open(file_path) as f:
            data = json.load(f)
            result = []
            for player in data:
                if not self.filter.field or self.filter.field in player['Player']:
                    result.append(PlayerRushing(
                        player['Player'],
                        player['Team'],
                        player['Pos'],
                        player['Att/G'],
                        player['Att'],
                        player['Yds'],
                        player['Avg'],
                        player['Yds/G'],
                        player['TD'],
                        player['Lng'],
                        player['1st'],
                        player['1st%'],
                        player['20+'],
                        player['40+'],
                        player['FUM'],
                    ))
            return result


def get_db(filter: Filter, paginator: Paginator, sorters: list[Sorter]) -> Type[Db]:
    return JsonDb(filter, paginator, sorters)
