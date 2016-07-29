from sqlalchemy import Column, Unicode, Integer
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class MailAccount(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode, index=True)
    password = Column(Unicode)
    account_type = Column(Unicode)
    mail_server = Column(Unicode)


class CreateAccount(object):
    def __init__(self, db_name, db_dir):
        self.db_name = db_name
        self.db_dir = db_dir
        from sqlalchemy import create_engine
        self.engine = create_engine('sqlite:////{}/{}'.format(self.db_name,
                                                              self.db_dir))
        from sqlalchemy.orm import sessionmaker
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def db_exists(self):
        if os.path.exists(self.db_dir) and os.path.isfile(self.db_name):
            return True
        else:
            return False

    def make_account(self, username, password, mail_server, account_type):
        new_account = MailAccount(username=username,
                                  password=password,
                                  mail_server=mail_server,
                                  account_type=account_type)
        s = self.session()
        s.add(new_account)
        s.commit()

    def query_db(self, username):
            s = self.session()
            return s.query(MailAccount).filter(MailAccount.username==username)
