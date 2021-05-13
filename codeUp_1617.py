n = input()

def reverse_number(number):
    reverse_num = number[::-1]
    return reverse_num

reverse_num = reverse_number(n)

password = int(n) + int(reverse_num)

password = str(password)

reverse_password = reverse_number(password)

if password == reverse_password:
    print("YES")
else:
    print("NO")
