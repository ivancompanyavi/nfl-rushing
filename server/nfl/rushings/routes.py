from flask import Blueprint, request, Response, abort, jsonify
import csv
from io import StringIO
from dataclasses import asdict
from .entities import Filter, Paginator, PlayerRushing, Sorter
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
    @bp.route('/', methods=['GET', 'HEAD'])
    def get_index():
        filter_by = request.args.get('filter_by', '')
        sort_by = request.args.get('sort_by', '')
        page = request.args.get('page', '')
        offset = request.args.get('offset', '')

        filter = build_filter(filter_by)
        paginator = build_paginator(page, offset)
        sorter = build_sorters(sort_by)

        data, total_results = models.get_player_rushings(
            filter, paginator, sorter)

        return jsonify({'data': data, 'total': total_results})

    @bp.route('/download', methods=['GET'])
    def get_csv_data():
        filter_by = request.args.get('filter_by', '')
        sort_by = request.args.get('sort_by', '')

        filter = build_filter(filter_by)
        sorter = build_sorters(sort_by)
        si = StringIO()
        cw = csv.writer(si)

        cw.writerow(asdict(PlayerRushing()).keys())
        data, _ = models.get_player_rushings(filter, None, sorter)
        cw.writerows([asdict(p).values() for p in data])
        return Response(
            si.getvalue(),
            mimetype="text/csv",
            headers={"Content-disposition":
                     "attachment; filename=rushings.csv"})
