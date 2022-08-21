from typing import TypedDict

from pymongo import MongoClient
from tqdm.auto import tqdm


class DocumentDict(TypedDict):
    age: float
    days: float
    gender: int
    cover: int
    province: int
    relation: int
    damage: float


class DamageCollectionWrapper:
    def __init__(self, client: MongoClient):
        self.database = client["damage_database"]
        self.collection = self.database["damage_collection"]
        self.collection.create_index("index", unique=True)

    def __len__(self) -> int:
        return self.collection.count_documents({})

    def create(self, document: DocumentDict) -> int:
        index = len(self)
        document["index"] = index
        self.collection.insert_one(document)
        return index

    def read(self, index: str) -> DocumentDict:
        document = self.collection.find_one({"index": index})
        if document is None:
            raise IndexError(f"{index=} is out of range")
        else:
            return document


def csv_line_to_document(line: str) -> DocumentDict:
    line = line.strip()
    age, days, gender, cover, province, relation, damage = line.split(",")
    age, days, damage = map(float, (age, days, damage))
    gender, cover, province, relation = map(int, (gender, cover, province, relation))
    return {
        "age": age,
        "days": days,
        "gender": gender,
        "cover": cover,
        "province": province,
        "relation": relation,
        "damage": damage,
    }
