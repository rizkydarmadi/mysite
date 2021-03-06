from fastapi import APIRouter, Depends
from common.responses_schemas import BadRequest, InternalServerError,Forbidden
from common.security import oauth2_scheme,get_user_from_jwt_token
from services.jensContentServices import JenisContentServices
from common.responses_services import common_response
from schemas.jenisContent import jenisContentDetailItem, jenisContentRequest, jenisContentResposne


router = APIRouter(
    prefix='/jenis-content',
    tags=['Jenis Content']
)

@router.get('/',responses={
    '200': {'model':jenisContentResposne},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def get_all_jenis_cotent(limit:int=25,terms:str='',token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await JenisContentServices.get_all(requestUser=user,limit=limit,terms=terms)
    return common_response(result)

@router.get('/{id}',responses={
    '200': {'model':jenisContentDetailItem},
    '403': {'model': Forbidden},
    '500': {'model': InternalServerError},
})
async def get_detail_jenis_content(id:int,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await JenisContentServices.get_detail(id=id)
    return common_response(result)

    
@router.post('/',responses={
    '200': {'model':jenisContentResposne},
    '400': {'model': BadRequest},
    '500': {'model': InternalServerError}
})
async def create_jenis_cont(request:jenisContentRequest,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await JenisContentServices.create(requestUser=user,request=request)
    return common_response(result)

@router.put('/{id}',responses={
    '200': {'model':jenisContentResposne},
    '400': {'model': BadRequest},
    '500': {'model': InternalServerError}
})
async def update_jenis_cont(request:jenisContentRequest,id:int,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await JenisContentServices.update(requestUser=user,id=id,request=request)
    return common_response(result)

@router.delete('/{id}',responses={
    '400': {'model': BadRequest},
    '500': {'model': InternalServerError}
})
async def delete_jenis_cont(id:int,token: str = Depends(oauth2_scheme)):
    user = get_user_from_jwt_token(token)
    result = await JenisContentServices.delete(requestUser=user,id=id)
    return result