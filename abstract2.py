#lists: much like array
#lists are immutable unlike strings
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)


#matrix: a way to describe 2D list
# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
# access "Oranges" and print it.

#ADDING
#append: changes the list inplace
#insert: modifies the list inplace
#extend: are lists and modifies the other list inplace

#REMOVING
#.pop()
#.remove() inplace
#.clear() removes completely whatever is in the list
#.index(x) gives index of x
# in: true / False
#.count('x') count no of times x exist
#.sort() sorts the list inplace
#sorted() produces a new sorted array
#.copy() coppies the list
#.reverse() reverses the list
print(list(range(1,100)))

#.join()
sen= '!!'.join(['hi', 'my', 'name', 'is' ,'sanya'])
print(sen)

#list unpacking

