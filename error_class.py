a = "the sky is blue"

print(a)
for letter in a:
    print(letter)

def function_name():
    try: 
        from my_math_calculator import sqrt 
    except ModuleNotFoundError:
        from math import sqrt
    x = sqrt(4)
    print(x)

def main():
    function_name()
    from my_math_calculator import add_postive_integer 
    try: 
        x = add_postive_integer
        print(x)
    except ValueError:
        print("Got value error")


if __name__ == "__main__":
    main()