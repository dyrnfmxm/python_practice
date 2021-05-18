text = input()
text = text+","

text = text.replace('  ', '')
text = text.replace(',',' ')
text = text.replace('  ',' ')
text = text.replace(';',' \n')

print(text)
