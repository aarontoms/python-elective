l1 = []
l2 = []

print("\nEnter numbers to add to list and Enter blank to stop")
print("List 1:")
while True:
    try:
        num = int(input(">>> "))
    except:
        break
    l1.append(num)
    
print("\nList 2:")
while True:
    try:
        num = int(input(">>> "))
    except:
        break
    l2.append(num)
    
new_list = []
for i in l1:
    if i in l2 and i not in new_list:
        new_list.append(i)

print("\nList 1:", l1)
print("List 2:", l2)
print("\nCommon Elements:", new_list)