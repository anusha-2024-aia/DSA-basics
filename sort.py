print("sorting a list:")
list=[6,7,10,11.4,1,2]
list.sort()
print(list)

print("Sorting  a tuple:")
Tuple=(10,100,22,78,65,33)
print(sorted(Tuple))

print("Sorting a string:")
String="Anusha"
print(sorted(String))

print("Sorting a dictionary:")
my_dict={345:"anu",232:"praveen"}
print(sorted(my_dict))

print("Ascending and Descending:")
my_list=[12,23,90,78,100,105]
my_list.sort()
print(f"Ascending of my_list:f{my_list}")
my_list.sort(reverse=True)
print(f"descending of my_list:f{my_list}")

print("Lambda function:")
# List of tuples
a = [(1, 'one'), (3, 'three'), (2, 'two')]

# Sorting by the second element of each tuple
sa = sorted(a, key=lambda x: x[1])
print("Sorted by second element:", sa)

print("User defined Sorting:")
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def myfun(p):
    return p.x

l=[point(1,3),point(4,5),point(6,9)]
l.sort(key=myfun)
for i in l:
    print(i.x,i.y)
     

print("Tuple sorted using for loop:")
tuple=[(2,3),(8,9),(7,10)]
tuple.sort()
for i in tuple:
    print(i[0],i[1])

