### Functions ###

def my_fuction():
    print("Esto es una función")
    
my_fuction()
my_fuction()
my_fuction()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_whith_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_whith_return(10, 5)
print(my_result)

def print_name(name, sourname):
    print(f"{name} {sourname}")
    
print_name(sourname = "SinBugs", name = "Codigo")

def print_name_with_default (name, sourname, alias = "Sin Alias"):
    print(f"{name} {sourname} {alias}")

print_name_with_default("Codigo", "SinBugs", "CSB")
print_name_with_default("Codigo", "SinBugs")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola")
print_upper_texts("Hola", "Python", "csb")