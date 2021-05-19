month, day = map(int,input().split())

day_count = 30-day
month_count = 10-month

month_count = ((month_count//2)+(month_count%2))*31 + (month_count//2)*30

total_count = month_count + day_count

print(total_count)
