LBJ_PT_raw_data.dropna()
# *** Spyder Python Console History Log ***
LBJ_PT_raw_data.to_csv(maindir+'3-LBJ/LBJ-PT-Stage-final.csv')
"""
Created on Wed Jul 15 14:17:48 2015

@author: Alex
"""

## CTRL-SPACE for code completion options

#### Import modules
## Data Processing
import os
import numpy as np
import pandas as pd
#import math
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
## Set Pandas display options
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.width', 180)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 10)
#pd.set_option('display.precision', 3)


#plt.close('all')

#timer
import datetime as dt
now = dt.datetime.now()
print 'Start time: '+now.strftime('%H:%M:%S')
now_date = now.strftime('%d_%m_%Y')


#### DIRECTORIES
Laptop = 'Field'
Laptop = 'Alex'
#Laptop = 'Trent'

if Laptop == 'Field': 
    maindir = "C:/Users/geoguser/Desktop/FieldLaptop/AmSamFieldLaptop/Siumu's Folder/"
    dirs={'main':maindir}


if Laptop == 'Alex': 
    maindir = "C:/Users/atm19/Documents/Github/Fagaalu_monitoring/Fagaalu_Monitoring_2016/"
    dirs={'main':maindir}


if Laptop == 'Trent': 
    maindir = "C:/Users/atm19/Google Drive/AmSamFieldLaptop/Siumu's Folder/" # <<<< TRENT ADD YOUR PATH HERE
    dirs={'main':maindir}



## Year Interval Times
#start2012, stop2012 = dt.datetime(2012,1,1,0,0), dt.datetime(2012,12,31,11,59)    
#start2013, stop2013 = dt.datetime(2013,1,1,0,0), dt.datetime(2013,12,31,11,59)
#start2014, stop2014 = dt.datetime(2014,1,1,0,0), dt.datetime(2014,12,31,11,59)   
#start2015, stop2015 = dt.datetime(2015,1,1,0,0), dt.datetime(2015,12,31,11,59)   
start2016, stop2016 = dt.datetime(2016,1,1,0,0), dt.datetime(2016,6,1,11,59)   

LBJ_PT_raw_data= pd.DataFrame.from_csv(maindir+'3-LBJ/LBJ-PT-Stage-raw.csv')
LBJ_PT_raw_data
LBJ_PT_raw_data.dropna()
LBJ_PT_final_data = correct_Stage_data(LBJ_correction_df,LBJ_PT_raw_data)
def correct_Stage_data(corrections,raw_stage):
    print 'Correcting stage...'
    Correction=pd.DataFrame()
    for correction in corrections.iterrows():
        #print correction[1]
        t1 = pd.to_datetime(correction[1]['T1_datetime'])
        t2 = pd.to_datetime(correction[1]['T2_datetime'])
        z = correction[1]['zshift_cm']    
        print t1,t2, z
        ## Make time series of zshift correction factors
        Correction = Correction.append(pd.DataFrame({'zshift_cm':float(z)},index=pd.date_range(t1,t2,freq='5Min')))
    ## Make complete time series    
    Correction = Correction.reindex(pd.date_range(start2016,stop2016,freq='5Min'))
    ## Add correction factors to PT data
    raw_stage['zshift_cm'] = Correction['zshift_cm']
    ## Calculate corrected stage
    raw_stage['corrected_stage_cm'] = raw_stage['raw_stage_cm'] + raw_stage['zshift_cm']
    ## Add in the part of the timeseries that did not need correction
    raw_stage['stage_cm']=raw_stage['corrected_stage_cm'].where(raw_stage['corrected_stage_cm']>0,raw_stage['raw_stage_cm'])#.round(0)
    return raw_stage

LBJ_correction_list = [[start2016,stop2016,'0']]
LBJ_correction_df = pd.DataFrame(LBJ_correction_list,columns=['T1_datetime','T2_datetime','zshift_cm'])
LBJ_PT_final_data = correct_Stage_data(LBJ_correction_df,LBJ_PT_raw_data)
LBJ_PT_final_data
LBJ_PT_final_data['stage_cm'].plot()
LBJ_PT_final_data.to_csv(maindir+'3-LBJ/LBJ-PT-Stage-final.csv')
LBJ_stage = pd.DataFrame.from_csv(maindir+'3-LBJ/LBJ-PT-Stage-final.csv') ## FINAL/CORRECTED STAGE DATA
LBJ_stage
LBJ_stage.dropna()
LBJ_stage['stage_cm'].plot()
del LBJ_stage['zshift_cm']
from Mannings_from_stage import Mannings_Q_from_stage_data
LBJ_S, LBJ_n, LBJ_k = 0.016, .067, 1
LBJ_stage_reduced = LBJ_stage['stage_cm'].dropna().round(0).drop_duplicates().order()
LBJ_stage_reduced 
LBJ_Man_reduced = Mannings_Q_from_stage_data(maindir+'3-LBJ/LBJ_cross_section.xlsx','LBJ_m',Slope=LBJ_S,Manning_n=LBJ_n,k=LBJ_k, stage_data=LBJ_stage_reduced)
LBJ_Man_reduced 
plt.scatter(LBJ_Man_reduced['stage(m)'], LBJ_Man_reduced['Q(m3/s)'])
LBJ_stage['stage_m'] = LBJ_stage['corrected_stage_cm'].round(0)/100.
LBJ_stage['Q(m3/s)'] = np.nan
LBJ_stage
LBJ_stage.dropna()
LBJ_stage.dropna(how='all')
for row in LBJ_stage.dropna(how='all').iterrows():
    print row[0]
    stage = row[1]['stage_m']
    try:
        Q = LBJ_Man_reduced[LBJ_Man_reduced['stage(m)']==stage]['Q(m3/s)'].iloc[0]
        LBJ_stage.loc[row[0],'Q(m3/s)'] = Q
    except:
        print "Can't get Q data from LBJ_Man_reduced"+ str(row[0])+str(stage)

LBJ_stage['Q(m3/s)'].plot()

##---(Tue Jun 14 10:29:31 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Code/Fagaalu-PT data process.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Code')
fig, Q = plt.subplots(1,1)
Q.plot_date(LBJ_stage.index, LBJ_stage['Q(m3/s)'])
fig, Q = plt.subplots(1,1)
Q.plot_date(LBJ_stage.index, LBJ_stage['Q(m3/s)'],marker='none',ls='-',c='r')
fig, Q = plt.subplots(1,1)
Q.plot_date(LBJ_stage.index, LBJ_stage['Q(m3/s)'],marker='None',ls='-',c='r')

##---(Tue Jun 14 10:36:54 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Code/Fagaalu-PT data process.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Code')

##---(Tue Jun 14 14:58:39 2016)---
"""
Created on Wed Jul 15 14:17:48 2015

@author: Alex
"""

## CTRL-SPACE for code completion options

#### Import modules
## Data Processing
import os
import numpy as np
import pandas as pd
#import math
import datetime as dt
import matplotlib
import matplotlib.pyplot as plt
## Set Pandas display options
pd.set_option('display.large_repr', 'truncate')
pd.set_option('display.width', 180)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 10)
#pd.set_option('display.precision', 3)


#plt.close('all')

#timer
import datetime as dt
now = dt.datetime.now()
print 'Start time: '+now.strftime('%H:%M:%S')
now_date = now.strftime('%d_%m_%Y')


#### DIRECTORIES
Laptop = 'Field'
Laptop = 'Alex'
#Laptop = 'Trent'

if Laptop == 'Field': 
    maindir = "C:/Users/geoguser/Desktop/FieldLaptop/AmSamFieldLaptop/Siumu's Folder/"
    dirs={'main':maindir}


if Laptop == 'Alex': 
    maindir = "C:/Users/atm19/Documents/Github/Fagaalu_monitoring/Fagaalu_Monitoring_2016/"
    dirs={'main':maindir}


if Laptop == 'Trent': 
    maindir = "C:/Users/atm19/Google Drive/AmSamFieldLaptop/Siumu's Folder/" # <<<< TRENT ADD YOUR PATH HERE
    dirs={'main':maindir}



## Year Interval Times
#start2012, stop2012 = dt.datetime(2012,1,1,0,0), dt.datetime(2012,12,31,11,59)    
#start2013, stop2013 = dt.datetime(2013,1,1,0,0), dt.datetime(2013,12,31,11,59)
#start2014, stop2014 = dt.datetime(2014,1,1,0,0), dt.datetime(2014,12,31,11,59)   
#start2015, stop2015 = dt.datetime(2015,1,1,0,0), dt.datetime(2015,12,31,11,59)   
start2016, stop2016 = dt.datetime(2016,1,1,0,0), dt.datetime(2016,6,1,11,59)   

FOREST_stage = pd.DataFrame.from_csv(maindir+'1-FOREST/FOREST-PT-Stage-final.csv')
FOREST_stage
print FOREST_stage
print FOREST_stage.dropna(how='all')
0 + np.nan
FOREST_stage = pd.DataFrame.from_csv(maindir+'1-FOREST/FOREST-PT-Stage-final.csv')

### HEC-RAS Model of the DAM structure: Documents/HEC/FagaaluDam.prj
def HEC_piecewise(PTdata):
    if type(PTdata)!=pd.Series:
        PTdata = pd.Series(data=PTdata)
    HEC_a1, HEC_b1 = 9.9132, -5.7184 ## from excel DAM_HEC.xlsx
    HEC_a2, HEC_b2 = 25.823, -171.15 
    HEC_a3, HEC_b3 = 98.546, -3469.4
    
    Func1=PTdata[PTdata<=11]*HEC_a1 + HEC_b1
    Func2=PTdata[(PTdata>11)&(PTdata<=45)]*HEC_a2 + HEC_b2
    Func3=PTdata[PTdata>45]*HEC_a3 + HEC_b3
    AllValues = Func1.append([Func2,Func3])
    return AllValues


FOREST_HEC = pd.DataFrame(data=range(0,150),columns=['stage(cm)'])
FOREST_HEC['Q_HEC(L/sec)'] = HEC_piecewise(FOREST_HEC['stage(cm)'])

FOREST_HEC['Q_HEC(L/sec)']= HEC_piecewise(FOREST_HEC['stage(cm)']).values

DAM_HEC = pd.ols(y=DAMstageDischarge['Q_HEC(L/sec)'],x=DAMstageDischarge['stage(cm)'],intercept=True) 



FOREST_stage = pd.DataFrame.from_csv(maindir+'1-FOREST/FOREST-PT-Stage-final.csv')

### HEC-RAS Model of the DAM structure: Documents/HEC/FagaaluDam.prj
def HEC_piecewise(PTdata):
    if type(PTdata)!=pd.Series:
        PTdata = pd.Series(data=PTdata)
    HEC_a1, HEC_b1 = 9.9132, -5.7184 ## from excel DAM_HEC.xlsx
    HEC_a2, HEC_b2 = 25.823, -171.15 
    HEC_a3, HEC_b3 = 98.546, -3469.4
    
    Func1=PTdata[PTdata<=11]*HEC_a1 + HEC_b1
    Func2=PTdata[(PTdata>11)&(PTdata<=45)]*HEC_a2 + HEC_b2
    Func3=PTdata[PTdata>45]*HEC_a3 + HEC_b3
    AllValues = Func1.append([Func2,Func3])
    return AllValues


FOREST_HEC = pd.DataFrame(data=range(0,150),columns=['stage(cm)'])
FOREST_HEC['Q_HEC(L/sec)'] = HEC_piecewise(FOREST_HEC['stage(cm)'])

FOREST_HEC['Q_HEC(L/sec)']= HEC_piecewise(FOREST_HEC['stage(cm)']).values

DAM_HEC = pd.ols(y=FOREST_HEC['Q_HEC(L/sec)'],x=FOREST_HEC['stage(cm)'],intercept=True) 



DAM_HEC
FOREST_stage = pd.DataFrame.from_csv(maindir+'1-FOREST/FOREST-PT-Stage-final.csv')

### HEC-RAS Model of the DAM structure: Documents/HEC/FagaaluDam.prj
def HEC_piecewise(PTdata):
    if type(PTdata)!=pd.Series:
        PTdata = pd.Series(data=PTdata)
    HEC_a1, HEC_b1 = 9.9132, -5.7184 ## from excel DAM_HEC.xlsx
    HEC_a2, HEC_b2 = 25.823, -171.15 
    HEC_a3, HEC_b3 = 98.546, -3469.4
    
    Func1=PTdata[PTdata<=11]*HEC_a1 + HEC_b1
    Func2=PTdata[(PTdata>11)&(PTdata<=45)]*HEC_a2 + HEC_b2
    Func3=PTdata[PTdata>45]*HEC_a3 + HEC_b3
    AllValues = Func1.append([Func2,Func3])
    return AllValues


FOREST_HEC = pd.DataFrame(data=range(0,150),columns=['stage(cm)'])
FOREST_HEC['Q_HEC(L/sec)'] = HEC_piecewise(FOREST_HEC['stage(cm)'])

FOREST_HEC['Q_HEC(L/sec)']= HEC_piecewise(FOREST_HEC['stage(cm)']).values

FOREST_HEC_rating = pd.ols(y=FOREST_HEC['Q_HEC(L/sec)'],x=FOREST_HEC['stage(cm)'],intercept=True) 



FOREST_HEC_rating
FOREST_stage['Q(L/sec)'] = HEC_piecewise(FOREST_stage['stage_cm'])
FOREST_stage
FOREST_stage['Q(L/sec)'].plot()
if 'LBJ_Man' not in locals():
    try:
        ## Import final/corrected stage data from csv's (created in Module 1)
        LBJ_stage = pd.DataFrame.from_csv(maindir+'3-LBJ/LBJ-PT-Stage-final.csv') ## FINAL/CORRECTED STAGE DATA
        ## Straight from csv
        LBJ_Man_reduced = pd.DataFrame.from_csv(maindir+'3-LBJ/LBJ_Man_reduced.csv')
    except:
        ## Import final/corrected stage data from csv's (created in Module 1)
        LBJ_stage = pd.DataFrame.from_csv(maindir+'3-LBJ/LBJ-PT-Stage-final.csv') ## FINAL/CORRECTED STAGE DATA
        del LBJ_stage['zshift_cm']
        ## Calculate discharge from Manning's equation, for each cm of stage
        from Mannings_from_stage import Mannings_Q_from_stage_data
        ## Mannings parameters for the LBJ
        LBJ_S, LBJ_n, LBJ_k = 0.016, .067, 1
        ## Create a dataframe of only the stage values that are recorded
        LBJ_stage_reduced = LBJ_stage['stage_cm'].dropna().round(0).drop_duplicates().order()
        ## Calculate discharge with Mannings on the reduced range of values
        LBJ_Man_reduced = Mannings_Q_from_stage_data(maindir+'3-LBJ/LBJ_cross_section.xlsx','LBJ_m',Slope=LBJ_S,Manning_n=LBJ_n,k=LBJ_k, stage_data=LBJ_stage_reduced)
        ## Visualize Stage-Q Rating
        plt.scatter(LBJ_Man_reduced['stage(m)'], LBJ_Man_reduced['Q(m3/s)'])
        ## Save the output to csv
        LBJ_Man_reduced.to_csv(maindir+'3-LBJ/LBJ_Man_reduced.csv')


try:
    del LBJ_stage['zshift_cm']
except:
    pass


## Add to stage
#LBJ_stage['corrected_stage_cm'] = LBJ_stage['corrected_stage_cm'] + 5. ## add 5cm so no zero/negative values???? Not sure what this is from, maybe offset with the AV measurements
LBJ_stage['stage_m'] = LBJ_stage['corrected_stage_cm'].round(0)/100.

## Match discharge to stage records for whole time series
## Add column for Discharge
LBJ_stage['Q(m3/s)'] = np.nan

## Iterate over stage records and add discharge value from the reduced stage record for which Manning's Q was calculated
## This saves you from re-calculating Mannings for each stage value, just do it once for each cm of stage!
for row in LBJ_stage.dropna(how='all').iterrows():
    #print row[0]
    stage = row[1]['stage_m']
    try:
        Q = LBJ_Man_reduced[LBJ_Man_reduced['stage(m)']==stage]['Q(m3/s)'].iloc[0]
        LBJ_stage.loc[row[0],'Q(m3/s)'] = Q
    except:
        print "Can't get Q data from LBJ_Man_reduced"+ str(row[0])+str(stage)
    #print row[0], stage, Q
    # .iloc[row_index,col_index] = value
    # .loc[row_index,col_index] = value


## Visualize Q timeseries
fig, Q = plt.subplots(1,1)
Q.plot_date(LBJ_stage.index, LBJ_stage['Q(m3/s)'],marker='None',ls='-',c='r')
## Pass stage data on to discharge df
LBJ_Q = LBJ_stage
## ADD a L/sec
LBJ_Q['Q(L/sec)'] = LBJ_Q['Q(m3/s)'] * 1000
## Save the Q timeseries output to csv
LBJ_Q.to_csv(maindir+'3-LBJ/LBJ_Q.csv')

FOREST_Q = FOREST_stage
fig, Q = plt.subplots(1,1)

Q.plot_date(LBJ_Q.index, LBJ_Q['Q(L/s)'],marker='None',ls='-',c='r')
Q.plot_date(FOREST_Q.index, FOREST_Q['Q(L/s)'],marker='None',ls='-',c='g')

FOREST_stage['Q(L/s)'] = HEC_piecewise(FOREST_stage['stage_cm'])
FOREST_Q = FOREST_stage
fig, Q = plt.subplots(1,1)

Q.plot_date(LBJ_Q.index, LBJ_Q['Q(L/s)'],marker='None',ls='-',c='r')
Q.plot_date(FOREST_Q.index, FOREST_Q['Q(L/s)'],marker='None',ls='-',c='g')

Q.plot_date(LBJ_Q.index, LBJ_Q['Q(L/s)'],marker='None',ls='-',c='r')
LBJ_Q['Q(L/s)'] = LBJ_Q['Q(m3/s)'] * 1000
fig, Q = plt.subplots(1,1)

Q.plot_date(LBJ_Q.index, LBJ_Q['Q(L/s)'],marker='None',ls='-',c='r')
Q.plot_date(FOREST_Q.index, FOREST_Q['Q(L/s)'],marker='None',ls='-',c='g')
