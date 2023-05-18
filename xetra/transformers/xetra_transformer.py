""" Xetra ETL component """

from typing import NamedTuple

from xetra.common.s3 import S3BucketConnector

import logging 



class XetraSourceConfig(NamedTuple):

	"""
	Class for source config data

	src_first_extract_date: determines the date for extracting the source
	src_columns: source column name
	src_col_date: column name for date in source
	src_col_isin: column name for isin in source
	src_col_time: column name for time in source
	src_col_start_price: column name for starting price in source
	src_col_min_price: column name for minimum price in source
	src_col_max_price: column name for maximum price in source
	src_col_traded_vol: column name for traded volume in source

	"""


	src_first_extract_date: str 
	src_columns: list 
	src_col_date: str 
	src_col_isin: str 
	src_col_time: str 
	src_col_start_price: str 
	src_col_min_price: str 
	src_col_max_price: str 
	src_col_traded_vol: str 



class XetraTargetConfig(NamedTuple):


	"""
	Class for target config data

	trg_first_extract_date: determines the date for extracting the target
	trg_columns: target column name
	trg_col_date: column name for date in target
	trg_col_isin: column name for isin in target
	trg_col_time: column name for time in target
	trg_col_start_price: column name for starting price in target
	trg_col_min_price: column name for minimum price in target
	trg_col_max_price: column name for maximum price in target
	trg_col_traded_vol: column name for traded volume in target

	"""


	trg_first_extract_date: str 
	trg_columns: list 
	trg_col_date: str 
	trg_col_isin: str 
	trg_col_time: str 
	trg_col_start_price: str 
	trg_col_min_price: str 
	trg_col_max_price: str 
	trg_col_traded_vol: str 




class XetraETL():

	""" 
	Reads the Xetra Data, transforms and writes the transformed to target
	"""


	def __init__(self,
				s3_bucket_src: S3BucketConnector,
				s3_bucket_trg: S3BucketConnector,
				meta_key: str,
				src_args: XetraSourceConfig,
				trg_args: XetraTargetConfig
				):

		""" 
		Constructor for XetraTransformer

		:param s3_bucket_src: connection to source bucket
		:param s3_bucket_trg: connection to target bucket
		:param meta_key: used as self.meta_key -> key of meta file
		:param src_args: NamedTuple class with source config data
		:param trg_args: NamedTuple class with target config data

		"""
		self._logger = logging.getLogger(__name__)
		self.s3_bucket_src = s3_bucket_src
		self.s3_bucket_trg = s3_bucket_trg
		self.meta_key = meta_key
		self.src_args = src_args
		self.trg_args = trg_args
		self.extract_date = ''
		self.extract_date_list = ''
		self.meta_update_list = ''


		def extract(self):
			pass

		def transform_report1(self):
			pass

		def load(self):
			pass 

		def etl_report1(self):
			pass



























