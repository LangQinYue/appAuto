#!coding=utf-8
'''
Created on 2016年11月3日

@author: lx-lang.qinyue
'''
import os
#from robot.variables import GLOBAL_VARIABLES
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from keywordgroup import KeywordGroup

class Logging(KeywordGroup):

    # Private

    def _debug(self, message):
        logger.debug(message)

    def _get_log_dir(self):
        logfile = GLOBAL_VARIABLES['${LOG FILE}']
        if logfile != 'NONE':
            return os.path.dirname(logfile)
        return GLOBAL_VARIABLES['${OUTPUTDIR}']

    def _html(self, message):
        logger.info(message, True, False)

    def _info(self, message):
        logger.info(message)

    def _log(self, message, level='INFO'):
        level = level.upper()
        if (level == 'INFO'): self._info(message)
        elif (level == 'DEBUG'): self._debug(message)
        elif (level == 'WARN'): self._warn(message)
        elif (level == 'HTML'): self._html(message)
        elif (level=='Error'):self._error(message)
        
    def _error(self,message):
        raise AssertionError(message)
     
    def _warn(self, message):
        logger.warn(message)