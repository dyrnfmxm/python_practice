w, h, b = map(int,input().split())
result_bit = w*h*b
result_byte = result_bit/8
result_mb = result_byte/1024
result_kb = result_mb/1024
print('%.2f'%result_kb,"MB")
