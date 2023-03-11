import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_FOLDER


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        if 'status' in item:
            self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        results = BASE_DIR / RESULTS_FOLDER
        now = dt.datetime.now()
        formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{formatted}.csv'
        file_path = results / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            ).writerows([
                ['Статус', 'Количество'],
                *sorted(self.count_status.items()),
                ['Суммарно', sum(self.count_status.values())]
            ])
