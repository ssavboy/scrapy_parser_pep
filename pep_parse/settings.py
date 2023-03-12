from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_FOLDER = 'results'
URL = 'https://{domain}/'
FILE = 'status_summary_{time}.csv'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
FEEDS = {
    f'{RESULTS_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
