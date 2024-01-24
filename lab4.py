# Lab 1,2 - complete
# Lab 3: 

my_details = ['ori','40','ori@email.com','05412345678']
print(f'\nThese are my details:\n####################\n')
print(f'My name is: {my_details[0].title()}.\nMy age is:{my_details[1]}\nMy Email Address is:{my_details[2].title()}\nMy Phone number is:{my_details[3]}\n')

ips = ['10.0.0.0','172.16.0.0' ,'192.168.0.0']
ips.append('1.1.1.1')
ips.append('1.1.1.2')
ips.append('1.1.1.3')
ips.pop(2)
print (ips)