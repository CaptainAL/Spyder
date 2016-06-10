for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = Solinst_data_parser(Barologger_path+f)
        raw = raw[['LEVEL','TEMPERATURE']]

raw
raw.columns  = ['Abs Pres, kPa','Temp, C']
raw
Barologger_path = maindir+'3-LBJ/LBJ-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = Solinst_data_parser(Barologger_path+f)
        raw = raw[['LEVEL','TEMPERATURE']]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

LBJ_Barologger_raw_data= Barologger_raw_data
LBJ_Barologger_raw_data['index'] = LBJ_Barologger_raw_data.index
LBJ_Barologger_raw_data = LBJ_Barologger_raw_data.drop_duplicates(cols='index')
LBJ_Barologger_raw_data = LBJ_Barologger_raw_data.reindex(pd.date_range(start2016,stop2016,freq='5Min'))
LBJ_Barologger_raw_data
LBJ_Barologger_raw_data.dropna()
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')
FOREST_Barologger_raw_data
FOREST_Barologger_raw_data.dropna()
FOREST_Barologger_raw_data.index
LBJ_Barologger_raw_data
LBJ_Barologger_raw_data.dropna()
FOREST_Barologger_raw_data['Abs Pres, kPa'].plot()
FOREST_Barologger_raw_data[dt.datetime(2016,2,6):]
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')

##---(Thu Jun 09 14:31:47 2016)---
PT_path = maindir+'3-LBJ/LBJ-PT/'
LBJ_PT_raw_data = pd.DataFrame()
for f in os.listdir(PT_path):
    if f.endswith('cm.csv') == True:
        print f
        raw = Solinst_data_parser(PT_path+f)
        raw = raw[['LEVEL','TEMPERATURE']]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        LBJ_PT_raw_data = LBJ_PT_raw_data.append(raw)

## CLEAN UP DATA          
LBJ_PT_raw_data = LBJ_PT_raw_data.sort_index()
LBJ_PT_raw_data['index'] = LBJ_PT_raw_data.index
LBJ_PT_raw_data = LBJ_PT_raw_data.drop_duplicates(cols = 'index')
LBJ_PT_raw_data
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')
PT_path = maindir+'3-LBJ/LBJ-PT/'
LBJ_PT_raw_data = pd.DataFrame()
for f in os.listdir(PT_path):
    if f.endswith('cm.csv') == True:
        print f
        raw = Solinst_data_parser(PT_path+f)
        raw = raw[['LEVEL','TEMPERATURE']]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        LBJ_PT_raw_data = LBJ_PT_raw_data.append(raw)

## CLEAN UP DATA          
LBJ_PT_raw_data = LBJ_PT_raw_data.sort_index()
LBJ_PT_raw_data['index'] = LBJ_PT_raw_data.index
LBJ_PT_raw_data = LBJ_PT_raw_data.drop_duplicates(cols = 'index')
LBJ_PT_raw_data
LBJ_PT_raw_data ['Abs Pres, kPa'] = LBJ_PT_raw_data ['Abs Pres, kPa']*0.0980665
LBJ_PT_raw_data

##---(Thu Jun 09 14:49:39 2016)---
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')

##---(Thu Jun 09 15:02:08 2016)---
runfile('C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016/Fagaalu-PT data process.py', wdir='C:/Users/atm19/Documents/GitHub/Fagaalu_monitoring/Fagaalu_Monitoring_2016')
QUARRY_R
QUARRY_RG
QUARRY_RG_path = maindir+'2-QUARRY/QUARRY-RAIN GAUGE/'
QUARRY_RG_raw_data = pd.DataFrame()
for f in os.listdir(QUARRY_RG_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(QUARRY_RG_path+f,header=1,parse_dates=1,index_col=1)
        raw = raw.ix[:,1:3]
        raw.columns  = ['Temp, C','Events']
        QUARRY_RG_raw_data = QUARRY_RG_raw_data.append(raw)

## CLEAN UP DATA       
QUARRY_RG_raw_data = QUARRY_RG_raw_data.sort_index()
QUARRY_RG_raw_data['index'] = QUARRY_RG_raw_data.index
QUARRY_RG = QUARRY_RG_raw_data.drop_duplicates(cols = 'index')
QUARRY_RG
QUARRY_RG_path = maindir+'2-QUARRY/QUARRY-RAIN GAUGE/'
QUARRY_RG_raw_data = pd.DataFrame()
for f in os.listdir(QUARRY_RG_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(QUARRY_RG_path+f,header=1,parse_dates=1,index_col=1)
        raw = raw.ix[:,1:3]
        raw.columns  = ['Temp, C','Events']
        QUARRY_RG_raw_data = QUARRY_RG_raw_data.append(raw)

## CLEAN UP DATA       
QUARRY_RG_raw_data = QUARRY_RG_raw_data.sort_index()
QUARRY_RG_raw_data['index'] = QUARRY_RG_raw_data.index
QUARRY_RG = QUARRY_RG_raw_data.drop_duplicates(cols = 'index')
## Resample cumulative events to 1 minute (eg. 16:00 to 16:01 has two events at 16:00:15 and 16:00:44 so 16:00=2; next event is at 16:02:13 so 16:01=2 and 16:02=3)
QUARRY_RG_1Min=pd.DataFrame()
QUARRY_RG_1Min['Events_Cum_1Min'] = QUARRY_RG['Events'].resample('1Min',how='last',fill_method='ffill')
QUARRY_RG_1Min['Events_Cum_15Min'] = QUARRY_RG['Events'].resample('15Min',how='last',fill_method='ffill')
## Subtract previous minutes events from the following minute (eg. cumulative events at 16:00=2, and at 16:02=3 so events for 16:02=1) 
QUARRY_RG_1Min['Events_1Min'] = QUARRY_RG_1Min['Events_Cum_1Min'] - QUARRY_RG_1Min['Events_Cum_1Min'] .shift(1).fillna(0) ## fillna(0) is for the very first value, it would be NaN when shifted down
QUARRY_RG_1Min['Events_15Min'] = QUARRY_RG_1Min['Events_Cum_15Min'].dropna() - QUARRY_RG_1Min['Events_Cum_15Min'].dropna().shift(1).fillna(0) ## fillna(0) is for the very first value, it would be NaN when shifted down
## Events to mm
QUARRY_RG_1Min['mm_1Min'] = QUARRY_RG_1Min['Events_1Min']*0.254 ##hundredths to mm
QUARRY_RG_1Min['mm_15Min'] = QUARRY_RG_1Min['Events_15Min']*0.254 ##hundredths to mm
## Reindex into a 15Min interval
QUARRY_RG = QUARRY_RG_1Min[['mm_15Min']].reindex(pd.date_range(start2016,stop2016,freq='15Min'))
QUARRY_RG