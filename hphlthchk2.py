#!/usr/bin/python3
from netmiko import ConnectHandler
import sys
import getpass
import string
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('\n')
ip = input("IP Address: \b" )
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
print('\n#### Incident\Task#: ####\n')
print(ticket)
print('\n#### User ID: ####\n')
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
time.sleep(2)
print(show_logbuffer)

print('\n#### Display logbuffer data ####\n')
show_neigh = connection.send_command('display lldp neighbor list')
print(show_neigh)

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

with open(os.path.join(username, ticket, hostname + "-hlthchk.txt"), 'w') as f:
    f.write('\r'.join('#### HP Access-Switch Health Check ####\n\n\n\n'))
    f.write('\r'.join('#### Incident\Task#: ####\n\n'))
    f.write('\r'.join(ticket + '\n\n'))
    f.write('\r'.join('#### User ID: ####: \n\n'))
    f.write('\r'.join(username + '\n\n'))
    f.write('\r'.join('#### Device hostname ####\n\n\n\n'))
    f.write('\r'.join(hostname + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display Time ####\n\n'))
    f.write('\r'.join(show_clock + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display logbuffer data ####\n\n'))
    f.write('\r'.join(show_logbuffer + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display neighbor data ####\n\n'))
    f.write('\r'.join(show_neigh + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display information center data ####\n\n'))
    f.write('\r'.join(show_infocenter + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display Manufacture information ####\n\n'))
    f.write('\r'.join(show_manuinfo + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display inbound traffic counters ####\n\n'))
    f.write('\r'.join(show_incounters + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display outbound traffic counters ####\n\n'))
    f.write('\r'.join(show_outcounters + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display interface packet drops ####\n\n'))
    f.write('\r'.join(show_packdrops + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display memory information ####\n\n'))
    f.write('\r'.join(show_memory + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display cpu usage information ####\n\n'))
    f.write('\r'.join(show_cpu + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display cpu usage history information ####\n\n'))
    f.write('\r'.join(show_cpuhist + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display inbound traffic rate counters ####\n\n'))
    f.write('\r'.join(show_inrate + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display outbound traffic rate counters ####\n\n'))
    f.write('\r'.join(show_outrate + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display traffic behavior data ####\n\n'))
    f.write('\r'.join(show_bhdefined + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display traffic classifier data ####\n\n'))
    f.write('\r'.join(show_cldefined + '\n\n\n\n\n'))
    f.write('\r'.join('#### Display Time ####\n\n'))
    f.write('\r'.join(show_clock + '\n\n\n\n\n'))
    f.write('\r'.join('#### END ####\n\n'))
    exit()


sender = ((username))@aa.com
receivers = ((username))@aa.com

msg = MIMEMultipart()
msg['Subject'] = 'Test'
msg['From'] = 'Jonas Medina'
msg['To'] = username@aa.com
file='-hlthchk.txt'

msg.attach(MIMEText("Labour"))
attachment = MIMEBase('ticket', '-hlthchk.txt')
attachment.set_payload(open(ticket + "-hlthchk.txt", 'rb').read())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment; filename="-hlthchk.txt"' % os.path.basename(file))
msg.attach(attachment)

print('Send email.')
conn.sendmail(sender, receivers, msg.as_string())
conn.close()
