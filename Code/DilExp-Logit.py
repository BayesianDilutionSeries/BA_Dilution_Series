###################################################
# Logistic regression for dilution series  
# 
# Marco A. Aquino-López
###################################################

import numpy as np
import scipy as sp
from pandas import read_excel

import DilExp as DE


CBE =\
[['RoomTemp', [ 1, 10, 15], "blue"],\
 [ '65CTemp', [15, 30, 45, 60, 90], "yellow"],\
 [ '70CTemp', [10, 20, 30, 40, 60], "orange"],\
 [ '75CTemp', [10, 20], "red"],\
 [ '80CTemp', [ 1,  2], "firebrick"]]

CBEData = read_excel( './Data/CBE_BiofilmHotWaterStudies.xls',\
                ['RoomTemp', '65CTemp', '70CTemp', '75CTemp', '80CTemp'])

rt_CBE =[]
    print("%16s, %2s, %16s, %16s, %16s, %16s" %\
              ( "experiment", "k" , "bbinom" , "binom" , "Prob binom", "BF"))
    for item in CBE:
        experiment= item[0]
        for time in item[1]:
            rt_CBE += AnaBF( CBEData=CBEData, experiment=experiment, time=time)
    dump( rt_CBE, open("CBE_rt_CBE.pkl", "wb")) #To be used by InterLabExamples in the BF plot

    All = {} ### Dictiionary to hold MCMC iterations of E for all experiments



















