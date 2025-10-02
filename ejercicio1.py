#Ejercicio 1, 50 manzanas repartidas entre 6 personas
manzanas = 50 
P = 6
repartidas = manzanas // P #división entera
print(repartidas) #cantidad de manzanas que le tocan a cada uno
sobran = manzanas % P
print ("sobran: ", sobran)

#ejercicio semana y días que sobran
curso = 100
dias = 7
semanastotales = curso // dias
print(semanastotales) # cuantas semanas son
sobr = curso % dias
print("sobran: ", sobr) # cuantos dias sobran

#Ejercicio triángulo
a = 7
b = 8
c = 9
s = (7 + 8+ 9)/ 2
A = (s * (s - a) * (s - b) * (s - c)) ** (1/2) 
print("Dado un triángulo con lados de a=7, b=8 y c=9, su semiperímetro es: ")
print(s)
print(" Y su área determinada por la fórmula de Herón es: ") 
print (A)



#x^2 - 5x + 6 =  0
a1 = 1
b1 = -5
c1 = 6
x1_1 = (-(b1) + (((b1 ** 2) - (4 * a1 * c1)) ** (1/2))) / (2 * a1) 
x1_2 = (-(b1) - (((b1 ** 2) - (4 * a1 * c1)) ** (1/2))) / (2 * a1)
print("x1: ", x1_1) #raiz 1
print("x2: ", x1_2) #raiz 2

#x^2 + 4x + 13 =0
a2 = 1
b2 = 4
c2 = 13
x2_1 = (-(b2) + (((b2 ** 2) - (4 * a2 * c2)) ** (1/2))) / (2 * a2)
x2_2 = (-(b2) - (((b2 ** 2) - (4 * a2 * c2)) ** (1/2))) / (2 * a2)
print("x1: ", x2_1) #raiz 1
print("x2: ", x2_2) #raiz 2