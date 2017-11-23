import socket
import os

print(''' ##############           IP Finder & Traceroute           ##############
                  #                                            #
                  #           Script Vesion: 1.0.0             #
                  #                                            #
                  #           Designed by @miador              #
                  #                                            #
     ########################################################################### ''')


a = input("Please enter a website:")



print("IP address of the website that you entered:",socket.gethostbyname(a))

print("-" * 60)

ping = input("Do you want to ping founded ip address? (y/n):")

if ping == 'y':
    os.system("ping -c 5 " + socket.gethostbyname(a))
    print("-" *56)
    reply= input("Do you want to traceroute? (y/n): ")
    print("-"*56)
    if reply == 'y':
        print("UDP Traceroute results:")
        os.system("traceroute " + socket.gethostbyname(a))
        print("TCP Traceroute results:")   #If you want to TcpTraceroute, you must become superuser in your OS.
        os.system("tcptraceroute " + socket.gethostbyname(a))
elif ping == 'n':
    print("Good Luck! ;)")

else:
    print("Please enter a valid value!")

