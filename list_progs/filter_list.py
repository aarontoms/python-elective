l = []

print("\nEnter numbers to add to list and Enter blank to stop")
while True:
    try:
        num = int(input(">>> "))
    except:
        break
    l.append(num)
    
max_num = int(input("Enter the max number: "))
new_list = list(filter(lambda x: x < max_num, l))
print("\nOriginal List:", l)
print("\nNew List:", new_list)