import idps_sdk
from idps_sdk import idps_client


client = idps_client.IdpsClientFactory.get_instance(endpoint="vkm-e2e.ps.idps.a.intuit.com", api_key_id="v2-8a409fc1241a2", api_secret_key="key_v2-8a409fc1241a2.pem")
#f = client.get_folder("root")
client.create_folder("srikanth5")
client.get_folder("srikanth5")
client.create_secret("srikanth5/corp_id", "superdupertopsecrepythontest")
s = client.get_secret("srikanth5/corp_id")
x=s.get_string_value()
print(x)


