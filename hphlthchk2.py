#!/usr/bin/python3
from netmiko import ConnectHandler
import sys
import getpass
import string
import time
import os
import select
import paramiko
import re

print('\n')
ip = input("IP Address: ")
print('\n')
username = input("Username: ")
password = getpass.getpass()
print('\n')
ticket = input("Enter Ticket#: ")
print('\n')

hp_comware = {'device_type': 'hp_comware',
              'ip': ip,
              'username': username,
              'password': password,
              'port': 22,
              'verbose': False}
connection = ConnectHandler(**hp_comware)
print(connection)
print(type(connection))
print('\n')

evidence_path = os.path.dirname(os.path.realpath(username))
if not os.path.exists(username):
    os.makedirs(username)
if not os.path.exists(os.path.join(username, ticket)):
    os.makedirs(os.path.join(username, ticket))


print('\n#### HP Access-Switch Health Check ####\n')
print(ticket)
print('\n')
print(username)

print('\n#### Device hostname ####\n')
hostname = connection.find_prompt()
print(hostname[:-1])
print('\n')

print('\n#### Display Time ####\n')
show_clock = connection.send_command('display clock')
print(show_clock)

print('\n#### Display logbuffer data ####\n')
show_logbuffer = connection.send_command('display logbuffer')
print(show_logbuffer)

print('\n#### Display information center data ####\n')
show_infocenter = connection.send_command('display info-center')
print(show_infocenter)

print('\n#### Display Manufacture information ####\n')
show_manuinfo = connection.send_command('display device manuinfo')
print(show_manuinfo)

print('\n#### Display inbound traffic counters ####\n')
show_incounters = connection.send_command('display counters inbound interface')
print(show_incounters)

print('\n#### Display outbound traffic counters ####\n')
show_outcounters = connection.send_command('display count out int')
print(show_outcounters)

print('\n#### Display interface packet drops ####\n')
show_packdrops = connection.send_command("display int | in drop")
print(show_packdrops)

print('\n#### Display memory information ####\n')
show_memory = connection.send_command('display memory')
print(show_memory)

print('\n#### Display cpu usage information ####\n')
show_cpu = connection.send_command('display cpu-usage')
print(show_cpu)

print('\n#### Display cpu usage history information ####\n')
show_cpuhist = connection.send_command('display cpu-usage history')
print(show_cpuhist)

print('\n#### Display inbound traffic rate counters ####\n')
show_inrate = connection.send_command('display count rate in int')
print(show_inrate)

print('\n#### Display outbound traffic rate counters ####\n')
show_outrate = connection.send_command('display count rate out int')
print(show_outrate)

print('\n#### Display traffic behavior data ####\n')
show_bhdefined = connection.send_command('dis traffic behavior user-defined')
print(show_bhdefined)

print('\n#### Display traffic classifier data ####\n')
show_cldefined = connection.send_command('dis traffic classifier user-defined')
print(show_cldefined)

print('\n#### Clock status and configuration information ####\n')
show_clock = connection.send_command('display clock')
print(show_clock)

with open(os.path.join(evidence_path, username, ticket, hostname + "-hlthchk.txt"), 'w') as f:
    f.write('\r'.join('#### HP Access-Switch Health Check ####\n\n\n\n'))
    f.write('\r'.join('#### Device hostname ####\n\n\n\n'))
    f.write('\r'.join(hostname + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display Time ####\n\n'))
    f.write('\r'.join(show_clock + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display logbuffer data ####\n\n'))
    f.write('\r'.join(show_logbuffer + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display information center data ####\n\n'))
    f.write('\r'.join(show_infocenter + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display Manufacture information ####\n\n'))
    f.write('\r'.join(show_manuinfo + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display inbound traffic counters ####\n\n'))
    f.write('\r'.join(show_incounters + '\n\n\n\n\n'))
    f.close()
