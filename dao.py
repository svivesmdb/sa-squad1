
from pymongo import MongoClient
import gridfs

# Set your classes here.
# fs.files must be full text indexed using :
#    use proofPointsManager
#    db.fs.files.createIndex({ "$**": "text" })

class DAO():

    def __init__(self, url):
        self.client = MongoClient(url)
        self.db = self.client.proofPointsManager
        self.fs = gridfs.GridFS(self.db)
    
    def addProofPoint(self, file):
    #add should just create the document in fs.files by uploading the file
    #a call must then be made to updateProofPoints to set the metadata    
        id = self.fs.put(file)
        return id

    def updateProofPoint(self, id, pp):
        '''
        pp = {
            "customerCompany": company,
            "customerIndustry": industry,
            "customerProject": project,
            "customerProjectDescription": project_desc,
            "useCase": use_case,
            "creationDate": creation_date,
            "owner_id": owner_id,
            "proofpointKey" : "AEF0897734"
        }
        '''
        self.db.fs.files.update_one({"_id":id},{"$set":{"metadata":pp}})

    def cursorToArray(self,cursor):
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs

    def getProofPoints(self):
        return self.cursorToArray(self.db.proof.fs.files.find({}))

    def getUseCases(self):
        projection = {"_id":0,"name":1}
        return self.cursorToArray(self.db.useCases.find({},projection))

    def getProofPoint(self, id):
        return self.db.fs.files.findOne({"_id" : id})

    def getProofPointByKey(self, key):
        return self.db.fs.files.findOne({"metadata.proofPointKey" : key})
    
    def downloadProofPoint(self, id):
        return self.fs.get({"_id" : id}).read()
    
    def searchProofPoints(self, keywords):
    # keywords is a space separated string with all keywords
        res = self.db.fs.files.find({
            '$text':{
                '$search': "\"" + keywords+  "\"" 
            }
        })
        return self.cursorToArray(res)
    
    def getProofPointUrl(self, pp):
        return self.baseURL + "/proofpoint/" + pp["proofPointKey"]
        pass
