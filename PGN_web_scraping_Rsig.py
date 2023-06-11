#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:58:23 2023

@author: prajjwal
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.ticker as ticker 
import datetime
import csv
from datetime import datetime as dt
from matplotlib.collections import PatchCollection
import urllib.request as urlrq
import certifi
import matplotlib as mpl
plt.rcParams['font.family']='Times New Roman'
import matplotlib as mpl
plt.style.use('classic')
plt.rc('figure',facecolor='w',figsize=(26,16))
#plt.subplot(1,4,1) 
fig, ax1 = plt.subplots()
plt.rcParams.update({'font.size': 22}) 
plt.subplots_adjust( wspace=0.14, hspace=0.12)
plt.rcParams['legend.numpoints'] = 1
mpl.rcParams['figure.dpi'] = 300
plt.rcParams['legend.numpoints'] = 1
plt.gca().tick_params(axis="y",direction="in", left="on",labelleft="on")
plt.gca().tick_params(axis="x",direction="in", left="on",labelleft="on")


date = input("Enter a date (YYYY-MM-DD): ")
from datetime import datetime, timedelta
old = datetime.strptime(date, "%Y-%m-%d")
new = old - timedelta(days=31)
new=new.strftime("%Y-%m-%d")

lat=input("Enter lat: "); lon=input("Enter lon: ")
lon1=float(lon)-0.10; lon2=float(lon)+0.10
lat1=float(lat)-0.10; lat2=float(lat)+0.10

plt.subplot(2,1,1)
url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rnvh3p1_8.tropospheric_nitrogen_dioxide&COMPRESS=0"  # Replace with the URL of the archive file


resp = urlrq.urlopen(url, cafile=certifi.where())

 

df = pd.read_csv(resp, sep='\t', encoding= 'unicode_escape')


yr, no2TC= np.squeeze(df.iloc[:, [0]].values), np.squeeze(df.iloc[:, [5]].values)
site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:21]
dt=[]

for i in range(len(yr)):

    # print (yr[i][0:10] , yr[i][11:17])

    dt.append(pd.to_datetime(yr[i][0:10] +" " + yr[i][11:19], format='%Y-%m-%d %H:%M:%S'))

array = {'datetime': dt,'no2': no2TC}

df3s = pd.DataFrame(array)

offset =1 *  float(lon) * 24 / 360 ##Aldine time
# print (offset)
frac, whole = np.modf(offset)
ndf1=pd.DatetimeIndex(df3s['datetime']) + pd.DateOffset(hours=whole,minutes=00)

array = {'datetime': ndf1,'no2': no2TC}
ndf3 = pd.DataFrame(array)


ndf4= ndf3.groupby([pd.Grouper(freq='H', key='datetime')]).mean().reset_index()

ndf5= ndf3.groupby([pd.Grouper(freq='H', key='datetime')]).std().reset_index()


plt.errorbar(ndf4['datetime'],ndf4['no2'],yerr=ndf5['no2'],color="k", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=4,alpha=0.8, label='Hourly')


legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})

# plt.xlabel("Date")
plt.ylim(0e16, 5e16)
plt.ylabel("NO2 Tr Column (molec/cm2)")

plt.setp(plt.gca().get_xticklabels(), visible=False)
# ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
plt.text(ndf4['datetime'][int(len(ndf4)-len(ndf4)/3)],4e16,str(site_name), fontweight='bold')

left, bottom, width, height = [0.25, 0.7, 0.3, 0.18]
ax2 = fig.add_axes([left, bottom, width, height])

#ax1.plot(range(10), color='red')
ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]
ax2.errorbar(nrt['datetime'],nrt['no2'],yerr=nrt1['no2'],color="r", marker='o',linestyle='dashed',markerfacecolor='r',linewidth=2.2,markerSize=8,alpha=0.9, label=str(date))
legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
hr_av=[];obs=[]; hr_std=[]
for i in range(6,19):
    ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
    obs.append(sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
    # print (sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
    hr_av.append(np.nanmean(ndf4.iloc[ix_loc].no2.values))
    hr_std.append(np.nanstd(ndf4.iloc[ix_loc].no2.values))
ax2.set_xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
plt.xticks(color='red', rotation=35, fontsize=16, fontweight='bold')
plt.yticks(color='red', rotation=0, fontsize=16, fontweight='bold')
plt.ylim(0e16, 2e16)
# plt.xlim(nrt.iloc[5].datetime, nrt.iloc[len(nrt)-1].datetime)
plt.ylabel("NO2 Tr Column")
plt.xlabel("Local Hours")

plt.twinx()
x_dt=np.array(pd.date_range(date+' 06:00',date+' 18:00',freq='H'))

if  ((sum(~np.isnan(hr_av))))==13:
    for xe in range(len(hr_av)):
        plt.scatter(x_dt[xe], hr_av[xe], marker= 'o', cmap='g', edgecolors='black', linewidths=7, alpha=0.75)
    
    #plt.annotate('K464E', (x[-2], y[22.8]))
    
    #for i, txt in enumerate('K464E', 'K472E', 'K464', 'M155E', 'K472', 'M155A', 'Q539A', 'M155R', 'D244A', 'E247A', 'E247R', 'D244K'):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        plt.ylim(0e16, 2e16)
else:
    
    ax2.errorbar(x_dt,hr_av,yerr=None,color="g", marker='o',linestyle='None',markerfacecolor='g',linewidth=2.2,markerSize=8,alpha=0.9, label=str(date))
# plt.ylim(0e16, 2e16)

plt.setp(plt.gca().get_xticklabels(), visible=False)


plt.subplot(2,1,2)
url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rfuh5p1_8.formaldehyde_tropospheric_vertical_column_amount&COMPRESS=0"  # Replace with the URL of the archive file


resp = urlrq.urlopen(url, cafile=certifi.where())

 

df = pd.read_csv(resp, sep='\t', encoding= 'unicode_escape')

yr, hchoTC= np.squeeze(df.iloc[:, [0]].values), np.squeeze(df.iloc[:, [5]].values)
site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:21]
dt=[]

for i in range(len(yr)):

    # print (yr[i][0:10] , yr[i][11:17])

    dt.append(pd.to_datetime(yr[i][0:10] +" " + yr[i][11:19], format='%Y-%m-%d %H:%M:%S'))

array = {'datetime': dt,'hcho': hchoTC}

df3s = pd.DataFrame(array)

ndf1=pd.DatetimeIndex(df3s['datetime']) + pd.DateOffset(hours=whole,minutes=00)

array = {'datetime': ndf1,'hcho': hchoTC}
ndf3 = pd.DataFrame(array)


ndf4= ndf3.groupby([pd.Grouper(freq='H', key='datetime')]).mean().reset_index()

ndf5= ndf3.groupby([pd.Grouper(freq='H', key='datetime')]).std().reset_index()



plt.errorbar(ndf4['datetime'],ndf4['hcho'],yerr=ndf5['hcho'],color="k", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=4,alpha=0.8, label='Hourly')


legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})

plt.xlabel("Date")
plt.ylim(0e16, 4e16)
plt.ylabel("HCHO Tr Column (molec/cm2)")
# ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
# plt.text(ndf4['datetime'][len(ndf4)-len(ndf4)/3],4e16,str(site_name), fontweight='bold')

left, bottom, width, height = [0.25, 0.27, 0.3, 0.18]
ax2 = fig.add_axes([left, bottom, width, height])

#ax1.plot(range(10), color='red')
ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]
ax2.errorbar(nrt['datetime'],nrt['hcho'],yerr=nrt1['hcho'],color="r", marker='o',linestyle='dashed',markerfacecolor='r',linewidth=2.2,markerSize=8,alpha=0.9, label=str(date))
legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
hr_av=[];obs=[]; hr_std=[]
for i in range(6,19):
    ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
    obs.append(sum(~np.isnan(ndf4.iloc[ix_loc].hcho.values)))
    hr_av.append(np.nanmean(ndf4.iloc[ix_loc].hcho.values))
    hr_std.append(np.nanstd(ndf4.iloc[ix_loc].hcho.values))
ax2.set_xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
plt.xticks(color='red', rotation=35, fontsize=16, fontweight='bold')
plt.yticks(color='red', rotation=0, fontsize=16, fontweight='bold')
plt.ylim(0e16, 2e16)
# plt.xlim(nrt.iloc[5].datetime, nrt.iloc[len(nrt)-1].datetime)
plt.ylabel("HCHO Tr Column")
plt.xlabel("Local Hours")

plt.twinx()
x_dt=np.array(pd.date_range(date+' 06:00',date+' 18:00',freq='H'))
if  ((sum(~np.isnan(hr_av))))==13:
    for xe in range(len(hr_av)):
        plt.scatter(x_dt[xe], hr_av[xe], marker= 'o', cmap='g', edgecolors='black', linewidths=7, alpha=0.75)
    
    #plt.annotate('K464E', (x[-2], y[22.8]))
    
    #for i, txt in enumerate('K464E', 'K472E', 'K464', 'M155E', 'K472', 'M155A', 'Q539A', 'M155R', 'D244A', 'E247A', 'E247R', 'D244K'):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        plt.ylim(0e16, 2e16)
else:
    
    ax2.errorbar(x_dt,hr_av,yerr=None,color="g", marker='o',linestyle='None',markerfacecolor='g',linewidth=2.2,markerSize=8,alpha=0.9, label=str(date))
# plt.ylim(0e16, 2e16)

plt.setp(plt.gca().get_xticklabels(), visible=False)

plt.show()
##"""
