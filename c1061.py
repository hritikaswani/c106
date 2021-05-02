import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath) :
    iceCreamSales = []
    tempData=[]
    with open (dataPath) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            iceCreamSales.append(float(row["Temperature"]))
            tempData.append(float(row["Ice-cream Sales( â‚¹ )"]))
            
    return {"x":iceCreamSales,"y":tempData}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])

    print("CORRELATION BETWEEN TEMPERATURE AND ICE CREAM SALES IS :",correlation[0,1])
    
def setup():
    dataPath="106temp.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    
setup()
