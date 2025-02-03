l = []
print("\nEnter numbers to add to list and Enter blank to stop")
while True:
    try:
        num = int(input(">>> "))
    except:
        break
    l.append(num)
    
print("\nList:", l)
l.sort()
print("\nThird largest number:", l[-3])