birthdays = {'Alice' : 'Apr 1' , 'Bob' : 'Dec 12' , 'Carol' : 'Mar 4'}

while True:
    print('Entre a name : (blank to quit)')
    name = input()
    if name == '':
        break


    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
                print('I do not have birthday information for ' + name)
                print('What is their birthday?')
                bday = input()
                birthdays[name] = bday
                print('Birthday database updated.')


for v in birthdays.values():
    print(v)
    
for i in birthdays.items():
    print(i)
    
    
spam = {'color' : 'red' , 'age' : 42}

for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))


spam1 = {'name': 'Pooka', 'age': 5}
spam1.setdefault('color', 'black')