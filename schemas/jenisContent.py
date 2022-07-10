from typing import List
from pydantic import BaseModel

class jenisContentItem(BaseModel):
    id : str
    name : str

class jenisContentResposne(BaseModel):

    count : int
    results : List[jenisContentItem]

class jenisContentDetailItem(BaseModel):
    id : str
    name : str
    catatan : str
