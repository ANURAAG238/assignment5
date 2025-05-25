list_1=[]
for i in range(1,11):
    list_1.append(i)
print("Original list: ",list_1)
list_2 = list_1[0:5]
print("Extracted first five elements: ",list_2)
list_2.reverse()
print("Reversed extracted elements: ",list_2)