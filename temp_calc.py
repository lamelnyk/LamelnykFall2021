def detect_fever(tempurature_list):
    fever_limit = 100.0
    for temperature in tempurature_list:
        if temperature >= fever_limit:
            return True
    return False