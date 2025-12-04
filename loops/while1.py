#Prime Numbers

n = int(input("Enter a number: "))
i = 2
is_prime = True

if n <= 1:
    is_prime = False
else:
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")