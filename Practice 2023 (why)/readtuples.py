f = open(r'C:\Users\Jrytoeku Qtuhtc\Downloads\shepetkova.txt',
         'r', encoding='utf-8')

text = f.read()
data = []
exec('data = ' + text)
print(data)
