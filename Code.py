import pandas as pd;
df = pd.read_csv("./Data/PROBE-201901/20190101.csv.out", sep = ',' , names = ['VehicleID','gpsvalid','lat','lon','timestamp','speed','heading','for_hire_light','engine_acc'])

#a = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']

split_date = df['timestamp'].str.split(' ', expand = True)

df['date'] = split_date[0]
df['timeR'] = split_date[1]

#print(df.loc[(df['date'] == '2019-01-01') & (df['time'] == '00:00:00')])

#for i in a :
#    aq = df[df['timeR'].str.contains('^'+i)]
#    aaq = aq.loc[(df['date'] == '2019-01-01')]
#    aaq.to_csv("./Data/Hour/"+i+"-20190101.csv.out" ,index = False)

aq = df[df['timeR'].str.contains('^02')]
aaq = aq.loc[(df['date'] == '2019-01-01')]
aaq.to_csv("./Data/Hour/02-20190101.csv.out" ,index = False)


