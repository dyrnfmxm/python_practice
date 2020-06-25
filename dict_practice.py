b = {'name':'John',
     'phone':'01012345432',
     'email':'test@test.com',
     'birth':'11111'}
print(b)
print(b['name'])
b['birth'] = 101010
print(b['birth'])
b['city'] = 'Seoul'
print(b['city'])
del b['email']
print(b)
