### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
 
my_bool_variable = False
print(my_bool_variable)

# Contatenación de variables en un print + uso de type + 'NoneType' ya que print no 
# tiene type ya que es una función no un tipo de dato
print(type((print(my_string_variable, my_int_to_str_variable, my_bool_variable)))) 


# Algunas funciones del sistema len cuenta 
print(len(my_string_variable))



