l = []
print("\nEnter numbers to add to list and Enter blank to stop")
while True:
    try:
        num = int(input(">>> "))
    except:
        break
    l.append(num)
    

print("\nList:", l)
print("\nLargest number:", max(l))
print("Smallest number:", min(l))