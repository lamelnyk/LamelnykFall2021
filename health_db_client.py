import requests


def add_patient_to_server(name_input, id_input, blood_type_input):
    patient1 = {"name": name_input, "id": id_input,
                "blood_type": blood_type_input}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
    print(r.status_code)
    print(r.text)
    return r.text
