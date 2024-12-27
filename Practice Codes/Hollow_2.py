# Write a program to print inverted Right-Angled Triangle.
def Inverted_Triangle(s,n):
    for i in range(n):
        pattern = "  " * i
        for j in range(n-i):
            if i == 0:
                pattern += str(s) + " "
                s += 1
            else:
                if j == 0 or j == n - i -1:
                    pattern += str(s) + " "
                    s += 1
                else:
                    pattern += "  "

        print(pattern.rstrip())
s = int(input("Enter a number: "))
n = int(input("Enter a number: "))
Inverted_Triangle(s,n)