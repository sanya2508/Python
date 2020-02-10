#if condition:
 # statement
  #elif condition:
   # statement
    #else:
     # (statement)

#ternary operator
#condition_if_true if condition else condition_is_false

#short circuiting: using or

#difference between is and ==

for item in ('sanya'):
  print(item)
  #iterable: can be list,string,tuple,dictionary,set


user={
    'name': 'Sanya',
    'age':'20'
  }

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for k,v in user.items():
  print(k,v)


  #Range: range creates a special kind of object that we can iterate over

  for int in range(0, 100, 2):
    print(int)

for int in range(2):
    print(list(range(10)))


#enumerate to access index number
for i,char in enumerate('saanyyyaaa'):
    print(i,char)


#while loop
continue
break
pass


