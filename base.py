#############################################################
#This base file contains functions and classes that will
#be called in other modules
#
#All the scripts should be is same folder as the base file 
#for them to call functions from base
#############################################################

import requests
import xml.etree.ElementTree as ET
from requests.exceptions import HTTPError
requests.packages.urllib3.disable_warnings()



#A class for any device (firewall/panorama)

class device:
	def __init__(self,hostname,mgmt_ip,serial):
		self.hostname = hostname
		self.mgmt_ip = mgmt_ip
		self.serial = serial
"""
#Needs testing
class device:
	def __init__(self,**kwargs):
		allowed_keys=["serial",
						"connected",
						"unsupported-version",
						"hostname",
						"ip-address",
						"ipv6-address",
						"mac-add",
						"uptime",
						"family",
						"model",
						"sw-version",
						"app-version",
						"av-version",
						"wildfire-version",
						"threat-version",
						"url-db",
						"url-filtering-version",
						"logdb-version",
						"vpnclient-package-version",
						"global-protect-client-package-version",
						"prev-app-version",
						"prev-av-version",
						"prev-threat-version",
						"prev-wildfire-version",
						"domain",
						"ha-state",
						"peer-serial",
						"vpn-disable-mode",
						"operational-mode",
						"certificate-status",
						"certificate-subject-name",
						"certificate-expiry",
						"connected-at",
						"custom-certificate-usage",
						"multi-vsys",
						"vsys-name",
						"vsys-shared-policy-status",
						"vsys-shared-policy-md5sum",
						"last-masterkey-push-status",
						"last-masterkey-push-timestamp",
						"express-mode"]
		self.__dict__.update((key,False) for key in allowed_keys)
		self.__dict__.update((key,value) for key,value in kwargs.items() if key in allowed_keys)
"""		
		
#Function to make an API call
def api_get(device_ip,credentials, api_path):
	key = get_api_key(device_ip,credentials)
	base_url = "https://{0}/".format(device_ip)
	url = base_url+api_path+"&key="+key
	#print(url)
	try:
		response = requests.get(url, verify = False)
		response.raise_for_status()
	except HTTPError as e:
		print(e)

	return  response
	
#Function for an API PUSH
def api_set(device_ip,credentials,xpath_value,element_value):
	key = get_api_key(device_ip,credentials)
	base_url = "https://{0}/".format(device_ip)
	url = base_url+"/api/?type=config&action=set&key="+key+"&xpath="+xpath_value+"&element="+element_value
	print(url)
#	try:
#		response = requests.post(url, verify = False)
#		response.raise_for_status()
#	except HTTPError as e:
#		print(e)
#	return response	


#Need to change the arguments
def get_api_key(device_ip,credentials):
	url = "https://{0}/api/?type=keygen&user={1}&password={2}".format(device_ip,credentials[0],credentials[1])
	#response = api_call(device_ip, api_path = "/api/?type=keygen&user={0}&password={1}".format(creds),key = '')
	
	################
	try:
		response = requests.get(url, verify = False)
		response.raise_for_status()
	except HTTPError as e:
		print(e)
	###################
	
	root = ET.fromstring(response.content)

	for i in root.iter():
		if 'key'==i.tag:
			key = i.text
	return key

#Did not test yet

def diff(device_ip,credentials):
	key = get_api_key(device_ip,credentials)
	base_url = "https://{0}/".format(device_ip)
	api_path="/api/?type=op&cmd=<validate><full></full></validate>"
	url = base_url+api_path+"&key="+key
	print(url)
	try:
		response = requests.post(url, verify = False)
		response.raise_for_status()
	except HTTPError as e:
		print(e)
	print(response)

"""

def commit(device_ip,credentials):
	key = get_api_key(device_ip,credentials)
	base_url = "https://{0}/".format(device_ip)
	commit_path="/api/?type=commit&cmd=<commit></commit>"
	url = base_url+api_path+"&key="+key
		print(url)
	try:
		response = requests.post(url, verify = False)
		response.raise_for_status()
	except HTTPError as e:
		print(e)
	print(response)
"""

#Function to get key		
