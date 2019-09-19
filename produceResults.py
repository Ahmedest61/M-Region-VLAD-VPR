from sklearn.metrics import auc
import collections
import csv
from matplotlib.pyplot import cm
import matplotlib.colors as coloR
import numpy as np
import  sklearn as skplt
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve,auc,average_precision_score
from itertools import cycle
import os
import matplotlib.pyplot as plt
from pylab import imread,subplot,imshow,show
import matplotlib.gridspec as gridspec
from matplotlib import pyplot

DATASETS = ["Synthesized_Nordland","SPEDTest","StLucia"]
REFERENCE_DATASET = ["summer_ref","refer","190809_0845_ref"]
TEST_DATASET = ["winter_test","query","100909_1410_test"]


datasetIndex = 1



dataset = DATASETS[datasetIndex]
testTraverse = TEST_DATASET[datasetIndex]
referenceTraverse = REFERENCE_DATASET[datasetIndex]


def generatePRCurves():
    
    precision = dict()
    recall = dict()
    auc_pr_curve = dict()
    name = dict()

    rows = 1
    columns = 1
    fig, ax = plt.subplots(rows, columns,sharex=True,sharey=True)  
    names = ["Red","Blue","Brown","Cyan","Green","Grey","Magenta","Orange","Purple","Silver","Yellow"]
    colors = cycle(names)

    
    ind = 0
    DatasetPath = os.path.join(os.getcwd(),dataset,"VPR_Results")
    print(DatasetPath)
    for csVFileName in os.listdir(DatasetPath):
        if "csv" not in csVFileName:
            continue
        approach= csVFileName.split("_")[0]
        print(dataset,approach)
        predictionLabel = []
        predictionScore = []
        
        CSVFilePath = os.path.join(DatasetPath,csVFileName)
        #print(CSVFilePath)
        with open(CSVFilePath, mode='r') as data:
            csv_reader = csv.reader(data, delimiter=',')
            start=0
            for i,row in enumerate(csv_reader):
                predictionLabel.append(float(row[3]))
                predictionScore.append(float(row[2]))


        precision[ind], recall[ind],_ = precision_recall_curve(predictionLabel,predictionScore)
        auc_pr_curve[ind] = auc(recall[ind], precision[ind])
        name[ind] = approach
        ind +=1
        
    lines = []
    labels = []
    #print("Working")
    for i, color in zip(range(ind), colors):        
        l, = ax.plot(recall[i], precision[i], color=color, lw=1.5)
        lines.append(l)
        labels.append('{0} (AUC:{1:.3f})'
                      ''.format(name[i], auc_pr_curve[i])) 

    
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('Recall',fontsize=12)
    ax.set_ylabel('Precision',fontsize=12)
    ax.set_title("Precision Recall curves on "+dataset)
    ax.legend(lines, labels, loc="lower right",fontsize=6.5,shadow=True)
    AUCPath= os.path.join(DatasetPath,"AUCPRcurves.jpg")    
    print(AUCPath)
    plt.savefig(AUCPath,dpi=200)

    
generatePRCurves()
