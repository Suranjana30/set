Items = [23,46]
Items.append(45)#Insert any item
print(Items)
Items.pop()#Delete any item
print(Items)
Items1=[32,78]
Items=Items+Items1
print(Items)
print(Items1[0])
print(len(Items))#return number of items in the list
print(max(Items))#return maximum element in the list
print(min(Items))#return minimum element in the list
print(sum(Items))#return sum of all elements in the list
print(sorted(Items))#return sorted list,list remains unchanged
Items.reverse()#used for reversing list
print(Items)