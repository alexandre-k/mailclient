from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import make_msgid

msg = MIMEMultipart()

class Message():
    def __init__(self, subject, from_field, to_field):
        self.msg['Subject'] = subject
        self.msg['From'] = from_field
        self.msg['To'] = to_field

    def make_msg_content(self, content):
        pass
        #msg.set_content(content)

    def make_header(self):
        pass

    def print_msg(self):
        print(self.msg)


    with open('mail.txt', 'r') as mail:
        msg = MIMEText(mail.read())


msg = Message('a subject', 'k.alex@fsolution.co.jp', 'recipient@mail.com')
msg.make_msg_content(
        '''
        Dear me,

        It is a test.

        Sincerely,
        Alex
        '''
        )
#msg.print_msg()
