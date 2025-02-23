from air_project.logger import logging
from air_project.exception import air_ProjectException
import sys

logging.info("welcome to custome logging")

try:
    a = 2/10
except Exception as e:
    raise air_ProjectException(e,sys)