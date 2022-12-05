import json
from types import SimpleNamespace
from typing import TypeVar, Type

T = TypeVar("T")

class Serializer():
    
    @staticmethod
    def json_to_object(data: str, returnInstance: Type[T]) -> T: 
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
