# Dictionary

A very simple python module that gives the user the definition of a given word. Works from command line or can be used to integrate into another project.

This script is a part of a bigger project I have called CHESTER. Currently I am using this as a part of the CHESTER Knowledgebase.

## Requirements


dictionaryapi.com api key: http://www.dictionaryapi.com/register/index.htm
  
## Usage


**Command line:**
```
python Weather.py fullReport
python Weather.py shortReport
```
**Code Integration:**
```
import Weather
print Weather.generate_report(fullReport, API_KEY) #Gets full weather report
print Weather.generate_report(shortReport, API_KEY) #Gets basic weather report
A simple dictionary module made in python.

*Still Pre-alpha*
