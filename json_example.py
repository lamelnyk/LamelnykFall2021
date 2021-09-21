import json

def create_person():
    new_person = { "First Name" : "Anna",
                    "Last Name": "Ables",
                    "Age": 35, 
                    "Visits": ["1/1/2020", "2/2/2020", "3/3/2020"]}
    return new_person

def output_json(my_dict):
    filename = "mybooleans.json"
    out_file = open(filename, 'w')
    json.dump(my_dict, out_file)
    out_file.close()

# second wat to write the json file method above 
def output_json_with(output_data):
    filename = "my_output.txt"
    with open(filename, 'w') as out_file:
        json.dump(output_json,out_file)
    print("output data has finshished")

def create_list():
    return [True, False, True]

if __name__ == "__main__":
    #person = create_person()
    #print(person)
    #output_json(person)
    data_to_output = create_list()
    output_json(data_to_output)