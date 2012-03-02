#!/usr/bin/python
from os import path

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.ext.declarative import declarative_base

from urlparse import urlparse, urljoin


# Website
   # n / hash       int/hash
   # domain         text
   # page           One to Many

# Page
   # website        Many to One
   # sublink        text
   # full url       text
   # content        text

# Subdomain


Base = declarative_base()


class Webpage(Base):
   # Administrivia
   __tablename__ = 'webpage'
   pk = Column(Integer, primary_key = True)
   first_craw_date = Column(DateTime, default=func.now())
   last_crawl_date = Column(DateTime, default=func.now(), onupdate=func.now())

   # Juice
   full_url = Column(String)
   html = Column(String)
   num_crawls = Column(Integer, default = 1)
   
   
   def __init__(self, full_url, html):
      self.full_url = full_url
      self.html = html

   def __repr__(self):
      return "<Webpage('%s')>" % (self.full_url)

   def get_path(self):
      return urlparse(self.full_url).path

   def get_base_url(self):
      return urljoin(urlparse(self.full_url).scheme, urlparse(self.full_url).netloc)   
      


class Database(object):
   session = None

   def __init__(self, db="sqlite:///db.sqlite"):
      # Engine and schema creation
      self.engine = create_engine(db)
      Base.metadata.create_all(self.engine)
      # Get a session so we can do stuff
      Session = sessionmaker(bind=self.engine)
      self.session = Session()
      
      
   