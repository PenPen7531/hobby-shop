import json
from models.toy import Toy
class Collection:
    def __init__(self, collection_name):
        if type(collection_name) != str:
            raise TypeError
        self.name =  collection_name
        self.collection = []
        try:
            with open(f"data/{self.name}.json") as file:
                self.collection = [
                    Toy(
                        toy["name"], 
                        toy["price"],
                        toy["description"],
                        toy["link"]
                    ) for toy in json.load(file)
                ]
        except:
            self.employees = []
