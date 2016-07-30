import smtplib


class MySmtp(object):
    def __init__(self, username, password, server, port=25, debug=False):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.debug = debug

    def make_secure_connection(self):
        self.connection = smtplib.SMTP(self.server)
        print('SSL')
        self.connection.starttls()
        print('Login')
        self.connection.login(self.username, self.password)
        print('Next')
        self.connection.set_debuglevel(self.debug)

    def send(self, to_field, from_field, msg):
        self.make_secure_connection()
        self.connection.sendmail(to_field, from_field, msg)
        self.connection.quit()
