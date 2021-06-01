import socket
from IPy import IP
from pyfiglet import Figlet


f = Figlet(font='standard')

print(f.renderText(': PORTSCANNER :'))

option = input("Please choose your option : \n [-_0] 0 For Single Target \n [0_-] 1 For Multiple Targets \n \n Enter your Option  :")
    

def scan(target):
    checked_ip = check_ip(target)

    print('\n [(0_0)] Scanning Target '+ str(target))
        
    for port in range(j,k):
        scan_ports(checked_ip, port)
 

def check_ip(ip):                  
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_ports(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)       #Change the time if you want results fast but less_time = less_accuracy  
        sock.connect((ipaddress, port)) 
        print('\n [+] Port %d is open '%port)
    except:
        pass


if option=='0':
    
    target2 = input('[+] Enter target to scan  : ')
    print("Enter Range")
    while True:
        try:
            j = int(input('\n[+] From port no. (enter 0 if nothing):'))
            k = int(input('\n[+] To port no.  (enter 100 if nothing):'))
            break
        except ValueError as e:
            print("\n \t Error %s Range is Missing You Dumaas . Try Again  |-__-| "%e)
    scan(target2)


elif option=='1':

    targets = input('[+] Enter targets to scan( Seperate them by , )  : ')        
    while True:
        try:
            j = int(input('\n[+] From port no. (enter 0 if nothing):'))
            k = int(input('\n[+] To port no.  (enter 100 if nothing):'))
            break
        except ValueError as e:
            print("\n \t Error %s Range is Missing You Dumaas . Try Again  |-__-| "%e)

    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))




