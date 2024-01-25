# Lab 1,2 - complete
# Lab 3: 
from time import sleep
from random import randint



my_details = ['ori','40','ori@email.com','05412345678']
print(f'\nThese are my details:\n####################\n')
print(f'My name is: {my_details[0].title()}.\nMy age is:{my_details[1]}\nMy Email Address is:{my_details[2].title()}\nMy Phone number is:{my_details[3]}\n')

ips = ['10.0.0.0','172.16.0.0' ,'192.168.0.0']
ips.append('1.1.1.1')
ips.append('1.1.1.2')
ips.append('1.1.1.3')
ips.pop(2)
print (ips)

# Lab 5:

bank = {'idan':30000, 'yossi':25000, 'ori':12}
sum =  (bank['idan'] + bank['ori'])
bank['yair'] = sum
print(len(bank.items()))
if 'idan' in bank:
    print('idan is here')

#Lab 6:

def raise_by_power():
    return()
def ip_list():
    return()
def dict_dns():
    return()
def check_palindrome():
    return()

def menu ():
    message = (f'\nMenue:\n#########\n\n')
    message += (f'1) Enter a number to raise by power of 3.\n')
    message += (f'2) Insert IPs to a list.\n')
    message += (f'3) Insert DNS to a dictionary.\n')
    message += (f'4) Check Palindrome\n')
    message += (f'\n To quit press `q`:\n')
    pick = 0
    while pick != 'q':
        pick = input(message)
        if pick == 1:
            raise_by_power()
        elif pick == 2:
            ip_list()
        elif pick == 3:
            dict_dns()
        elif pick == 4:
            check_palindrome()
        

menu()





