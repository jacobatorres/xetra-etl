""" running the application! """

import logging
import logging.config

import yaml

def main():
	"""
	 ENTRY POINT 
	"""


	# parse yaml file
	config_path = '/Users/jacobtorres/Desktop/etl_pipeline_python/xetra-etl/configs/xetra_report1_config.yml'

	config = yaml.safe_load(open(config_path))

	print(config)

	# configure logging 
	log_config = config['logging']
	logging.config.dictConfig(log_config)
	logger = logging.getLogger(__name__)
	print(__name__)
	logger.info("This is a test message")








if __name__ == '__main__':
	main()