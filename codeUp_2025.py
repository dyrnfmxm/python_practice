def str_sort(s):
    new_string = []

    for i in s:
        new_string.append(i)

    new_string.sort()

    return new_string


y, m, d = input().split('/')

md = m+d

#print(y, md)

sort_y = str_sort(y)
sort_md = str_sort(md)

#print(sort_y, sort_md)
if sort_y == sort_md:
    print("yes")
else:
    print("no")
