import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

requests_json = {"name": "Laryssa Melnyk",
   "net_id": "lam146",
   "e-mail": "laryssa.melnyk@duke.edu"}

r = requests.post(server_name + "student", json=requests_json)
