from flask import request


class BaseController:
    def extract_query_params(self):
        sort_by = request.args.get('sortBy')
        sort_order = request.args.get('sortOrder')
        start = request.args.get('start')
        count = request.args.get('count')

        return sort_by, sort_order, int(start) if start is not None else 0, int(count) if count is not None else 0
