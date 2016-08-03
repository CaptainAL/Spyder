# *** Spyder Python Console History Log ***
                y = '0'+y
            hour=y[:-2]
            minute=y[-2:]
            time=dt.time(int(hour),int(minute))
            parsed=dt.datetime.combine(x,time)
            #print parsed
            if parsed > fieldstart2014b:
                parsed = parsed + dt.timedelta(minutes=15)
            if round_to_5==True:
                parsed = misc_time.RoundTo5(parsed)
            if round_to_15==True:
                parsed = misc_time.RoundTo15(parsed)
            else:
                pass
        except:
            raise
            parsed = pd.to_datetime(pd.NaT)
        #print parsed
        return parsed
    
    SSC= SSCXL.parse(sheet,header=0,parse_dates=[['Date','Time']],date_parser=my_parser,index_col=['Date_Time'])
    SSC['NTU'], SSC['SSC (mg/L)'] = SSC['NTU'].round(0), SSC['SSC (mg/L)'].round(0)
    SSC = SSC[['Location','Sample #','NTU','SSC (mg/L)']]
    return SSC


## ALL SSC samples
SSC= loadSSC(pd.ExcelFile(datadir+'SSC/SSC_grab_samples.xlsx'),'ALL_MASTER',round_to_15=False)
SSC
SSC[SSC['Location']=='Upper Sed Pond']
SSC['Location'].unique
SSC['Location'].is_unique
SSC['Location'].unique()
SSC[SSC['Location']=='Quarry-Where quarry enters stream']
SSC[SSC['Location']=='Quarry-Lower Sediment Pond']
SSC[SSC['Location']=='Quarry-Lower Sed. Pond']
SSC[SSC['Location']=='Quarry-Upper Sed. Pond']
SSC[SSC['Location']=='Quarry-Upper Sediment Pond']
SSC[SSC['Location']=='Quarry-Upper Landing']
SSC[SSC['Location']=='DT']

##---(Tue Jul 26 13:07:45 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Load_SedPod_Tube_Data.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
SedPods
SedTubes[SedTubes == 'T1A']
SedTubes[SedTubes.ix['T1A']'
SedTubes.ix['T1A']
SedTubes.ix['T1A']['Fine Carb(gm2d)']
SedTubes.columns
SedTubes.ix['T1A']['Fine(%carb)']
SedTubes.ix['T2A']['Fine(%carb)']
SedTubes.ix['T2A']['Fine(%terr)']
SedTubes.ix['T2A']['Fine(%carb)']
SedTubes.ix['T2A']['Coarse(%carb)']
SedTubes.ix['T2A']['Fine(%carb)'].mean()
SedTubes.ix['T2A']['Coarse(%carb)'].mean()
SedTubes.ix[['T2A','T1A']]['Coarse(%carb)']
datadir
SedTubes.to_csv(datadir+'SedTubes.csv')
SedPods.to_csv(datadir+'SedPods.csv')
SedTubes.ix[['T2A','T2C','T1A','T1B','T1C']]['Total(%terr)']
SedTubes.ix[['T2A','T2C','T1A','T1B','T1C']]['Total(%terr)'].mean()
SedTubes.ix[['T2B','T3A','T3B','T3C']]['Total(%terr)'].mean()
north = ['T2A','T2C','T1A','T1B','T1C']
south = ['T2B','T3A','T3B','T3C']
SedTubes['Month'].is_unique()
SedTubes['Month'].drop_duplicates()
north_tubes = SedTubes.ix[north]
north_tubes
SedTubes['Month'].drop_duplicates()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['fine(%terr)'].mean()
north_tubes.columns
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%carb)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%carb)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%terr)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%terr)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%org)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%organic)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%carb)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%terr)'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%organic)'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%carb)'].mean()
south_tubes = SedTubes.ix[south]
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%carb)'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%terr)'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%org)'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Fine(%organic)'].mean()
44+31+9
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%carb)'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%terr)'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['Coarse(%organic)'].mean()
50+26+8
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['%coarse']
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['%coarse'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['%finee'].mean()
south_tubes[south_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['%fine'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['%coarse'].mean()
north_tubes[north_tubes['Month'].isin(['Oct_2014','Nov_2014','Dec_2014','Jan_2015','Feb_2015','Mar_2015'])]['%fine'].mean()
runfile('C:/Users/atm19/Documents/GitHub/Faga-alu-Bay-water-circulation/Code/PlotDrifters_Gridcell_ResidenceTime.py', wdir='C:/Users/atm19/Documents/GitHub/Faga-alu-Bay-water-circulation/Code')
__version__

##---(Wed Aug 03 13:08:26 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code/Plot_timeseries_terrig_v_P_and_SSY.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu-Sedimentation/Code')
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Code/Fagaalu-PT data process.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Code')