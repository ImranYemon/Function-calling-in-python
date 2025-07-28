def Greatest(a,b,c):
    if (a>b and a>c):
        print("gratest number = a")
        return a 
    elif(b>a and b>c):
        print("gratest number = b")
        return b 
    else:
        print("gratest number = c")
        return c 
    
a =int(input("enter number a:")) 
b =int(input("enter number b:"))
c =int(input("enter number c:"))

print(Greatest(a,b,c))