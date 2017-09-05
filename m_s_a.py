#Multiples.
#1. Write code that prints all the odd numbers from 1-1000 using for loop.
#2. Create another program that prints all multiples of 5 from 5-1000000.
#1:
for num in range(1,1000):
    if(num%2==1):
        print(num)
#2:
for num in range(5,1000000):
    if(num%5==0):
        print(num)

#tThe list for the bottom two assignments.
a = [1,2,5,10,255,3]

#Sum List.
#Sum of all values in list.
def my_sum(my_list):
    the_sum = 0
    for el in my_list:
        the_sum += el
    return the_sum
print(my_sum(a))

#Average List.
#Average of all values in list.
a_avg = my_sum(a) / len(a)
print(a_avg)
