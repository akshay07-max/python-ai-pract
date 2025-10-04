print("My first program...")

a = 10
b = 200

print("Total", a*b)

# continuation character \

name = "Raju"

string = "Hello {} \
    Welcome to \
        the party.\
            from to".format(name)

print(string)

# writing a longer mathematical expression.
a1 = 10
a2 = 30
a3 = 12
a4 = 30

expr = (a1+a2) * (a3+a4) / \
(a1-a2) * (a3-a4)

print("Expr == ", expr)

# in python we are use semicolon for assigning multiple values in a single line.

a5 = 20; a6 = 50; a7 = 30

checkAdd = id(a5)
print(checkAdd)