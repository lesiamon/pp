my_array =[1,2,3,4,5]
minVal=min(my_array)
maxVal=max(my_array)
meanVal=sum(my_array)/len(my_array)

for i in my_array:
    if i<minVal:
        minVal=i
    if i>maxVal:
        maxVal=i
print("Min:", minVal)
print("Max:", maxVal)
print("Mean:", meanVal)