import numpy as np

fname = 'test_rawdatat_mario.txt'

#file = open(fname, 'r',encoding='UTF-8') 
#
#data = file.readlines()



#text = []
#with open(fname, 'r', encoding='UTF-8') as f:
#    for line in f:
#        text.append(line)
#
#text2 = text[4:]
#
#
#
#
#  
#textdata = []   
#for line in text2:
#   line = line.split('    ')
#   textdata.append(line)
#    print (line)
##    line = line.rstrip()
    
import pandas as pd
df = pd.read_csv(fname, sep = '\t', header = 4)

rt = df['RecordingTime [ms]'].tolist()

np.mean(rt)
df.columns
df.columns.get_loc("Eye Position Right Y [mm]")

df['RecordingTime [ms]']
df.loc[0]