from typing import Tuple,List
from models import Session, jenis_content
from sqlalchemy import or_, select, func,and_
from sqlalchemy.orm import joinedload
from models.content import Content
from models.user import User
import datetime
import pytz
from datetime import datetime

class ContentRepository():


    @staticmethod
    def get_all_content(limit:int=None,terms:str=None)->Tuple[List[Content],int]:
        with Session() as session:
            stmt = select(Content)\
                .options(joinedload(Content.jenis))\
                .where(or_(Content.judul.ilike(f'{terms}'),(Content.narasi.ilike(f'{terms}'))))\
                .where(Content.status==True)\
                .limit(limit=limit)
            data = session.execute(stmt).scalars().all()

            stmt2 = select(func.count(Content.id))\
                .where(or_(Content.judul.ilike(f'{terms}'),(Content.narasi.ilike(f'{terms}'))))
            num_data = session.execute(stmt2).scalars().all()

        return data,num_data
    
    @staticmethod
    def get_detail_content(id=int)->Content:
        with Session() as session:
            stmt = select(Content)\
                .options(joinedload(Content.jenis))\
                .where(Content.id==id,Content.status==True)
            data = session.execute(stmt).scalar()
    
    @staticmethod
    def create_new_content(jenis_cont:int,judul:str,narasi:str,status:bool,lampiran:str,user:User)->Content:
        with Session() as session:
            new_content = Content(
                jns_content_id=jenis_content,
                judul=judul,
                narasi=narasi,
                status=status,
                lampiran=lampiran,
                created_by = user.username,
                created_date= datetime.now(pytz.timezone('Asia/Jakarta'))
            )
            session.add(new_content)
            session.commit()
            session.refresh(new_content)
        return new_content
    
    @staticmethod
    def update_content(id:int,jenis_cont:int,judul:str,narasi:str,status:bool,lampiran:str,user:User)->Content:
        with Session() as session:

            stmt = select(Content).where(Content.id==id)
            data = session.execute(stmt).scalar()

            # updated data
            data.jns_content_id = jenis_cont
            data.judul = judul
            data.narasi = narasi
            data.status = status
            data.lampiran = lampiran
            data.updated_by = user.username
            data.updated_date = datetime.now(pytz.timezone('Asia/Jakarta'))

            session.commit()

            stmt = select(Content).where(Content.id==id)
            data = session.execute(stmt).scalar()

        return data

    @staticmethod
    def delete_cont(id:int)->str:
        with Session() as session:
            stmt = select(Content).where(Content.id==id)
            data = session.execute(stmt).scalar()

            judul_cont = data.judul

            session.delete(data)
            session.commit()
        
        return judul_cont

    

