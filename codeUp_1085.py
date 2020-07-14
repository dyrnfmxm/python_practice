h, b, c, s = map(int,input().split())
result_bit = h*b*c*s
result_byte = result_bit/8
result_mb = result_byte/1024
result_kb = result_mb/1024
print(round(result_kb,1),"MB")
