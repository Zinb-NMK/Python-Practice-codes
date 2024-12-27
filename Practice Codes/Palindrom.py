'''def check_palindrome(w1,w2):
    modified_word = w1[::-1]
    if(modified_word == w2):
        print("palindrome")
    else:
        print("not palindrome")
w1 = "LAPTOP"
W2 = "TOPLAP"
check_palindrome(w1,W2)'''

def print_quadratic_root(a,b,c):
    dis = (b*b) - (4 * a * c)
    if(dis > 0):
        print("Roots are Real and unequal")
    elif(dis == 0):
        print("Roots are equal")
    else:
        print("Not equal")
p=1
q=-5
r=6
print_quadratic_root(a=p,b=q,c=r)