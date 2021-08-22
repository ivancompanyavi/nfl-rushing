from .entities import Filter, Paginator, Sorter
from flask import Blueprint, request, Response, abort, jsonify
from . import models


def build_filter(filter_by: str) -> Filter:
    return Filter(filter_by)


def build_sorters(sort_by: str) -> list[Sorter]:
    if not sort_by:
        return []
    sorters = []
    for s in sort_by.split(','):
        ascending = s[0] != '-'
        field = s[1:] if not ascending else s
        sorters.append(Sorter(field, ascending))

    return sorters


def build_paginator(page: str, offset: str) -> Paginator:
    if not page or not offset:
        return Paginator(0, 0)
    try:
        p = int(page)
        o = int(offset)
        return Paginator(p, o)
    except ValueError:
        abort(Response('Paginator parameters must be integers', 400))


def init(bp: Blueprint):
    @bp.route('/', methods=['GET'])
    def get_index():
        filter_by = request.args.get('filter_by', '')
        sort_by = request.args.get('sort_by', '')
        page = request.args.get('page', '')
        offset = request.args.get('offset', '')

        filter = build_filter(filter_by)
        paginator = build_paginator(page, offset)
        sorter = build_sorters(sort_by)

        data = models.get_player_rushings(filter, paginator, sorter)

        return jsonify(data)
