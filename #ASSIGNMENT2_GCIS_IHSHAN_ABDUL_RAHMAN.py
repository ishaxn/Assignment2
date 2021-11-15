import array as Array
import csv
with open('assignment2_file.csv','r') as csv:
    cont=csv.reader(csv)
    contlist=[]
    for i in cont:
        contlist.append(i)
    tuple_new_data=[]
    for i in contlist[1]:
        if i!="":
            tuple_new_data.append(int(i))
        else:
            pass
    arraynewdata=list(map(int,contlist[0]))
    tuplenewdata=list(map(int,tuple_new_data))
    array1=Array.array('i',arraynewdata)
    tuple1=tuple(tuplenewdata)
    list1=contlist[2]
    set1=set(contlist[3])
    dict1=dict(zip(contlist[4],contlist[5]))


print(array1,'\n',tuple1,'\n',list1,'\n',set1,'\n',dict1)

with open('assignment2_file.txt','w') as file1:
    data=str(dict1)+'\n'+str(list1)+'\n'+str(tuple1)+'\n'+str(array1)
    file1.write(data)

print("\n")

cont=[]

with open('assignment2_file.txt','r') as file2:
    for line in file2:
        cont.append(line.rstrip())
for i in cont:
    print(i)

print("\n")

if 'Fujairah' in list1 and 'brown' in set1 and 'Data Science' in dict1:
    print("Yes, Found them!!\n 'Fujairah' in list1,\n 'brown' in set1 and \n 'Data Science' in dict1")
else:
    print("None")

print("\n")

#Question 2

for i in range(0,len(array1)):
    temp=array1[i]
    j=i-1
    while j>=0 and temp<array1[j]:
        array1[j+1],array1[j]=array1[j],array1[j+1]
        j=j-1

#merge sorting using the function's for tuple1

def merge_sort(array):
    if len(array)<=1:
        return array
    midpoint=len(array)//2
    left,right=merge_sort(array[:midpoint]),merge_sort(array[midpoint:])
    return merge(left,right)
def merge(left,right):
    result=[]
    left_pointer=right_pointer=0
    while left_pointer< len(left) and right_pointer<len(right):
        if left[left_pointer]<right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer +=1
        else:
            result.append(right[right_pointer])
            right_pointer+=1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

ltuple1=list(tuple1)
resultuple1=merge_sort(ltuple1)
tuple1=tuple(resultuple1)

#Quick Sorting for list1

def quick_sort(sequence):
    length = len(sequence)
    if length < 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item >pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

quick_sort(list1)

#Quick sorting for set1

quick_sort(set1)

'''sorting by value done for dict1'''

ndict1={}
for i in sorted(dict1):
    temp=dict1[i]
    ndict1[i]=temp
dict1=ndict1

with open('assignment2_file.txt','w') as file3:
    data=str(array1)+'\n'+str(tuple1)+'\n'+str(list1)+'\n'+str(set1)+'\n'+str(dict1)
    file3.write(data)
cont=[]
with open('assignment2_file.txt','r') as file4:
    for line in file4:
        cont.append(line.rstrip())

for i in cont:
    print(i)

print("\n")

with open('assignment2_file2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for i in cont:
        temp=[]
        temp.append(i)
        writer.writerow(temp)


