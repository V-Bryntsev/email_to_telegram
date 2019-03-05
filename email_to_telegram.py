#!/usr/bin/python
# -*- coding: utf-8 -*-

#Script receive email from fetchmail, parse it and send by telegram

import sys #for stdin
#Email parse
import email
from email.header import decode_header
from email.utils import parsedate_tz, mktime_tz, formatdate

import telebot #Telegram API.pip install python-telegram-bot --upgrade
import configparser #For config file parse


#Get message by stdin from fetchmail and parse it
full_msg = sys.stdin.read()
msg = email.message_from_string(full_msg)
to = msg['to']
#For filter, message subject should start by "email_to_telebot"
subject = decode_header(msg['subject'])[0][0].split('email_to_telebot')[1]
body = " "
if msg.is_multipart():
    for payload in msg.get_payload():
         body = body + payload.get_payload()
else:
    body = msg.get_payload()

#parse datetime with time zone
ts = mktime_tz(parsedate_tz(msg["Date"]))
date_time = formatdate(ts, localtime=True)

#Config telegram bot
config = configparser.ConfigParser()
config.read('cfg')
telegram_cfg = config['TELEGRAM']

telegram_username = telegram_cfg['USERNAME']
telegram_pass = telegram_cfg['PASS']
telegram_proxy_hostport = telegram_cfg['PROXY_HOSTPORT']
telegram_token = telegram_cfg['TOKEN']
telegram_recipient = telegram_cfg['RECIPIENT']

bot = telebot.TeleBot(telegram_token)
#if proxy don`t use, next string can be commented
telebot.apihelper.proxy = {'https':'socks5://%s:%s@%s' % (telegram_username,telegram_pass,telegram_proxy_hostport)}
#Create message for telegram and send it
telegram_message = "<b>---EMAIL_TO_TELEGRAM---</b>\n\n\
<b>DATETIME:</b>%s\n\
<b>SUBJECT:</b>%s\n\
<b>BODY:</b>%s\n\
<b>---EMAIL_TO_TELEGRAM---</b>" % (date_time,subject,body)
bot.send_message(telegram_recipient, telegram_message, parse_mode= "HTML")

