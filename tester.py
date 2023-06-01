import argparse
import yaml
import requests
 
class Colors:
    '''
    Lets make our world colorful!!!
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_yaml(file_path):
    '''
    Loads the yaml file and returns the datastructure
    '''
    if not file_path:
        file_path = 'TestCases.yaml'
    with open(file_path, 'r') as file:
        try:          
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            #fails if yaml is unable to load
            print(Colors.FAIL + f"Error loading YAML file: {e}" + Colors.ENDC)

def validate(resp_data, valid_data):
    '''
    Validates the key value pair in the validate block in yaml file corresponds to 
    the response form the API. 
    Returns True if the key and value are same else returns False.
    '''
    result = True
    for key in valid_data:
        try:
            if valid_data[key] != resp_data[key]: 
                print(Colors.WARNING + f"Value does not match for key : {key}" + Colors.ENDC) 
                result = False
        except KeyError:
            print(Colors.WARNING + f"Key is not present : {key}" + Colors.ENDC)
            result = False            
    return result

def promotion_vaidate(resp_data, valid_data):
    '''
    Validates that the promotions elements from the api response contains the dictionaries given in the 
    validate_promotion block in the yaml file.
    Returns True if the response contains the dict in the yaml file else returns False.
    '''
    for item in resp_data:
        if valid_data.items() <= item.items():
            return True
    return False
        
def main():
    parser = argparse.ArgumentParser(description='Tester script to test API')
    parser.add_argument('-f', '--file', type=str, help='Path to the test file')
    args = parser.parse_args()
    file_path = args.file
    #load the yaml file
    test_data = load_yaml(file_path)
    for test in test_data.keys(): 
        print(Colors.HEADER + test + Colors.ENDC)
        #check the Execute keyword is true or false
        if not test_data[test]['Execute']:
            print(Colors.OKBLUE + f"Execute is false for this case." + Colors.ENDC)
            continue
        #get the method and api for the testcase
        method = test_data[test]['method']
        api = test_data[test]['API']
        #check the method and get the response
        if method.upper() == 'GET':
            response = requests.get(api)
        else:
            print(Colors.FAIL + f"Method not supported currently: {method}" + Colors.ENDC)
            continue
        #process the response
        if response.status_code == 200:
            #get the response in a jason format
            resp_data = response.json()
            try:
                if test_data[test]['validate'].keys(): 
                    #check the response from api with the data in testcase
                    testcase_status = validate(resp_data,test_data[test]['validate'])
                    if testcase_status:
                        print(Colors.OKGREEN + f"Testcase {test} passed for validation checks!!!" + Colors.ENDC)
                    else:
                        print(Colors.FAIL + f"Testcase {test} failed for validation checks!!!" + Colors.ENDC)
            except KeyError:
                pass
            try:
                #check the response from api for the promotions element with the data in testcase 
                if test_data[test]['validate_promotion'].keys():
                    testcase_status = promotion_vaidate(resp_data['Promotions'], test_data[test]['validate_promotion'])
                    if testcase_status:
                        print(Colors.OKGREEN + f"Testcase {test} passed for promotion checks!!!" + Colors.ENDC)
                    else:
                        print(Colors.FAIL + f"Testcase {test} failed for promotion checks, the dict given is not present!!!" + Colors.ENDC)
            except KeyError:
                pass  
        else:
            print(Colors.FAIL + f"Failed to retrieve data from the API. Status code: {response.status_code}" + Colors.ENDC)
        
if __name__ == "__main__":
    main()    
