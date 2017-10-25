print ('Please enter your name.')
name = input()
print ('Please enter your age.')
age = input()
if name == 'Alice':
    print('Hi, Alice')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
