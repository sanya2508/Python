#String concatenation
#works only with string
print('hello ' + 'sanya')

#converted int to string
print(type(str(100)))

#Escape sequence \
#whatever comes after \ it will assume that to be a string
weather=('It\'s "kind of" sunny')
print(weather)

#\t adds a tab spacing
#\n adds a new line

#formatted strings: f or dot format
print("Hello {}, your balance is {}.".format("Cindy", 50))
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))
name = 'Ci'
amount = 50
print(f"Hello {name}, your balance is {amount}.")

#string indexes
#[start:stop:stepover]  //stepover is optional
#negative index means start from end
python = 'I am PYHTON'
print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1]) #reverse the order

#strings in python are immutable(cant reassign part of a string)

print(len('hellooooo'))

#built in functions and methods

#booleans TRUE or FALSE



