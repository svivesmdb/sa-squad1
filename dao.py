
from pymongo import MongoClient

# Set your classes here.


class DAO():

    client = -1

    def __init__(self, url):
        self.client = MongoClient(url)
        self.db = self.client.proofPointsManager
    
    def addProofPoint(self, company, industry, project, project_desc, use_case, creation_date, owner_id):
        
        pp = {
            "customerCompany":company,
            "customerIndustry":industry,
            "customerProject": project,
            "customerProjectDescription": project_desc,
            "useCase":use_case,
            "creationDate": creation_date,
            "owner_id": owner_id
        }

        self.db.proofPoints.insert_one(pp)

    def getProofPoints(self):
        cursor = self.db.proofPoints.find({})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs

    def getProofPoint(self, id):
        return self.db.proofPoints.find({"_id" : id})
    
    def downloadProofPoint(self, id):
        return self.db.proofPoints.find({"_id" : id})
    
    def searchProofPoints(self):
        return self.db.proofPoints.find({})
    
    def getProofPointUrl(self):

        pass
