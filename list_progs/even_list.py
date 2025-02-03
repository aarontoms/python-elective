l = []

print("\nEnter numbers to add to list and Enter blank to stop")
while True:
    try:
        num = int(input(">>> "))
    except:
        break
    l.append(num)
    
new_list = list(filter(lambda x: x % 2 == 0, l))
new_list.sort()
print("\nOriginal List:", l)
print("\nEven and Sorted List:", new_list)