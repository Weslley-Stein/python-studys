# Lists
Lists are a data structure which allows you to store multiples pieces of data of multiples types, a list its enumerated by Index, which means
the first element its represented by "0" and then go on
```py
#Creating a List
my_list = ["Weslley", "Zeno", "Sett"]
print(my_list)
#Expected output: Weslley, Zeno, Sett

#Take a specific element of a list
print(my_list[index_of_the_element]) 

#Periods with lists
print(my_list[1:])#That will take every element after the element of index 1(including himself)
print(my_list[:1]#That will take every elements which came before the element of index 1(including himself)
print(my_list[0:1])#Thats its a period, from index 0 until index 1 will be taked every element(including both of them)

#Changing a value of an element of the list
my_list[0] = "Yellsew"
Print(my_list[0])
#Expected Output: Yellsew 
```

### built-in Functions
- list1.extends(list2): will append the second list inside of the first one 
- list.append(element): will append a new element at the end of the list 
- list.insert(index,element): will append an element on the specified index
- list.remove(element): will remove the specified element 
- list.clear(): will remove every element of the list 
- list.pop(): will remove the last element of the list 
- list.index(element): will show you the index of the specified element
- list.count(element): will show you the number of occurences of this element on a list
- list.sort(): will sort the elements of list by alphanumerical order
- list.reverse(): will revert the sort of elements inside the list
- list.copy(): will copy a list, you can put it inside a variable 


