from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:user123@localhost/testdb"

engine = create_engine(DATABASE_URL,echo=True)

Sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()