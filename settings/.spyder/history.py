# *** Spyder Python Console History Log ***
    def my_parser(x,y):
        try:
            y = str(int(y))
            hour=y[:-2]
            minute=y[-2:]
            time=dt.time(int(hour),int(minute))
        except:
            time=dt.time(0,0)
        parsed=dt.datetime.combine(x,time)
        return parsed
    Stage_Correction = Stage_Correction_XL.parse(location,parse_dates=False)
    Correction=pd.DataFrame()
    for correction in Stage_Correction.iterrows():
        t1_date = correction[1]['T1_date']
        t1_time = correction[1]['T1_time']
        t1 = my_parser(t1_date,t1_time)
        t2_date = correction[1]['T2_date']
        t2_time = correction[1]['T2_time']
        t2 = my_parser(t2_date,t2_time)
        z = correction[1]['z']    
        print t1,t2, z
        Correction = Correction.append(pd.DataFrame({'z':z},index=pd.date_range(t1,t2,freq='15Min')))
    Correction = Correction.reindex(pd.date_range(start2012,stop2014,freq='15Min'))
    PTdata['Manual_Correction'] = Correction['z']
    PTdata['stage_corrected_Manual'] = PTdata['Uncorrected_stage']+PTdata['Manual_Correction']
    PTdata['stage(cm)']=PTdata['stage_corrected_Manual'].where(PTdata['stage_corrected_Manual']>0,PTdata['stage(cm)'])#.round(0)
    return PTdata
Stage_Correction_XL = pd.ExcelFile(watershed_datadir+'Q/StageCorrection.xlsx')    
PT1 = correct_Stage_data(Stage_Correction_XL,'LBJ',PT1)
Fagaalu_stage_data = pd.DataFrame({'LBJ':PT1['stage(cm)']})
Fagaalu_stage_data = Fagaalu_stage_data.reindex(pd.date_range(start2012,stop2015,freq='15Min'))
import datetime as dt
start_time = dt.datetime.now()
print 'Start time: '+start_time.strftime('%H:%M:%S')
git=True
if git==True: ## Git repository
    maindir = 'C:/Users/atm19/Documents/GitHub/Fagaalu-Sediment-Flux/'
    datadir=maindir+'Data/'
    watershed_datadir= 'C:/Users/atm19/Documents/GitHub/Fagaalu-Sediment-Flux/Data/' 
    dataoutputdir = datadir+'Output/'
    GISdir = maindir+'Data/GIS/'
    figdir = maindir+'Figures/'
    tabledir = maindir+'Tables/'
    dirs={'main':maindir,'data':datadir,'GIS':GISdir,'fig':figdir}
elif git!=True: ## Local folders
    maindir = 'C:/Users/Alex/Desktop/'### samoa/
    csvoutputdir = datadir+'samoa/WATERSHED_ANALYSIS/FAGAALU/MasterDataFiles/csv_output/'
    savedir = datadir+'samoa/WATERSHED_ANALYSIS/GoodFigures/'
    figdir = datadir+'samoa/WATERSHED_ANALYSIS/GoodFigures/rawfigoutput/'
import os
import numpy as np
import pandas as pd
from scipy import stats
import pandas.stats.moments as m
from scipy.stats import pearsonr as pearson_r
from scipy.stats import spearmanr as spearman_r
import statsmodels.formula.api as smf
import statsmodels.stats.api
import rpy2.robjects as ro
import pandas.rpy.common as com
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')

##---(Wed May 25 10:14:34 2016)---
import statsmodels.api as sm
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
maindir = 'C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/'
datadir = maindir+'Data/'
watersheddir  = datadir+'Fagaalu_watershed/'
wavedir = datadir+'WW3_data/'
GISdir = datadir+'GIS/'
rawfig= maindir+'rawfig/'
figdir= maindir+'Figures/'
tabledir= maindir+'Tables/'
import statsmodels.api as sm
import statsmodels.formula.api as smf
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')

##---(Wed May 25 10:33:11 2016)---
import statsmodels.formula.api as smf
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
SedTubes
sed_acc='Total_gm2d'
data = SedTubes
for x, loc in enumerate(np.sort(data['Pod(P)/Tube(T)'].value_counts().index.values)):
    print x, loc
loc
reg_loc = data[data['Pod(P)/Tube(T)'] == loc][['Month',sed_acc,'SSY','Waves']]
reg_loc = reg_loc.dropna()
reg_loc
smf.ols(formula=sed_acc+" ~ SSY + Waves", data=reg_loc).fit()
smf.__version__
smf.__name__
smf.__package__
statsmodels.__version
import statsmodels
statsmodels.__version__

##---(Wed May 25 10:49:52 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
Tubes_Total= SedAcc_vs_SSY_Waves(SedTubes,'Total_gm2d',max_y=600,plot_health_thresholds=False,show=True,save=False,filename='')  

##---(Wed May 25 10:56:06 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')