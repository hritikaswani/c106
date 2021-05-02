import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath) :
    SizeOfTv = []
    avgTimeSpent=[]
    with open (dataPath) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            SizeOfTv.append(float(row["Size of TV"]))
            avgTimeSpent.append(float(row["\tAverage time spent watching TV in a week"]))
            
    return {"x":SizeOfTv,"y":avgTimeSpent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])

    print("CORRELATION BETWEEN SIZE OF TV AND AVERAGE TIME SPENT WATCHING TV IN A WEEK IS :",correlation[0,1])
    
def setup():
    dataPath="c106tv.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    
setup()
