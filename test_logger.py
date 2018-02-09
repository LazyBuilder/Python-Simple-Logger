# -*- coding: utf-8 -*-
"""
Date : 5 Sept 2017
Author : Asit Deva
Description : Logger example usage.
"""
print "******************* Logger Test Program *******************"

import _logger as logger

print "Logger setup requested"

log = logger.setupLogger("Test Logger","C:\Python Test Logs","Test_File")

if log is None:
    print "\nLogger is not set"
else:
    print "\nLogger is set."
    log.debug("This is an debug log.")
    log.info("This is an info log.")
    log.warning("This is an warning log.")
    log.error("This is an error log.")
    log.critical("This is an critical log.")

if logger.closeLogger():
    print "\nLogger has been closed"