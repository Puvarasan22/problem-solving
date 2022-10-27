#finding missing numbers from 1 to 100
integer=[14,5,6,78,9,2,3]
miss_int=[]
for i in range(1,101):
    if i not in integer:
        miss_int.append(i)
print("missing numbers are",miss_int)

#finding duplicate numbers from a array
dup_ele=[1,2,3,4,1,2]
print("duplicate numbers are")
for i in range(0,len(dup_ele)):
    for j in range(i+1,len(dup_ele)):
        if(dup_ele[i]==dup_ele[j]):
            print(dup_ele[j],end=" ")

#how do yo find largest number in a unsorted list
flag=0
large_array=[1,2000,400,20]
large_array.sort()
print("Smallest number",large_array[0])
print("Largest number",large_array[-1])



#how do you find all pair of integers whose sum is equal to given number

pair_array=100
def my_sum(s):
    print("all pair of integers are")
    for i in range(0,pair_array):
        for j in range(i,pair_array):
            for k in range(i,pair_array):
                if i+j+k==s:
                    print([i,j,k],end=" ")
                
sum=int(input("Enter number for finding pair of numbers"))                
my_sum(sum)


#remove duplicate elements
given_array=[10,20,10,30,20]
print("before removal of duplicate",given_array)
remove_duplicate=[]
for i in given_array:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
print("After removal of duplicate",remove_duplicate)


#removing duplicates in string

a"he is so cute"
alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
non_repeat=[each for each alph in a if each not in alph]
print(non_repeat)







































