"""
Date : 5 Sept 2017
Author : Asit Deva
Description :
    The script below has been written to setup logger for any project
    where it is being used.
    The script will verify the absolute path and then creates the folder if required.
    The log file is rotated every-midnight.
    Log Levels (From high to low severity  : CRITICAL, ERROR, WARNING, INFO, DEBUG)
    This logger will log everthing starting from the lowest serverity.
    ** Please feel free to modify and use
    
    https://docs.python.org/3/library/logging.html
    
    Input 
    loggerName : Name to used to create the logger. Used is creating hierarchy 
    logAbsolutePath : Location of the directory inside which the log file needs to be generated.
    This has to be a local accessible folder.
    logFileName : Name of the log file with which the file would be created.

    Output
    status : if the setup of logger was sucessfull or not
    lg : log instance or incase of false the error message
"""

def setupLogger(loggerName,logAbsolutePath,logFilename):
    import logging,os
    
    try :
        if not (os.access(logAbsolutePath,os.F_OK)):
            print "LOGGER : Creating log directory at " + logAbsolutePath
            os.system("mkdir \"" + logAbsolutePath.replace("\\","\\\\") + "\"")
        else:
            print "LOGGER : Log Directory already present at " + logAbsolutePath
        
        lg = logging.Logger(loggerName)
        hdlr = logging.handlers.TimedRotatingFileHandler(logAbsolutePath + "\\" + logFilename + '.log','midnight',1)
        hdlr.suffix = "%Y-%m-%d"
        frmtr = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(frmtr)
        lg.addHandler(hdlr) 
        lg.setLevel(logging.DEBUG)
    except Exception, (e):
        print "LOGGER : Error occured " + str(e)
        lg = None
    else :
        return lg

def closeLogger():
    import logging
    
    print "LOGGER : Shutdown requested."
    
    try:
        logging.shutdown();
        print "LOGGER : Shutdown complete."
        return True
    except :
        print "LOGGER : Shutdown failed."
        return False