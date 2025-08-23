print("Prime Number:")
class Prime:
    def is_prime(self, n):
        count=0
        i=1
        while(i*i<=n):
            if n%i==0:
                count+=1
                if n//i !=i:
                    count+=1
            i+=1
        if count==2:
            return "prime"
        else:
            return "not prime"
n=int(input("Enter a number:"))
obj=Prime()
print(obj.is_prime(n))   


print("Armstrong Number:")
class Armstrong:
    def is_armstrong(self, n):
        dup=n
        sum=0
        while(n>0):
            last_digit=n%10
            sum=sum+(last_digit**3)
            n=n//10
        if(dup == sum):
            return "Armstrong"
        else:
            return "Not"
num=int(input("Enter a number:"))
obj=Armstrong()
print(obj.is_armstrong(num))   

print("all divisors of a number:")
class divisors:
    def all_divisors(self, x):
        divisors_list=[]
        for i in range(1,x+1):
            if x%i==0:
                divisors_list.append(i)
            return divisors_list    
num=int(input("enter a number:"))
obj=divisors()
print(obj.all_divisors(num))        
