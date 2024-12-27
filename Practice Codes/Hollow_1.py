# Write a program to print inverted hollow triangle.
def Hollow_triangle(n):
    num = 1 #count
    for i in range(n):
        pattern = ""
        for j in range(n-i):#Based on i columns will decrease
            if i ==0:
                pattern += str(num) + " "
                num += 1#increment count
            else:
                if j==0 or j == n-i-1:
                    pattern += str(num) + " "
                    num += 1
                else:
                    pattern += "  "
        print(pattern)
n = int(input("Enter a number: "))
Hollow_triangle(n)

