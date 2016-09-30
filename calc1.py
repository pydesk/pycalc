import math
print("python calculator")
print("a little github project")
print("written and coded by : webtech")
# end of introduction
# start of function
def add(): # the adding function
    xstring = input('enter 1st value :')
    x = int(xstring)
    ystring = input('enter 2nd value :')
    y = int(ystring)
    print('result is :' , x+y)
def minus(): # the minus function
    astring = input('enter value :')
    a = int(astring)
    bstring = input('enter 2nd value :')
    b = int(bstring)
    print('result is :' , a-b)
def into(): # the into function
    cstring = input('enter value :')
    c = int(cstring)
    dstring = input('enter 2nd value :')
    d = int(dstring)
    print('result is :' , c*d)
def devide(): # the devide function
    estring = input ('enter value :')
    e = int(estring)
    fstring = input('enter value :')
    f = int(fstring)
    print('result is :' , e/f)
def rootover():
    out = input('entervalue :')
    x = int(out)
    print(math.sqrt(x))

# end of function
# start of coding
print("input choice(1/2/3/4)")
print("1 = add")
print("2 = minus")
print("3 = into")
print("4 = devide")
print("5 = rootover")

choice = input('enter choice:')
if choice is '1':
    print(add())
elif choice is '2':
    print(minus())
elif choice is '3':
    print(into())
elif choice is '4':
    print(devide())
elif choice is '5':
    print(rootover())
else:
    print("invalid option , exiting")
#end of coding
exit()