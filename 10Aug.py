'''collection:- collection is a collection of object type element.
we have two type of collection:-
1. Similar type collection.
	ex. Array
2. Different type collection.
	ex. 
	List
	dict
	Set
	tuples
List:- 
-> List is a dynamic 
-> List is a Mutable
-> List store data on index.
-> List is a collection of object type elements
-> List is ordered or sequential.
-> List denoted by Square bracket [].
-> List ke ander complex data type nhi store kr skte.
 	k=[1,20,'muzim','a', 90.5, True]
	print(k) // 
output [1,20,"muzim",'a', 90.5, True]
	k.remove('muzim')
	print(k) //
output [1,20,'a', 90.5, True]
pop->depend on LIFO
	k.pop(index Number)
	k.pop(1)
	print(k) //
output [1,'muzim','a'.90.5,True]
	k.append('Ducat') // add on last
output [1,20,'muzim','a', 90.5, True, 'Ducat']
	
	k.insert(3,'ali') //
output [1,20,'muzim','ali','a', 90.5, True, 'Ducat']

	k.clear() //
clear sai empty List rhjati hai data clear ho jata hai

	k.reverse()
reverse list using reverse in build function
			or
print(k[ : :-1]) // reverse list using slicing

assignment;
write a program to remove duplicate element in list.
l=[1,2,3,2,4,6,1,5,4]
k=[]
for item in l:
    if item not in k:
        k.append(item)
print(k)
write a program findout grater than 6 char. '''
# write a program to findout prime number in list.

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
k=[]
for i in l:
    if i ==2 or i ==3 or i ==5 or i ==7 or i ==11:
        print("Prime number",i)
    elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0 or i == 1 :
    else:
        print("Prime number")
    print(l)        

	
 

    

		