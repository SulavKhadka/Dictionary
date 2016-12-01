# Dictionary

Still Pre-alpha.

A very simple python module that gives the user the definition of a given word. Works from command line or can be used to integrate into another project.

This script is a part of a bigger project I have called CHESTER. Currently I am using this as a part of the CHESTER Knowledgebase.

## Requirements


dictionaryapi.com api key: http://www.dictionaryapi.com/register/index.htm
  
## Usage


**Command line:**
```
python Dictionary.py *word*
```
**Code Integration:**
```
import Dictionary

output_dict = Dictionary.dictionary_info(query, API_KEY)        #gets parsed info from the dictionary api
Dictionary.display_output(output_dict)        #prints the results from output_dict 
```
