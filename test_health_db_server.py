from health_db_server import db

def test_add_database_entry():
    from health_db_server import add_datebase_entry
    answer = add_datebase_entry("David", 1, "O+")
    expected = [{"name": "David", "id": 1, "blood_type": "O+", "tests": []}]
    assert db == expected

def test_add_database_entry_2():
    from health_db_server import add_datebase_entry
    db.clear()
    answer = add_datebase_entry("Ann", 2, "O+")
    expected = [{"name": "Ann", "id": 2, "blood_type": "O+", "tests": []}]
    assert db == expected

def test_find_patient():
    from health_db_server import find_patient 
    from health_db_server import add_datebase_entry
    db.clear()
    excepted = {"name": "David", "id": 1, "blood_type": "O+", "tests": []}
    add_datebase_entry("David", 1, "O+")
    answer = find_patient(1)
    
    assert answer == excepted
