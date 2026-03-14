num = int(input("Entr number: "))
sum = 0
prod = 1

while num > 0:
    digit = num % 10
    sum += digit
    prod *= digit
    num //= 10

if sum == prod:
    print("Spy number")
else:
    print("Not spy number")