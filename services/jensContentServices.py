from common.responses_services import BadRequest,Created,InternalServerError, Ok
from models.user import User
from repository.jenisContentRepository import jenisContentRepository


class JenisContentServices:


    @staticmethod
    async def get_all(requestUser:User,limit:int,terms:str):
        try:
            data, numdata = jenisContentRepository.get_all_jenis_cont(limit=limit,terms=terms)
            return Ok(data={
                'count':numdata,
                'results':[{
                    'id':item.id,
                    'name':item.name,

                }for item in data]
            })
        except Exception as e:
            return InternalServerError(error=str(e))
    
    @staticmethod
    async def get_detail(id:int):
        try:
            data = jenisContentRepository.get_detail_jenis_cont(id=id)
            return Ok(data={
                'id':data.id,
                'name':data.name,
                'catatan':data.catatan
            })
        except Exception as e:
            return InternalServerError(error=str(e))