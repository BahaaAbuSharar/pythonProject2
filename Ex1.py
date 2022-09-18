
my_condition = True
input_name = input("Enter your name: ")
# to te real name
m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in m:
    con = str(i) in input_name
    if con or input_name == "":
        print("Error")
        my_condition = False
        break

if my_condition:
    input_age = input("Enter your age: ")
    con2 = input_age.isdigit() and not input_age == ""
    if con2:
        pass
    else:
        print("Error")
        my_condition = False

if my_condition:
    input_address = input("Enter your address: ")
    if input_address == "":
        print("Error")
    else:
        print("Hello Ms/Mr", input_name, "age", input_age, "located in", input_address, ".",
              "thanks for beening one of our community,          Enjoy")

