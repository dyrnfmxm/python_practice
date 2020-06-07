burger = 2000
drink = 2000
for i in range(3):
    n = int(input())
    burger = min(n,burger)
for i in range(2):
    n = int(input())
    drink = min(n,drink)
    
print(burger+drink-50)
