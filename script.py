# Python Syntaxis
# 1
print("Hello World")
# 2
# This is a comment

#  Python Variables
# 1
carname = "Voldo"
# 2
x = 50
# 3
x = 5
y = 10
print(x+y)
# 4
x = 5
y = 10
z = x + y
print(z)

#  Python String
# 1
x = "Hello World"
print(len(x))#Longitud
# 2
txt = "Hello World"
x = txt[0] # imprimir H
# 3
txt = "Hello World"
x = txt[2:5] # posiciones
# 4
txt = " Hello World "
x = txt.strip() # Quitar espacios principio y final
# 5
txt = "Hello World"
txt = txt.upper() # Convertir en Mayusculas
# 6
txt = "Hello World"
txt = txt.lower() # Convertir en Minuscula
# 7
txt = "Hello World"
txt = txt.replace("H", "J") # Replazar una letra por otra

# Python Operadores
# 1
print(10 * 5) # Multiplicacion
# 2
print(10 / 2) # Division
# 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!") # con in miramos si apple esta en el diccionario de fruits
# 4
if 5 != 10:
  print("5 and 10 is not equal") # si el numero el diferente de 
# 5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true") # Verificamo si alguna de las dos condiciones es verdadera

# Pyhton Listas
# 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1]) # imprimir la segunda posicion
# 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi" # Renombrar en la posicion correcta
# 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # vamos agregar a nuestro diccionario una nueva fruta utilizando append
# 4 
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon") # insertemos un nuevo elemento sin eliminarlo
# 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") # remover

# Python Tuples - Tuplas
# 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# 2
fruits = ("apple", "banana", "cherry")
print(len(fruits)) # imprimir nuemro de itms

# Python Sets (Conjuntos)
# 1
fruits = {"apple", "banana", "cherry"}
if ("apple" in fruits):
  print("Yes, apple is a fruit!") # revisar si apple esta en fruits
# 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange") # otra manera de agregar items
# 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) # agregar multiples items a un diccionario
# 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") # remover
# 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") # otro metodo para remover

# Python Diccionarios
# 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model")) # imprimir el valor de modelo
# 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2018 # cambiar valor
# 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red" # agregar Color al diccionario
# 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model") # Elimimar item del diccionario
# 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear() # vamos a vaciar car y quedara {}

# Python Condicionales If ... Else
# 1
a = 50
b = 10

if a > b:
  print("Hello World") # si a es mayor que b entonces
# 2
a = 50
b = 10

if a != b:
  print("Hello World") # si a es diferente a b entonces
# 3
a = 50
b = 10

if a == b:
  print("Yes")
else:
  print("No") # si a es igual a b entonces imprime si de lo contrario imprime no
# 4
a = 50
b = 10

if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
# 5
if a == b and c == d:
  print("Hello")
# 6
if a == b or c == d:
  print("Hello")

# Python Loops (Bucles)
# 1
i = 1

while i < 6:
  print(i)
  i += 1
# 2
i = 1
while i < 6:
  if i == 3:
      break
      i += 1
# 3
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
# 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
      print(x)
# 5
for x in range(6)
  print(x)

# Python Funciones
# 1
def my_function():
    print("Hello from a function")
# 2
def my_function():
    print("Hello from a function")
my_function()
# 3
def my_function(fname, lname):
    print(fname)
# 4
def my_function(x):
    return x + 5
# 5
x = lambda a : a

