import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

requests.json = {"Recipient": "<ID1>", "Donor": "<ID2>"}

r = requests.get(server_name+"get_patients/lam146")
# r = requests.post(server_name + "compare", json=requests_json)
print(r.text)
print(r.json())

r = requests.get(server_name+"get_blood_type/M4")
t = requests.get(server_name+"get_blood_type/F4")
print(r.text)

request_json = {"Name": "lam146", "Match": "No"}
r = requests.post(server_name+"match_check", json=request_json)
print(r.text)