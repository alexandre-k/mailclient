import sys
import io
import poplib
import math
import email
from email.parser import Parser


class MyPop(object):
    poplib._MAXLINE=20480

    def __init__(self, username, password, server):
        self.mailbox = poplib.POP3_SSL(server)
        self.mailbox.user(username)
        self.mailbox.pass_(password)
        self.basic_headers = ['Date', 'From', 'To', 'Subject']
        self.detailed_headers = ['Delivered-To', 'List-Post', 'Message-ID', 'From', 'To', 'Subject', 'Content-Type']



    @staticmethod
    def conv_msg_size(size):
        if size==0:
            return '0B'
        suffix = ('B', 'KB', 'MB', 'GB')
        i = math.floor(math.log(int(size), 1024)) # get which suffix to choose
        prefix = math.pow(1024, i)
        return '{} {}'.format(round(size/prefix,2), suffix[i])

    def display_mailbox(self):
        msg_by_index = (msg_num for msg_num in self.mailbox.list()[1])
        total_msgs = len(self.mailbox.list()[1])
        n = 0
        limit_display_overview_msg = 3
        while n < total_msgs:
            for m in msg_by_index:
                m_index = m.decode().split(' ')
                self.display_overview_msg(m_index[0])
                n += 1
                if n == limit_display_overview_msg:
                    answer = input('Next')
                    if answer == '':
                         limit_display_overview_msg += 10
                         break
                    else:
                         sys.exit(0)

    def display_overview_msg(self, index):
        response, lines, octets = self.mailbox.retr(index)
        if b'OK' in response:
            try:
                raw_msg = email.message_from_string(b'\n'.join(lines).decode('utf-8'))
                #print(raw_msg.get('Subject')[0])
                #msg_encoding = email.header.decode_header(raw_msg.get('Subject')[0][1])
                #print(msg_encoding)
            except UnicodeEncodeError:
                pass

        for part in raw_msg.walk():
            print('-'*72)
            for item in part.items():
                if item[0] in self.basic_headers:
                    print(item[0] + ': ' + item[1])
    #        print(part.get_payload())

    def preview_msg(self, num, body_lines):
        self.mailbox.top(num, body_lines)

    def display_overview_msg_content(self, num):
        self.mailbox.retr(num)

    def delete_msg(self, num):
        self.mailbox.dele(num)

    def get_status(self):
        print('Total messages: {} and {} in bytes'.format(self.mailbox.stat()))
        return

    def close(self):
        self.mailbox.quit()

