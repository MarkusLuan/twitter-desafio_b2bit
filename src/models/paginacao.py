class Paginacao:
    """ Classe modelo de paginalção """
    def __init__(self, first_result: int = 0, max_results: int = 0, ts_after: int = 0, ts_before: int = 0, *args, **kwargs):
        self.first_result = int(first_result)
        self.max_results = int(max_results)
        self.ts_after = int(ts_after)
        self.ts_before = int(ts_before)