#How to find average of N numbers in Python
N = int(input("Enter a number: "))
sum = 0
for i in range(N):
    num = float(input("Enter any numbers: "))
    sum += i
avg = sum/N
print('Average: ',avg)