"""
File to store constants
"""

from enum import Enum

class S3FileTypes(Enum):
	"""
	supported file types for S3
	"""

	CSV = 'csv'
	PARQUET = 'parquet'


class MetaProcessFormat(Enum):
	"""
	formation for MetaProcess class
	"""


	META_DATE_FORMAT = '%Y-%m-%d'
	META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
	META_SOURCE_DATE_COL = 'source_date' # arg_date = '2021-05-19'
	META_PROCESS_COL = 'datetime_of_processing' # processed_date
	META_FILE_FORMAT = 'csv'


	# arg_date = '2021-05-19'
	# src_bucket = 'xetra-1234'
	# trg_bucket = 'xetra-jacob-1234'
	# columns = ['ISIN', 'Date', 'Time', 'StartPrice', 'MaxPrice', 'MinPrice', 'EndPrice', 'TradedVolume']
	# trg_key = 'xetra_daily_report_'
	# trg_format = '.parquet'
	# meta_key = 'meta_file.csv'






