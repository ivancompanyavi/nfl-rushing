from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Sorter:
    field: str
    ascending: bool


@dataclass
class Paginator:
    page: int
    offset: int


@dataclass
class Filter:
    field: str


@dataclass
class PlayerRushing:
    name: str
    team: str
    position: str
    avg_attempts_per_game: int
    attempts: int
    yards: int
    avg_yards_per_attempt: int
    avg_yards_per_game: int
    touchdowns: int
    longest_rush: str
    first_down: int
    first_down_pct: int
    twenty_plus_yards: int
    forty_plus_yards: int
    fumbles: int

    def build_from_obj(self, obj):
        self.name = obj['Player']
        self.team = obj['Team']
        self.position = obj['Pos']
        self.avg_attempts_per_game = obj['Att/G']
        self.attempts = obj['Att']
        self.yards = obj['Yds']
        self.avg_yards_per_attempt = obj['Avg']
        self.avg_attempts_per_game = obj['Yds/G']
        self.touchdowns = obj['TD']
        self.longest = obj['Lng']
        self.first_down = obj['1st']
        self.first_down_pct = obj['1st%']
        self.twenty_plus_yards = obj['20+']
        self.forty_plus_yards = obj['40+']
        self.fumbles = obj['FUM']


class Db:
    """Generic Db class. Given a sorter, a paginator and the database data, it returns the result of the query """

    def __init__(self, filter: Filter, paginator: Paginator, sorters: list[Sorter]) -> None:
        self.filter = filter
        self.sorters = sorters
        self.paginator = paginator

    def query(self) -> list[PlayerRushing]:
        raise NotImplementedError
