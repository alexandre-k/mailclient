from pop3 import MyPop
from smtp import MySmtp
from credentials import CreateAccount
from message import Message
from getpass import getpass

account = CreateAccount('fsolution.db', '/var/db/')
if account.db_exists:
    username, password, server = get_credentials('k.alex@fsolution.co.jp')
else:
    print('It is the first time you connect')
    username = input('Enter your mail address: ')
    password = getpass('Enter your password: ')
    server = input('Server name: ')
    account.make_account('')

#smtp_conn = MySmtp(username, password, 'sv34.wadax.ne.jp', debug=True)
server = MyPop(username, password, server)
server.display_mailbox()

#server.display_msg(3)
server.close()
