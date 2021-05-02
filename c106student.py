import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath) :
    marksInP = []
    daysPresent=[]
    with open (dataPath) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marksInP.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
            
    return {"x":marksInP,"y":daysPresent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])

    print("CORRELATION BETWEEN MARKS IN PERCENTAGE AND DAYS PRESENT IS :",correlation[0,1])
    
def setup():
    dataPath="c106student.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    
setup()
