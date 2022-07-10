from common.responses_services import BadRequest,Created,InternalServerError, Ok
from models.user import User
from repository.jenisContentRepository import jenisContentRepository
from schemas.jenisContent import jenisContentRequest


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
    
    @staticmethod
    async def create(requestUser:User,request:jenisContentRequest):

        jenis_cotent = jenisContentRepository.create_new_jenis_cont(
            name=request.name,
            catatan=request.catatan
            )
        return Created(data={
            'id':jenis_cotent.id,
            'name':jenis_cotent.name,
            'catatan':jenis_cotent.catatan
        })

    @staticmethod
    async def update(requestUser:User,id:int,request:jenisContentRequest):
        jenis_cotent = jenisContentRepository.update_jenis_cont(
            id=id,
            name=request.name,
            catatan=request.catatan
            )

        return Ok(data={
            'id':jenis_cotent.id,
            'name':jenis_cotent.name,
            'catatan':jenis_cotent.catatan
        })
    
    @staticmethod
    async def delete(requestUser:User,id:int):
        data = jenisContentRepository.delete_jenis_cont(id=id)
        return Ok(data={'message':f'{data} has been deleted'})