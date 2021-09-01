def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False 

        elif choice == 1:
            HDL_Driver()
        print(choice)

        elif choice == 2:
            LDL_Driver()
        print(choice)

    return choice


def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)

def hdl_input():
    hdl_value = int(input(("Enter HDL value: ")))
    return hdl_value

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def hdl_output(HDL_value, HDL_character):
    print("The HDL value of {} is condsidered {}".format(HDL_value, HDL_character))
    return


def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)

def ldl_input():
    hdl_value = int(input(("Enter LDL value: ")))
    return ldl_value

def ldl_analysis(LDL_value):
    if LDL_value >= 130:
        return "Normal"
    elif 130 <= HDL_value < 159:
        return "Borderline High"
    elif 160 <= HDL_value < 189:
        return "High"
    else:
        return "Very High"

def ldl_output(LDL_value, LDL_character):
    print("The LDL value of {} is condsidered {}".format(LDL_value, LDL_character))
    return  


interface()
        


    