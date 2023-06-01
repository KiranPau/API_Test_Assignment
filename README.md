## Table of contents
* [General info](#general-info)
* [Yaml Structure](#Yaml-Structure)
* [Working](#working)
* [Dependencies](#Dependencies)
* [Usage](#usage)

## General info
This Script is used to check the response from a given api endpoint and validates the response with the given conditions 
in the input yaml file. This will give the user a generic and easy way to configure the testcases.
 
## Yaml Structure
Let's take a look at typical structure of the yaml file.
First structure is for the case where we need to validate a dictionary in the response from API. Please find the
breakdown and an example.
```yaml
<Name of the testcase>:
  Description: <Enter the description for the test case> (This section is optional)
  Execute: <True or False> (Runs the test case id this parameter is true)
  method: <method used in the testcase> (Currently GET method is supported)
  API: <api endpoint to test>
  validate(this keyword will validate the components in the below section to the content in the response):
    <key1>: <value1>
    <key2>: <value2>
 ```
Example for the above case:
```yaml
TestCase-1:
  Description: "Test Case to check the first criteria"
  Execute: True
  method: GET
  API: https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
  validate:
    Name: "Carbon credits"
```
Second case is where we need to validate data which is under the promotions element. Please find the breakdown and 
example for that.
```yaml
<Name of the testcase>:
  Description: <Enter the description for the test case> (This section is optional)
  Execute: <True or False> (Runs the test case id this parameter is true)
  method: <method used in the testcase> (Currently GET method is supported)
  API: <api endpoint to test>
  validate_promotion(to validate the components in the section to the content in promotions section of response):
    <key1>: <value1>
    <key2>: <value2>
 ```
Example for the above case:
```yaml
TestCase-3:
  Description: "Test Case to check the third criteria"
  Execute: True
  method: GET
  API: https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false
  validate_promotion:
    Name: "Gallery"
    Description: "Good position in category"
 ```
## Working
The script loads the yaml file, it goes through each of the test cases and reads the configurations. The parameter 
"method" is the http method which should be used in the testcase, currently we just use the GET method. We can add 
the other methods in future as the situation demands. Parameter API is the url which needs to be used with the 
method. Parameter Validate will get the key value pairs in the block and check for those values in the api response,
if all the values are present in the response the test case passes otherwise the test case fails. Parameter 
validate_promotion will only match the rest of the block with the promotions element in the response and if the 
block is a subset of one of the dictionaries in the list, the test case is passed otherwise the result is failed. 
We can use both validate and validate_promotion in the same test case.
 
## Dependencies
 Python is a prerequisite for the script. 
 Below modules are also needed.
 Python requests
```
pip install requests
```
 python yaml
```
pip install pyyaml
```
 Python argparse
``` 
pip install argparse
```
## Usage
```
python tester.py -f <path-to-testcase-file>
python tester.py --file <path-to-testcase-file>
```
Below command needs the test case file by name TestCases.yaml in the same folder as the script tester.py
```
python tester.py 
```