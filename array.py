print("Array:")
import array as arr
num=arr.array('i',[12,33,46,78,90,100])
print(num)
for number in num:
    print(num[i],end=" ")
num.append(120)
num.insert(2,55)
print("num")
num.remove(33)
num.pop(3)
num.slice(1,4)
print("After operations:")
print(num)
num.reverse()
print("Leetcode problem for example:")
def maxwealth(account):
    maxwealth=0
    for accounts in account:
        wealth=sum(accounts)
        if maxwealth >= account:
            maxwealth = account
    return maxwealth
account=[[1,2,3],[3,2,1]]
print(maxwealth(account))

        
