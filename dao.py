
from pymongo import MongoClient
import gridfs

# Set your classes here.


class DAO():

    def __init__(self, url):
        self.client = MongoClient(url)
        self.db = self.client.proofPointsManager
        self.fs = gridfs.GridFS(self.db)
    
    def addProofPoint(self, company, industry, project, project_desc, use_case, creation_date, owner_id):
        pp = {
            "customerCompany": company,
            "customerIndustry": industry,
            "customerProject": project,
            "customerProjectDescription": project_desc,
            "useCase": use_case,
            "creationDate": creation_date,
            "owner_id": owner_id
        }
        self.db.proofPoints.insert_one(pp)

    def cursorToArray(self,cursor):
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs

    def getProofPoints(self):
        return self.cursorToArray(self.db.proofPoints.find({}))

    def getUseCases(self):
        return self.cursorToArray(self.db.useCases.find({},{"_id:0","name":1}))

    def getProofPoint(self, id):
        return self.db.proofPoints.findOne({"_id" : id})
    
    def downloadProofPoint(self, id):
        return self.db.proofPoints.findOne({"_id" : id})
    
    def searchProofPoints(self, keywords):
        res = self.db.proofPoints.find({
            '$text':{
                '$search': "\"" + keywords+  "\"" 
            }
        })

        return self.cursorToArray(res)
    
    def getProofPointUrl(self):

        pass
