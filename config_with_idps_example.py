import requests
import xml.etree.ElementTree as ET
requests.packages.urllib3.disable_warnings()
import getpass
#from argparse
from base import get_api_key,api_get
import idps_sdk
from idps_sdk import idps_client


client = idps_client.IdpsClientFactory.get_instance(endpoint="vkm-e2e.ps.idps.a.intuit.com", api_key_id="v2-8a409fc1241a2", api_secret_key="key_v2-8a409fc1241a2.pem")

localuser = client.get_secret("secret/localcreds/localuser")
localpass = client.get_secret("secret/localcreds/localpass")
localapikey = client.get_secret("secret/localcreds/localapikey")

localusertext=localuser.get_string_value()
localpasstext=localpass.get_string_value()
localapikeytext=localapikey.get_string_value()

OUTPUT_FILE = open("output.xml",'w')

def get_candidate_config(device_ip,credentials):
        #options_dict = {'1':"/api/?type=op&cmd=<show><config><candidate></candidate></config></show>", '2':"/api/?type=op&cmd=<show><config><running></running></config></show>"}
        ######################
        #User Input
        #user_prompt = "Please select an option:\n\n"
        #user_prompt+= "1: Get Candidate Config of the device\n"
        #user_prompt+= "2: Get Running config of the device\n"
        #user_input = input(user_prompt)
        #print(user_input)
        #parser = argparse.ArgumentParser(description = "Exporting device configuration")
        #my_parser = parser.add_argument('Config Type',metavar='config_type',type=str,help='-c for candidate condif | -r for running config')
        #args = my_parser.parse_args()
        #print(args)


        api_path = "/api/?type=op&cmd=<show><config><candidate></candidate></config></show>"


        #Making the API call
        response = api_get(device_ip,credentials, api_path)
        #writing candidate config into an XML file
        try:
                OUTPUT_FILE.write(response.text)
                print("Output written to {}".format(OUTPUT_FILE.name))
                OUTPUT_FILE.close()
        except:
                print('Something went wrong. Could not perform the action')
        #returns response class that can be used in any other script
        return response


if __name__ == "__main__":

        #add credentials here
        device_ip= input("Device IP:")
        username = localusertext
        password = localpasstext

        credentials = (username,password)
        get_candidate_config(device_ip,credentials)
