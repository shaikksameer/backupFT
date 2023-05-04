attempts=0
while attempts<3:
    password=input("enter you pws: ")
    has_upper = 0
    has_lower = 0
    has_special = 0
    has_number = 0
    arr=[]
    for i in range (0,len(password)):
        num=ord(password[i])
        arr.append(num)
    print(arr)
    for i in password:
        if ord(i) in range (65,92):
            has_upper += 1
        elif ord(i) in range (97,123):
            has_lower += 1
        elif i in ('@','#','$'):
            has_special += 1
        elif ord(i) in range (48,55):            
            has_number += 1
    if has_upper >0 and has_lower>0 and has_special>0 and has_number>0:
            print("Password is accepted ")
            break;
    else:
        print("Password is wrong try again ")
        attempts+=1
if(attempts==3):
    print("Bye Bye")
    
'''
1)what is a procedural language?
->  Python is a high-level, interpreted, general-purpose programming language. It is 
    often considered a multi-paradigm language, as it supports various programming paradigms, 
    including object-oriented, imperative, functional, and procedural programming.
    
2)What is complex and frozenset datatype?   
->  The complex data type in python consists of two values, the first one is the real part of the complex number, 
    and the second one is the imaginary part of the complex number.

'''

    
    









