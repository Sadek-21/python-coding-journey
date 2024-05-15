name = ''
while name != 'Mohamed':
    print('Pleas type your name.')
    name = input()
print('Thank you')



while True:
    print('Please type your name.')
    name = input()
    if name == 'Mohamed':
        break
print('Thank you!')


#while True:
#    print('Hello world!')




while True:
    print('Who are you ?')
    name = input()
    if name != 'Joe':
          continue
    print('Hello, Joe.what is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')



print('My name is')

for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


total = 0
for num in range(101):
    tital  = total + num
print(total)
