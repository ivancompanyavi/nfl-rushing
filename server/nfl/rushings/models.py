from .entities import Filter, Paginator, Sorter, PlayerRushing
from .db import get_db


def get_player_rushings(filter: Filter, paginator: Paginator, sorter: Sorter) -> list[PlayerRushing]:
    db = get_db(filter, paginator, sorter)

    player_data, total_results = db.query()

    return (player_data, total_results)
