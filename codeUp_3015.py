n, m = map(int,input().split())
student_list = []
score_list = []
name_list = []

for i in range(n):
    name, score = input().split()
    
    student_list.append((name, score))
    score_list.append(int(score))

score_list.sort(reverse = True)

#print(score_list)

for i in range(m):
    for j in student_list:
        #print(j[0], j[1])
        #print(score_list[i])
        if score_list[i] == int(j[1]):
            if j[0] in name_list:
                continue
            else:
                name_list.append(j[0])
                break


#print(student_list)
for i in name_list:
    print(i)
