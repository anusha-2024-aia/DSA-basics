print("count of digiits using last digit method:")
def count_digits(n):
    count = 0
    while (n>0):
        last_digit=n%10
        n=n//10
        count+=1
    return count
n=int(input("Enter a number:"))
print(count_digits(n))    


print("Using the same method to reverse number:")
def reverse_number(n):
    rev=0
    while (n>0):
        last_digit=n%10
        rev_number=rev*10+last_digit
        n=n//10
        return rev_number
n=int(input("Enter a number:"))
print(reverse_number(n))

print("Palindrome:")
def is_palindrome(n):
    dup=n
    rev=0
    while(n>0):
        last_digit=n%10
        rev_number=rev*10+last_digit
        n=n//10
        if(dup==rev_number):
            return True
        else:
            return False
n=int(input("enter a number:"))
print(is_palindrome(n))        
        
