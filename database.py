class Patient: 

    def __init__(self, name, id_no, age):
        self.name = name
        self.id_no = id_no
        self.age = age
        self.test = []

    def __repr__(self):
        return "{}: {}".format(self.id_no, self.name)

#def class_work():
    #new_patient = Patient("Ann Ables", 120, 36)
    #print(new_patient.id_no)
    #print(new_patient.name)
    #x = Patient("Bob Boyles", 24, 33)
    #print (x.name)

def create_database_entry(patient_name, id_no, age):
    new_patient = Patient(patient_name, id_no,age)
    #new_patient = {"name": patient_name, "id_no": id_no, "age": age, "tests": []}
    return new_patient

def print_database(db):
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for patient, location in zip(db, locations):
        print ("{} - {}". format(patient, location))

#def get_patient_age():

def get_patient(db, id_no):
    patient = db[id_no]
    return patient

def main():
    db = {}
    x = create_database_entry("Ann Ables", 120, 30)
    db[x.id_no] = x
    x = create_database_entry("Bob Boyles", 24, 31)
    db[x.id_no] = x
    x = create_database_entry("Chris Chou", 33 ,33 )
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 14, 34)
    db[x.id_no] = x
    print(db)

    patient_id_tested = 24
    test_done = ("HDL", 65)
    
    patient = get_patient(db, patient_id_tested)
    patient.test.append(test_done)
    print(db[24].test)




if __name__ == "__main__":
    main()