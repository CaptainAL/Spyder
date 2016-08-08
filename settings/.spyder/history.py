    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['raw_stage_cm'],  c='r',ls='-',marker='None', alpha=0.6,)
# *** Spyder Python Console History Log ***
plot_stage()
fig, (ax1,ax2) = plt.subplots(2,1, figsize=(12,6))
ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['corrected_stage_cm'], c='g',ls='-', marker='None', label='FOREST 15Min')
ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['corrected_stage_cm'], c='m',ls='-', marker='None',label='FOREST 5Min')
ax1.legend(loc='upper left'), ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['raw_stage_cm'], c='r',ls='--',marker='None')
ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['raw_stage_cm'], c='b',ls='--', marker='None')
def plot_stage():
    fig, (ax1,ax2) = plt.subplots(2,1, figsize=(12,6))
    
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['corrected_stage_cm'], c='g',ls='-', marker='None', label='FOREST 15Min')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['corrected_stage_cm'], c='m',ls='-', marker='None',label='FOREST 5Min')
    ax1.legend(loc='upper left'), ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['raw_stage_cm'], c='r',ls='--',marker='None')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['raw_stage_cm'], c='b',ls='--', marker='None')
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['stage_cm'], c='b',ls='-', marker='None',label='LBJ 15Min')
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['stage_cm'],  c='r',ls='-',marker='None', label='LBJ 5Min')
    ax2.legend(loc='upper left'), ax2.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['raw_stage_cm'], c='b',ls='-', marker='None',alpha=0.6,
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['raw_stage_cm'],  c='r',ls='-',marker='None', alpha=0.6,)
    return
plot_stage()
def plot_stage():
    fig, (ax1,ax2) = plt.subplots(2,1, figsize=(12,6))
    
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['corrected_stage_cm'], c='g',ls='-', marker='None', label='FOREST 15Min')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['corrected_stage_cm'], c='m',ls='-', marker='None',label='FOREST 5Min')
    ax1.legend(loc='upper left'), ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['raw_stage_cm'], c='r',ls='--',marker='None')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['raw_stage_cm'], c='b',ls='--', marker='None')
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['stage_cm'], c='b',ls='-', marker='None',label='LBJ 15Min')
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['stage_cm'],  c='r',ls='-',marker='None', label='LBJ 5Min')
    ax2.legend(loc='upper left'), ax2.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['raw_stage_cm'], c='b',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['raw_stage_cm'],  c='r',ls='-',marker='None', alpha=0.6)
    return
plot_stage()
def plot_stage():
    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True, figsize=(12,6))
    
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['corrected_stage_cm'], c='g',ls='-', marker='None', label='FOREST 15Min')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['corrected_stage_cm'], c='m',ls='-', marker='None',label='FOREST 5Min')
    ax1.legend(loc='upper left'), ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['raw_stage_cm'], c='r',ls='-',marker='None',alpha=0.6)
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['raw_stage_cm'], c='b',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['stage_cm'], c='b',ls='-', marker='None',label='LBJ 15Min')
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['stage_cm'],  c='r',ls='-',marker='None', label='LBJ 5Min')
    ax2.legend(loc='upper left'), ax2.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['raw_stage_cm'], c='b',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['raw_stage_cm'],  c='r',ls='-',marker='None', alpha=0.6)
    return
plot_stage()
def plot_stage():
    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True, figsize=(12,6))
    
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['corrected_stage_cm'], c='g',ls='-', marker='None', label='FOREST 15Min')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['corrected_stage_cm'], c='g',ls='-', marker='None',label='FOREST 5Min')
    ax1.legend(loc='upper left'), ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['raw_stage_cm'], c='r',ls='-',marker='None',alpha=0.6)
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['raw_stage_cm'], c='r',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['stage_cm'], c='g',ls='-', marker='None',label='LBJ 15Min')
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['stage_cm'],  c='g',ls='-',marker='None', label='LBJ 5Min')
    ax2.legend(loc='upper left'), ax2.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['raw_stage_cm'], c='r',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['raw_stage_cm'],  c='r',ls='-',marker='None', alpha=0.6)
    return
plot_stage()
def plot_stage():
    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True, figsize=(12,6))
    
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['stage_cm'], c='g',ls='-', marker='None', label='FOREST 15Min')
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['stage_cm'], c='g',ls='-', marker='None',label='FOREST 5Min')
    ax1.legend(loc='upper left'), ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax1.plot_date(FOREST_Stage_15Min.index,FOREST_Stage_15Min['raw_stage_cm'], c='r',ls='-',marker='None',alpha=0.6)
    ax1.plot_date(FOREST_Stage_5Min.index, FOREST_Stage_5Min['raw_stage_cm'], c='r',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['stage_cm'], c='g',ls='-', marker='None',label='LBJ 15Min')
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['stage_cm'],  c='g',ls='-',marker='None', label='LBJ 5Min')
    ax2.legend(loc='upper left'), ax2.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
    ax2.plot_date(LBJ_Stage_15Min.index, LBJ_Stage_15Min['raw_stage_cm'], c='r',ls='-', marker='None',alpha=0.6)
    ax2.plot_date(LBJ_Stage_5Min.index, LBJ_Stage_5Min['raw_stage_cm'],  c='r',ls='-',marker='None', alpha=0.6)
    return
plot_stage()
FOREST_correction_list = [['02/09/2012 12:00','03/26/2012 15:00','-0.5'],
                          ['03/26/2012 15:15','08/17/2012 00:00','-0.5'],
                          ['02/25/2013 00:00','03/08/2013 13:15','-20'],
                          ['03/08/2013 13:30','03/28/2013 10:30','-17.5'],
                          ['03/28/2013 10:45','04/15/2013 16:00','-15'],
                          ['04/15/2013 16:15','04/30/2013 14:00','-16'],
                          ['04/30/2013 14:15','06/04/2013 15:15','-13'],
                          ['06/04/2013 15:30','06/26/2013 14:00','-12'],
                          ['06/26/2013 14:30','01/10/2015 11:15','6']] 
FOREST_correction_df = pd.DataFrame(FOREST_correction_list,columns=['T1_datetime','T2_datetime','zshift_cm'])
FOREST_Stage_15Min  = correct_Stage_data(FOREST_correction_df,FOREST_PT_15Min)
plot_stage(
)

##---(Fri Aug 05 15:47:51 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sediment-Flux/Code/SedFlux.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sediment-Flux/Code')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sediment-Flux/Code/Load_Sediment_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sediment-Flux/Code')