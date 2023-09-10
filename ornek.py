numbers = [1,2,3,4,5,6,7,8,9]
numbers = [x for x in range(1,11) if x %2==0]
print(numbers)

list = [number * number for number in numbers]
print(list)

list1 = [number for number in numbers if number %2 ==0]
print(list1)

list2 = [number * number for number in numbers if number %2 ==0 ]
print(list2)

list3 =[number * number for number in numbers if number > 4 and number %2==0 ]
print(list3)

numbers =[1,2,3,4]
letters = "abcd"
list4 = [(number,letter)for number in numbers for letter in letters]
print(list4)

list1=[1,2,3,4,5,6,7,8,9]
list2=[2,3,6,9,5]
list5 = [i * i for i in list1 if not i in list2]
print(list5)

list_ = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
list6=[j for i in list_ for j in i]
print(list6)

liste = [method for method in dir(list) if not method.startswith("__")]
print(liste)


