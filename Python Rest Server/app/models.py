from datetime import datetime
from time import time
from app import db
from sqlalchemy import Column
from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import Time



class Tasks(db.Model):
    id=Column(Integer,primary_key=True)
    title=Column(String(140))
    description=Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    scheduledDateTime=Column(DateTime,index=True,default=datetime.utcnow)
    completionDateTime=Column(DateTime,index=True,default=datetime.utcnow)
    comments=Column(String(140),default="")
    done=Column(Boolean,unique=False,default=False)
    reminder=Column(Boolean,unique=False,default=False)

    def __repr__(self):
        return '<Tasks {}>'.format(self.title)