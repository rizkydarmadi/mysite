from sqlalchemy import Column, Integer, String
from models import Base

class jenisContent(Base):
    __tablename__ = 'jenis_content'

    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(length=255))
    catatan = Column('catatan', String(length=255))

