import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_FOLDER, FILE


class PepParsePipeline:
    def __init__(self):
        self.results_directory = BASE_DIR / RESULTS_FOLDER
        self.results_directory.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_directory / FILE.format(
            dt.now().strftime(DATETIME_FORMAT))
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            ).writerows([
                ['Статус', 'Количество'],
                *sorted(self.count_status.items()),
                ['Суммарно', sum(self.count_status.values())]
            ])
