import numpy as np   
print("Capitalizing the string using capitalize()...")  
print(np.char.capitalize("welcome to numpy"))   #Welcome to numpy
print(np.char.title("welcome to numpy")) #Welcome To Numpy
print(np.char.lower("NUMPY"))#numpy
print(np.char.upper("numpy")) #NUMPY
print(np.char.strip("  numpy  ")) #numpy
print(np.char.split("python is easy language",sep=" ")) #['python', 'is', 'easy', 'language']
