from datetime import datetime
from typing import TypeVar
from pydentic import BaseModel

T = TypeVar("T")

class BaseFile(BaseModel):
    def __init__(self, name:str, owner:str, data:any):
        self.name:str = name
        self.size:int #calculate field
        self.create_date:datetime # calculate field
        self.owner:str = owner
        self.__data:any = data

    def update(self, data:any):
        ...

class BaseStore():
    def __init__(self):
        ...
    
    def __next__(self)->T:
        ...
    
    def __iter__(self)->T:
        ...
    
    def delete(self, file:BaseFile)->bool:
        ...
    
    def save(self, file:BaseFile)->bool:
        ...

class Mp3File(BaseFile):
    def __init__(self, name:str, owner:str, data:any):
        super().__init__(name, owner, data)
        self.create_date = datetime.now()
        self.length:int

class JpgFile(BaseFile):
    def __init__(self, name:str, owner:str, dpi:int, data:any):
        super().__init__(name, owner, data)
        self.create_date = datetime.now()
        self.dpi:int = dpi

class BmpFile(BaseFile):
    def __init__(self, name:str, owner:str, data:any):
        super().__init__(name, owner, data)
        self.create_date = datetime.now()
        self.length:int
        self.bit:int

class LocalStore(BaseStore):
    def __init__(self):
        super().__init__()

class GoogleStore(BaseStore):
    def __init__(self):
        super().__init__()

class AnyStore(BaseStore):
    def __init__(self):
        super().__init__()

class Utilites():
    
    @staticmethod
    def convert(store:BaseStore, src_file:BaseFile, dst_type:type[BaseFile])->BaseFile:
        ...

    @staticmethod
    def delete(store:BaseStore, file:BaseFile)->bool:
        ...
    
    @staticmethod
    def copy(src_store:BaseStore, src_file:BaseFile, dst_store:BaseStore, dst_file:BaseFile)->int:
        ...
    
    @staticmethod
    def create_mp3(store:BaseStore, name:str, owner:str, data:any)->BaseFile:
        ...
    
    @staticmethod
    def update(store:BaseStore, file:BaseFile, data:any)->bool:
        ...
