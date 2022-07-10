from typing import List, Tuple
from models import Session
from models.jenis_content import jenisContent
from sqlalchemy import select,or_,func

class jenisContentRepository():

    @staticmethod
    def get_all_jenis_cont(limit:int=None,terms:str=None)-> Tuple[List[jenisContent],int]:
        with Session() as session:
            stmt = select(jenisContent)\
                .where(or_(jenisContent.name.ilike(f'%{terms}%'),jenisContent.catatan.ilike(f'%{terms}%')))\
                .order_by(jenisContent.name.asc())\
                .limit(limit=limit)
            data = session.execute(stmt).scalars().all()

            stmt2 = select(func.count(jenisContent.id))\
                .where(or_(jenisContent.name.ilike(f'%{terms}%'),jenisContent.catatan.ilike(f'%{terms}%')))
            num_data = session.execute(stmt2).scalar()
        
        return data,num_data

    @staticmethod
    def get_detail_jenis_cont(id=int)->jenisContent:
        with Session() as session:
            stmt = select(jenisContent).where(jenisContent.id==id)
            data = session.execute(stmt).scalar()

        return data