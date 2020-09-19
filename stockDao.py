import pymongo

myclient = pymongo.MongoClient("mongodb://0.0.0.0:27017/")
mydb = myclient["stocks"]
mycol = mydb["signals"]

def findMongo(ticker):
    return mycol.find_one({"ticker": ticker})


def insertMongo(signal):

    x = mycol.insert_one(signal)