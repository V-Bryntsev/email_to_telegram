# Email_to_telegram
This script send email to telegram.
For work you need install fetchmail and procmail.
Script use socks5 proxy (because telegram "block" in Russia)

## Algorithm:
1. Message with subject "email_to_telegram..." is coming to mail server
2. Mail client/sieve or somthing else put message to specific folder of mailbox
3. Fetchmail by schedule check messages on server folder and transfer it to procmail. Procmail transfer it to script email_to_telegram.py
4. Script parse message, get config for telegram from cfg file and send it to telegram

## Files:
1. .fetchmailrc.example - example of fetchmail config
2. .procmailrc.example - example of procmail config
3. cfg.example - config file example
4. email_to_telegram.py - script

## TODO:
Implement processing attachments
