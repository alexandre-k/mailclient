import smtplib


class MySmtp(object):
    def __init__(self, username, password, server, port=25, debug=False):
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.debug = debug

    def make_secure_connection(self):
        self.connection = smtplib.SMTP_SSL(self.server + ':' + self.port)
        self.connection.starttls()
        self.connection.login(self.username, self.password)
        self.connection.set_debuglevel(self.debug)

    def send(self, msg):
        self.connection.sendmail(sender, recipient, msg)
        self.connection.quit()





