datos = "ID_123_ABC_Info" 

#SOLUCION RIGIDA YA QUE ENCONTRAMOS LA PRIMERA POSICIÓN SUMANDO 5 (+5)
#LO CUAL HACE QUE SI CAMBIASE LA LONGITU AL PRINCIPIO EL 5 YA NO VALE

#I D _ 1 2 3 _ A B  C   _  I   n    f  o 
#1 2 3 4 5 6 7 8 9  10 11  12  13  14  15

# #p1 = datos.find("_") + 5

#p2 = datos.rfind("_")

#sub_cadena_abc = datos[p1:p2]

#rint(sub_cadena_abc)

#---------------------------------

#SOLUCIÓN FLEXIBLE HECHA PERFECTAMENTE GARANTIZA QUE AUNQUE HUBIESE CAMBIOS 
#OBTENDREMOS LO QU QUEREMOS (LO QUE ESTA DENTRO DEL SEGUNDO "_" Y EL TERCER "_")

p1 = datos.find("_") 

p2 = datos.find("_", p1 + 1)

p3 = datos.find("_" , p2 + 1)

sub_cadena_abc = datos[p2 +1 :p3]

print(sub_cadena_abc)


