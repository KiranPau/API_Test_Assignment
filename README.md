This Script is use to check the response from a given api endpoint and validates the response with the given condotions in the input yaml file. 

Here is the structure of the yaml file.

<Name of the testcase>:
  Description: <Enter the description for the testcase>(This section is optional)
  Execute: <True or False> (Runs the testcase id this parameter is true)
  method: <method used in the testcase>(Currently GET method is supported)
  API: <api endpoint to test> 
  validate:(this keyword will validate the components in the below section to the content in the response)
    <key1>: <value1>
    <key2>: <value2> 

Example for the above case:
TestCase-1:
  Description: "Testcase to check the first criteria"
  Execute: True
  method: GET
  API: https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false 
  validate:
    Name: "Carbon credits"

<Name of the testcase>:
  Description: <Enter the description for the testcase>(This section is optional)
  Execute: <True or False> (Runs the testcase id this parameter is true)
  method: <method used in the testcase>(Currently GET method is supported)
  API: <api endpoint to test> 
  validate_promotion:(this keyword will validate the componets in the below section to the content in the promotions section of the response)
    <key1>: <value1>
    <key2>: <value2> 

Example for the above case:
TestCase-3:
  Description: "Testcase to check the third criteria"
  Execute: True
  method: GET
  API: https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false 
  validate_promotion:
    Name: "Gallery"
    Description: "Good position in category"

The script loads the yaml file, it goes through each of the testcases and reads the configurations. The parameter "method" is the http method which should be used in the testcase, currently we just use the GET method. We can add the other methods in future as the situation demands. Parameter API is the url which need to be used with the method. Parameter Validate will get the key value pairs in the block and check for those values in the api response, if all the values are present in the response the testcase passes otherwise the testcase fails. Parameter validate_promotion will only match the rest of the block with the promotions element in the response and if the block is a subset of one of the dictionaroes in the list, the testcase is passed otherwise the result is failed. We can use both validate and validate_promotion in the same test case. 


Dependencies
 Python is a prerequisite for the script. Below modules are also needed.
 Python requests - ('pip install requests' in command promt)
 Python yaml - ('pip install pyyaml' in command promt)
 Python argparse - ('pip install argparse' in command promt)

Usage
python tester.py -f <path-to-testcase-file>
python tester.py --file <path-to-testcase-file>
python tester.py (this command needs the testcase file by name TestCases.yaml in the same folder as the script tester.py)

