import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, filename='log.log')
#logging.basicConfig(level=logging.DEBUG, format="%(name)s %(asctime)s %(levelname)s %(message)s")
#logging.info("INFO")

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
