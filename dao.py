
from pymongo import MongoClient

# Set your classes here.


class DAO():

    client = -1

    def __init__(self, url):
        self.client = MongoClient(url)
        self.db = self.client.proofPoints
    
    def addProofPoint(self, author):
        pp = {
            "author":author,
            "":
        }
        s
        pass

    def getProofPoints(self):
        self.db.proofpoints.find({})
        pass
    
    def getProofPointUrl(self):

        pass
