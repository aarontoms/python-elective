def estimate_sqrt(n):
    estimate = n / 2.0
    precision = 0.0000001
    while True:
        final = (estimate + n / estimate) / 2.0
        if abs(estimate - final) < precision:
            return final
        estimate = final

while True:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Enter a positive number")
    else:
        print("Square root of", num, "is", estimate_sqrt(num))
        break
