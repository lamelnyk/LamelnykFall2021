def input_values():
    print("Input two points to create a slope of the line")
    cord1 = input("Input the first x and y values separated by a comma: ")
    cord2 = input("Input the second x and y values separated by a comma: ")
    value3 = int(input("Input an x value on the line: "))
    list1 = cord1.split(",")
    tuple1 = tuple(list1)
    list2 = cord2.split(",")
    tuple2 = tuple(list2)
    print('Coordinate 1 is: ',tuple1)
    print('Coordinate 2 is: ',tuple2)
    return tuple1, tuple2, value3


def calculate_slope(tuple1,tuple2):
    slope = (int(tuple2[1]) - int(tuple1[1]))/(int(tuple2[0]) - int(tuple1[0]))
    # print("The slope of the line is {}" .format(slope))
    return slope

def calculate_y3(slope, tuple1, value3):
    y3_value = slope * (value3 - int(tuple1[0])) + int(tuple1[1])
    print("The corresponding y values is {}" .format(y3_value))
    return y3_value 

def lin_plot_driver():
    tuple1, tuple2, value3 = input_values()
    slope = calculate_slope(tuple1, tuple2)
    y3_value = calculate_y3(slope, tuple1, value3)

if __name__ == "__main__":
    lin_plot_driver()
