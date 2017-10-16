#!/usr/local/bin/python
# coding: latin-1
import os, sys
import vk
import time
import datetime
def ping(p):
app_id, login, password = '6130262', 'anmalyanov@gmail.com', ''
session = vk.AuthSession(app_id, login, password, scope='messages')
vk_api = vk.API(session, v='5.62')
vk_api.messages.send(user_id='197195467', message=p)
time.sleep(3600)
while True:
response = os.system("ping -c 1 " + 'deslab.kz') 
if response == 0:
ping('Сайт в норме')
else:
ping('Сайт отказал')
break