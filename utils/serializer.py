import json
from types import SimpleNamespace

class Serializer():
    def __init__(self) -> None:
        pass

    @staticmethod
    def json_to_object(data: str) -> any: 
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

        