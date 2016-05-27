# *** Spyder Python Console History Log ***
    plt.subplots_adjust(left=0.05, right=0.90, top=0.95, bottom=0.08,hspace=0.1,wspace=0.01)
    
    return
def Sed_Time_Series_dots():
    study_start , study_end= dt.datetime(2014,3,1), dt.datetime(2015,4,30)
    
    SedPods_TS= pd.DataFrame(columns=['Precip',u'P1A', u'P1B', u'P1C', u'P2A', u'P2B', u'P2C', u'P3A', u'P3B', u'P3C'], index=pd.date_range(study_start,study_end,freq='15Min'))
    
    as_lines = True
    
    for col in SedPods_TS.columns:
        print col
        pod = SedPods[SedPods.index == col]
        for row in pod.iterrows():
            dep_start = row[1]['start']
            dep_end = row[1]['end'] - dt.timedelta(minutes = 15)
            if as_lines == False:
                SedPods_TS[col].ix[dep_start:dep_end] = row[1]['Total_gm2d'] 
                SedPods_TS['Precip'].ix[dep_start:dep_end] = row[1]['Precip']
            if as_lines == True:
                SedPods_TS[col].ix[dep_end] = row[1]['Total_gm2d'] 
                SedPods_TS['Precip'].ix[dep_end] = row[1]['Precip']
    
    if as_lines == True:            
        SedPods_TS = SedPods_TS.dropna()            
    
    fig, (precip, pods, tubes)  = plt.subplots(3,1,sharex = True,figsize=(11,7))
    SedPods_TS['Precip'].plot(ax=precip, c='b',ls='-')
    
    SedPods_TS['P1A'].plot(ax=pods, c='r',ls='None',marker='o',alpha=1)
    SedPods_TS['P1B'].plot(ax=pods, c='r',ls='None',marker='o',alpha=0.8)
    SedPods_TS['P1C'].plot(ax=pods, c='r',ls='None',marker='o',alpha=0.6)
    
    SedPods_TS['P2A'].plot(ax=pods, c='y',ls='None',marker='o',alpha=1)
    SedPods_TS['P2B'].plot(ax=pods, c='y',ls='None',marker='o',alpha=0.8)
    SedPods_TS['P2C'].plot(ax=pods, c='y',ls='None',marker='o',alpha=0.6)
    
    SedPods_TS['P3A'].plot(ax=pods, c='g',ls='None',marker='o',alpha=1)
    SedPods_TS['P3B'].plot(ax=pods, c='g',ls='None',marker='o',alpha=0.8)
    SedPods_TS['P3C'].plot(ax=pods, c='g',ls='None',marker='o',alpha=0.6)
    
    pods.legend(bbox_to_anchor=(1.12,1))
    
    SedTubes_TS= pd.DataFrame(columns=['Precip',u'T1A', u'T1B', u'T1C', u'T2A', u'T2B', u'T2C', u'T3A', u'T3B', u'T3C'], index=pd.date_range(study_start,study_end,freq='15Min'))
    
    for col in SedTubes_TS.columns:
        print col
        tube = SedTubes[SedTubes.index == col]
        for row in tube.iterrows():
            dep_start = row[1]['start']
            dep_end = row[1]['end'] - dt.timedelta(minutes = 15)
            if as_lines == False:
                SedTubes_TS[col].ix[dep_start:dep_end] = row[1]['Total_gm2d'] 
                SedTubes_TS['Precip'].ix[dep_end] = row[1]['Precip']
            if as_lines == True:
                SedTubes_TS[col].ix[dep_end] = row[1]['Total_gm2d'] 
                SedTubes_TS['Precip'].ix[dep_end] = row[1]['Precip']
    
    if as_lines == True:
        SedTubes_TS = SedTubes_TS.dropna()
    
    ax2 = fig.add_subplot()
    SedTubes_TS['T1A'].plot(ax=tubes, c='r',ls='None',marker='o',alpha=1)
    SedTubes_TS['T1B'].plot(ax=tubes, c='r',ls='None',marker='o',alpha=0.8)
    SedTubes_TS['T1C'].plot(ax=tubes, c='r',ls='None',marker='o',alpha=0.6)
    
    SedTubes_TS['T2A'].plot(ax=tubes, c='y',ls='None',marker='o',alpha=1)
    SedTubes_TS['T2B'].plot(ax=tubes, c='y',ls='None',marker='o',alpha=0.8)
    SedTubes_TS['T2C'].plot(ax=tubes, c='y',ls='None',marker='o',alpha=0.6)
    
    SedTubes_TS['T3A'].plot(ax=tubes, c='g',ls='None',marker='o',alpha=1)
    SedTubes_TS['T3B'].plot(ax=tubes, c='g',ls='None',marker='o',alpha=0.8)
    SedTubes_TS['T3C'].plot(ax=tubes, c='g',ls='None',marker='o',alpha=0.6)
    
    tubes.legend(bbox_to_anchor=(1.12,1))
    
    pods.grid(False,which='both')
    tubes.grid(False,which='both')
    plt.subplots_adjust(left=0.05, right=0.90, top=0.95, bottom=0.08,hspace=0.1,wspace=0.01)
    
    return
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', args='--i', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
import matplotlib
matplotlib.is_interactive()
plt.ioff()
"""
from matplotlib import pyplot as plt
"
""""
from matplotlib import pyplot as plt
plt.ioff()
matplotlib.is_interactive()
plt.ion()
matplotlib.is_interactive()
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', args='PYTHONINSPECT=x', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', args='PYTHONINSPECT=True', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Plot_timeseries_terrig_v_P_and_SSY.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
import matplotlib
matplotlib.use('Qt4Agg')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')