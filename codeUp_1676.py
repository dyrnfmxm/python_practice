n = int(input())
company_list = []

for i in range(n):
    company_list.append(int(input()))

#print(company_list)

sales_rank = sorted(company_list, reverse=True)

#print(company_list, sales_rank)

for i in company_list:
    print(sales_rank.index(i)+1)
