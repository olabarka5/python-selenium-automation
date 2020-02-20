a = int(input ("input first value "))
b = int(input ("input second value "))
c = int(input ("input third value "))
if a < b:
    if b < c:
        print (" c-max")
    else:
        print ("b-max")
else:
    if a > c:
        print ("a-max")
    else:
        print ("c-max")

