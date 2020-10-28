attempt = 1
password = input('Please enter your Password : ')
while password != 'yourpassword' and attempt <= 2 :
    password = input('WRONG PASSWORD ! Please enter correct Password : ')
    attempt += 1
if password != 'yourpassword' :
    print('Too Many Failed Attempts !')
if password == 'yourpassword' :
    print('CORRECT PASSWORD')
