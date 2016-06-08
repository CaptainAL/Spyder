# *** Spyder Python Console History Log ***
# *** Spyder Python Console History Log ***
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

FOREST_Barologger_raw_data = Barologger_raw_data.drop_duplicates()
FOREST_Barologger_raw_data = FOREST_Barologger_raw_data.reindex(pd.date_range(start2016,stop2016,freq='5Min'))
Barologger_path = maindir+'1-FOREST/FOREST-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f

for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(Barologger_path+f,header=10,parse_dates=[[0,1]])
        raw = raw.ix[:,1:3]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

Barologger_path+f
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f

f
raw = pd.DataFrame.from_csv(Barologger_path+f,header=10,parse_dates=[[0,1]])
pd.DataFrame.from_csv(Barologger_path+f,header=10,parse_dates=[[0,1]])
Barologger_path = maindir+'1-FOREST/FOREST-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(Barologger_path+f,header=11,parse_dates=[[0,1]])
        raw = raw.ix[:,1:3]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

FOREST_Barologger_raw_data = Barologger_raw_data.drop_duplicates()
FOREST_Barologger_raw_data = FOREST_Barologger_raw_data.reindex(pd.date_range(start2016,stop2016,freq='5Min'))
FOREST_Barologger_raw_data
FOREST_Barologger_raw_data.dropna().tail()
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')
Barologger_path = maindir+'1-FOREST/FOREST-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(Barologger_path+f,header=11,parse_dates=[[0,1]])
        raw = raw.ix[:,1:3]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

FOREST_Barologger_raw_data = Barologger_raw_data.drop_duplicates()
FOREST_Barologger_raw_data = FOREST_Barologger_raw_data.reindex(pd.date_range(start2016,stop2016,freq='5Min'))
Barologger_path = maindir+'3-LBJ/LBJ-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f

for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(Barologger_path+f,header=10,parse_dates=[[0,1]])
        raw = raw.ix[:,1:3]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

Barologger_path = maindir+'3-LBJ/LBJ-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(Barologger_path+f,header=10,parse_dates=[[0,1]])
        raw = raw.ix[:,1:3]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

Barologger_raw_data
Barologger_raw_data.tail()
LBJ_Barologger_raw_data = Barologger_raw_data.drop_duplicates()
Barologger_raw_data.drop_duplicates()
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')
Barologger_path = maindir+'3-LBJ/LBJ-Barologger/'
Barologger_raw_data  = pd.DataFrame()
for f in os.listdir(Barologger_path):
    if f.endswith('.csv') == True:
        print f
        raw = pd.DataFrame.from_csv(Barologger_path+f,header=10,parse_dates=[[0,1]])
        raw = raw.ix[:,1:3]
        raw.columns  = ['Abs Pres, kPa','Temp, C']
        Barologger_raw_data = Barologger_raw_data.append(raw)

LBJ_Barologger_raw_data= Barologger_raw_data
LBJ_Barologger_raw_data['index'] = LBJ_Barologger_raw_data.index
LBJ_Barologger_raw_data = LBJ_Barologger_raw_data.drop_duplicates(cols='index')
LBJ_Barologger_raw_data = LBJ_Barologger_raw_data.reindex(pd.date_range(start2016,stop2016,freq='5Min'))
LBJ_Barologger_raw_data 
LBJ_Barologger_raw_data['Abs Pres, kPa'].plot()
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')

##---(Tue Jun 07 14:37:36 2016)---
FOREST_Barologger_raw_data 
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')

##---(Wed Jun 08 09:31:02 2016)---
runfile('C:/Users/atm19/Google Drive/Siumu-Fagaalu-PT data process.py', wdir='C:/Users/atm19/Google Drive')