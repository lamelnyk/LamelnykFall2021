def create_database_entry(patient_name,id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient

# allows you to print the patient names, by changing what is printed you are able to print out
# different entries
def print_database(db):
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for patient, location in zip(db, locations):
        print("{}  -  {}".format(patient , locations))

def print_over_age(age, db):
    for patient in db:
        if patient[2] > age:
            print(patient[0])

def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient 

def main():
    db = []
    x = create_database_entry("Ann Ables", 120, 30)
    db.append(x)
    x = create_database_entry("Bob Boyles", 24, 31)
    db.append(x)
    x = create_database_entry("Chris Chou", 33, 33)
    db.append(x)
    x = create_database_entry("David Dinkin", 14, 34)
    db.append(x)
    
    patient_id_tested =24
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    patient[3].append(test_done)

    # allows you use python functionality to show you what is in the code 
    #y = db[1]
    #print(y)

    # shows you the last entry and if you -2 shows you the second to last entry 
    #z = db[-1]
    #print(z)

    #yy = db[1:3]

    print_database(db)

    #print_over_age(32, db)


if __name__ == "__main__":
    main()