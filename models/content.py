from sqlalchemy import Column, ForeignKey, Integer, String, Text,Boolean,DateTime
from sqlalchemy.orm import relationship
from models import Base

class content(Base):
    __tablename__ = 'content'

    id = Column('id', Integer, primary_key=True, nullable=False)
    jns_content_id = Column('jns_content_id',ForeignKey('jenis_content.id'))
    judul = Column('judul', Text)
    narasi = Column('narasi', Text)
    status = Column('status', Boolean)
    lampiran = Column('lampiran', Text)
    created_date = Column('created_date', DateTime(timezone=True), nullable=False)
    updated_date = Column('updated_date', DateTime(timezone=True))
    created_by = Column('created_by', ForeignKey('user.username'), nullable=False)
    updated_by = Column('updated_by', ForeignKey('user.username'))


