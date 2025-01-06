def funct ():
    a = "I am defined inside a function hence local function"
    print (a)

"""calling the function below"""
funct()
"""now lets try and call a outside the function"""
print(a) #throwing an error NameError: name 'a' is not defined