#Sum of N positive numbers.
N = int(input("Enter a number: "))
sum = 0
for i in range(N):
    sum = (N*(N+1))/2
print('sum: ',sum)