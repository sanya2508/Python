#docstrings
def test(a):
  '''
  Info: it will test something
  '''
  print(a)

test('!!!!')
help(test)


# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions


#*args and **kwargs

#map
#filter
#zip
#reduce


#comprehension- list, set, dictionary

#list_comprehension
my_list= [char for char in 'hello']
my_list2= [num for num in range(0,100)]
my_list3= [num*2 for num in range(0,100)]
my_list4= [num**2 for num in range(0,100) if num%2==0]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

#set comprehension
my_list= {char for char in 'hello'}
my_list2= {num for num in range(0,100)}
my_list3= {num*2 for num in range(0,100)}
my_list4= {num**2 for num in range(0,100) if num%2==0}
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

#dictionary comprehension
simple_dict= {
  'a':1,
  'b':2
  }

my_dict ={key:value*2 for key,value in simple_dict.items()}
print(my_dict)


#duplicates using character comprehension
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1])) #set to print the char once
print(duplicates)
