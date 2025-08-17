print(789 % 100)
divmod(42, 10)

# Operator Overloading
greeting = "Hi "
audience = "class"
print (greeting + audience)

# Multiplying text with a whole number also works.

print(10 * greeting)

# Objects vs. Types vs. Values
a = 42
b = 42.0
c = "Python rocks"
#Identity / "Memory Location"
print(id(a))
#These addresses are not meaningful for anything other than checking if two variables reference the same object.

#Obviously, a and b have the same value as revealed by the equality operator ==: We say a and b "evaluate equal." The resulting True - and the False further below - is yet another data type, a so-called boolean. We look into them in Chapter 3 .

#(Data) Type / "Behavior"

print(type(a))
print(b.is_integer())







