from tibiapy.models import Character
from bson.objectid import ObjectId


class CharacterData(Character):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
