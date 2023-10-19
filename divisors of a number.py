number = int(input("Enter an integer: "))
divisors = []
for i in range(1, number+1):
    if number % i == 0:
        divisors.append(i)
print(f"Number of divisors is: {len(divisors)}")
print(f"The divisors of {number} are: {divisors}")

