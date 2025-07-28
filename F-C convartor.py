def f_to_c (f):
    c=5*(f-32)/9
    return c 
f= int(input("enter your farenhite value : "))
print(f"{round(f_to_c(f),2)}°c")