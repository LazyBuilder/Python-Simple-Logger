# SimplePythonLogger
A simple python logger module that can be integrated with any python project to get basic logging facility.

The script below has been written to setup logger for any python project.
The script will verify the absolute path and then creates the log folder if required.
The log file is rotated every-midnight.

Log Levels (From high to low severity  : CRITICAL, ERROR, WARNING, INFO, DEBUG)
This logger will log everthing starting from the lowest serverity.

Based on : https://docs.python.org/3/library/logging.html

### Inputs 
* loggerName : Name to used to create the logger. Used is creating hierarchy 
* logAbsolutePath : Location of the directory inside which the log file needs to be generated.This has to be a local accessible folder.
* logFileName : Name of the log file with which the file would be created.

### Output
* lg : log instance or incase of false the error message

### Methods
* setupLogger(loggerName,logAbsolutePath,logFilename)
This method creates the logger and then returns the logger instance for usage.

* closeLogger
This will shut-down all the logger instances running at the moment.
Each time you execute the setupLogger method a new logger instance would be initiated.

## How to use
### Instructions
* Download the [_logger.py](https://github.com/LazyBuilder/SimplePythonLogger/blob/master/_logger.py)
* Place it in the same folder as you other script
* Import the _logger.py in you main script and use it

Usage is shown in the [test_logger.py](https://github.com/LazyBuilder/SimplePythonLogger/blob/master/test_logger.py)

Click here to view a example of the [log file](https://github.com/LazyBuilder/SimplePythonLogger/blob/master/Test_File.log) generated
