import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__) #filename of the test

    fileHandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.INFO)

    logger.debug("debug statement is executed")
    logger.info("Info of the testcase")
    logger.warning("log.warning - something is not correct")
    logger.error("Failure of testcase")
    logger.critical("BLOCKER")
