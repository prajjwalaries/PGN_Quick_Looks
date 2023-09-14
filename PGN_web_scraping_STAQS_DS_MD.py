#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:33:48 2023

@author: prawat
"""



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.ticker as ticker 
import datetime
from urllib.error import HTTPError
import csv
from datetime import datetime as dt
from matplotlib.collections import PatchCollection
import urllib.request as urlrq
import certifi
import matplotlib as mpl
plt.rcParams['font.family']='Times New Roman'
import matplotlib as mpl
plt.style.use('classic')
plt.rc('figure',facecolor='w',figsize=(24,16))
#plt.subplot(1,4,1) 
fig, ax1 = plt.subplots()
plt.rcParams.update({'font.size': 18}) 
plt.subplots_adjust( wspace=0.06, hspace=0.15)
plt.rcParams['legend.numpoints'] = 1
mpl.rcParams['figure.dpi'] = 100
plt.rcParams['legend.numpoints'] = 1
plt.gca().tick_params(axis="y",direction="in", left="on",labelleft="on")
plt.gca().tick_params(axis="x",direction="in", left="on",labelleft="on")
plt.tight_layout()
plt.rc('xtick', labelsize=16) 
plt.rc('ytick', labelsize=18) 
import matplotlib.dates as mdates

date = input("Enter a date (YYYY-MM-DD): ")
from datetime import datetime, timedelta
old = datetime.strptime(date, "%Y-%m-%d")
new = old - timedelta(days=30)
new=new.strftime("%Y-%m-%d")

sitename=["ManhattanNY PGN# 135s1", 'BayonneNJ PGN# 38s1',  'BronxNY PGN# 180s1', 'WestportCT PGN# 177s1', 'KenoshaWI PGN# 167s1', 'QueensNY PGN# 140s1',  'WrightwoodCA PGN# 68s1', 'WhittierCA PGN# 247s1', 'OldFieldNY PGN# 51s1', 'NewBrunswickNJ PGN# 69s1', 'StGeorge  PGN# 109s1', 'Toronto-Scarborough PGN# 145s1', 'Toronto-West PGN# 108s1', 'Downsview PGN# 104s1', 'Philadelphia-PA PGN# 166s1', 'Bristol-PA PGN# 134s1', 'Chicago IL PGN# 249']
print ("1=ManhattanNY-CCNY, ", '2=BayonneNJ, ',  '3=BronxNY, ', '4=WestportCT, ', '5=KenoshaWI, ', '6=QueensNY, ',  '7=WrightwoodCA, ', '8=WhittierCA, ', '9=OldFieldNY, ', '10=NewBrunswickNJ, ', '11=StGeorge, ', '12=Toronto-Scarborough, ', '13=Toronto-West, ', '14=Downsview, ', '15=Philadelphia-PA, ', '16=Bristol-PA, ', '17=Chicago-IL')
location=[(40.8153, -73.9505), (40.6703, -74.1261), (40.8679, -73.8781), (41.1183, -73.3367), (42.5047, -87.8093), (40.73, -73.8215), (34.3819, -117.6813), (33.9768, -118.0299), (40.9635, -73.1402), (40.4622, -74.4294), (43.66, -79.3986),(43.7843, -79.1874), (43.7094, -79.5435), (43.7810, -79.4680), (39.9919, -75.0811), (40.1074,-74.8824), (41.9748, -87.7120) ]

ixd=int(input("Enter Location index: "))


lat=location[ixd-1][0]; lon=location[ixd-1][1]
lon1=float(lon)-0.04; lon2=float(lon)+0.04
lat1=float(lat)-0.04; lat2=float(lat)+0.04
print (location[ixd-1], lon1,lon2,lat1,lat2)

print ('Quality Control', '1=high', '2=medium')
QC=int(input("Quality Control: "))



plt.subplot(3,2,1)
df1=[]; df10=[];df=[];df0=[]
try:
   if QC ==1:
        url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rnvh3p1_8.tropospheric_nitrogen_dioxide&COMPRESS=0"  # Replace with the URL of the archive file
   else:
        url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rnvh3p1_8.tropospheric_nitrogen_dioxide&MINIMUM_QUALITY=medium"  # Replace with the URL of the archive file
   resp = urlrq.urlopen(url, cafile=certifi.where())
    
     
    
   df = pd.read_csv(resp, sep='\t', encoding= 'unicode_escape')
except HTTPError as e:
    content = e.read()
    print("No data found in  URL")

try:

   if QC ==1:
        url1 = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rnvs3p1_8.nitrogen_dioxide_vertical_column_amount&COMPRESS=0"  # Replace with the URL of the archive file
   else:
        url1 = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rnvs3p1_8.nitrogen_dioxide_vertical_column_amount&MINIMUM_QUALITY=medium"  # Replace with the URL of the archive file
    
    
    
   resp1 = urlrq.urlopen(url1, cafile=certifi.where())
    
     
    
   df1 = pd.read_csv(resp1, sep='\t', encoding= 'unicode_escape')

except HTTPError as e:
    content = e.read()
    print("No data found in URL")



print (len(df), len(df1))

if len(df)>0 and len(df1)==0:
    yr, no2TC= np.squeeze(df.iloc[:, [0]].values), np.squeeze(df.iloc[:, [5]].values)
    hx=np.where(no2TC>0)
    yr=yr[hx]; no2TC=no2TC[hx]
    site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:24]
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


    plt.errorbar(ndf4['datetime'],ndf4['no2'],yerr=ndf5['no2'],color="k", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markeredgecolor='k',markersize=6,alpha=0.8, label='Pandora MAX-DOAS')
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    
    # plt.xlabel("Date")
    plt.ylim(0e16, 5e16)
    plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
    plt.ylabel("NO2 column (molec/cm2)")
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    # ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
    
    plt.text(np.datetime64(new+' 23:00'),4.5e16,'(a)', fontweight='bold', fontsize=22)
    
    
    
    #####Diurnal
    plt.subplot(3,2,2)
    #ax1.plot(range(10), color='red')
    ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
    nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]

    ix_all=ndf3[ndf3.datetime.dt.normalize() == date].index.values
    ndf4all= ndf3.iloc[ix_all]
    
    plt.scatter(ndf4all['datetime'],ndf4all['no2'], marker= 'o', facecolors='coral', edgecolors='r', linewidths=3.5, alpha=0.7, label='MAX-DOAS_'+str(date))
    
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    # plt.text(np.datetime64(date+' 08:00'), 1.7e16,'30 Days Average', fontsize=18, color='k',fontweight='bold')
    plt.ylim(0e16, 3e16)
    plt.text(np.datetime64(date+' 07:00'),2.5e16,'(d)', fontweight='bold', fontsize=22)
    
    ####Hourly Average
    
    hr_av=[];obs=[]; hr_std=[]
    for i in range(6,19):
        ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_loc)).size)>1:
            ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
            obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
            # print (sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
            hr_av.append(np.nanmean(ndf4.iloc[ix_loc].no2.values))
        else:
            hr_av.append((ndf4.iloc[ix_loc].no2))
            obs.append((np.array(ix_loc)).size)

     
    x_dt=np.array(pd.date_range(date+' 06:00',date+' 18:00',freq='H'))
    
    hr_av1=[]; hr_avd1=[]
    for xe in range(len(hr_av)):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        plt.ylim(0e16, 3e16)
        # plt.setp(plt.gca().get_yticklabels(), visible=False)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
        hr_av1.append(hr_av[xe])  
    
    plt.errorbar(x_dt, hr_av1, color="k", marker='o',linestyle='solid',markerfacecolor='w', markeredgecolor='k',linewidth=2.2,markersize=14,markeredgewidth=6.0, alpha=0.8, label=' MAX-DOAS Average')
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.ylim(0e16, 3e16)
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    
    

if len(df)==0 and len(df1)>0:
    
    yr, no2TC= np.squeeze(df1.iloc[:, [0]].values), np.squeeze(df1.iloc[:, [5]].values)
    hx=np.where(no2TC>0)
    yr=yr[hx]; no2TC=no2TC[hx]
    site_name=np.squeeze(df1.iloc[:, [6]].values)[0][0:24]
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


    plt.errorbar(ndf4['datetime'],ndf4['no2'],yerr=ndf5['no2'],color="b", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markeredgecolor='b',markersize=6,alpha=0.8, label='Pandora Direct Sun')
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    
    # plt.xlabel("Date")
    plt.ylim(0e16, 5e16)
    plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
    plt.ylabel("NO2 column (molec/cm2)")
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    # ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
    
    plt.text(np.datetime64(new+' 23:00'),4.5e16,'(a)', fontweight='bold', fontsize=22)
    
    
    
    #####Diurnal
    plt.subplot(3,2,2)
    #ax1.plot(range(10), color='red')
    ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
    nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]

    ix_all=ndf3[ndf3.datetime.dt.normalize() == date].index.values
    ndf4all= ndf3.iloc[ix_all]
    
    plt.scatter(ndf4all['datetime'],ndf4all['no2'], marker= 'o', facecolors='g', edgecolors='g', linewidths=3.5, alpha=0.7, label='Direct Sun_'+str(date))
    
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    # plt.text(np.datetime64(date+' 08:00'), 1.7e16,'30 Days Average', fontsize=18, color='k',fontweight='bold')
    plt.ylim(0e16, 3e16)
    plt.text(np.datetime64(date+' 07:00'),2.5e16,'(d)', fontweight='bold', fontsize=22)
    
    ####Hourly Average
    
    hr_av=[];obs=[]; hr_std=[]
    for i in range(6,19):
        ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_loc)).size)>1:
            ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
            obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
            # print (sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
            hr_av.append(np.nanmean(ndf4.iloc[ix_loc].no2.values))
        else:
            hr_av.append((ndf4.iloc[ix_loc].no2))
            obs.append((np.array(ix_loc)).size)

     
    x_dt=np.array(pd.date_range(date+' 06:00',date+' 18:00',freq='H'))
    
    hr_av1=[]; hr_avd1=[]
    for xe in range(len(hr_av)):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        plt.ylim(0e16, 3e16)
        # plt.setp(plt.gca().get_yticklabels(), visible=False)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
        hr_av1.append(hr_av[xe])  
    
    plt.errorbar(x_dt, hr_av1, color="b", marker='o',linestyle='solid',markerfacecolor='w', markeredgecolor='b',linewidth=2.2,markersize=14,markeredgewidth=6.0, alpha=0.8, label=' Direct Sun Average')
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.ylim(0e16, 3e16)
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    
    
    
    
if len(df)>0 and len(df1)>0:


    ###MAX-DOAS
    
    yr, no2TC= np.squeeze(df.iloc[:, [0]].values), np.squeeze(df.iloc[:, [5]].values)
    hx=np.where(no2TC>0)
    yr=yr[hx]; no2TC=no2TC[hx]
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
    
    
    ####Direct Sun
    
    yrd, no2TCd= np.squeeze(df1.iloc[:, [0]].values), np.squeeze(df1.iloc[:, [5]].values)
    hxd=np.where(no2TCd>0)
    yrd=yrd[hxd]; no2TCd=no2TCd[hxd]
    # site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:22]
    dtd=[]
    
    for i in range(len(yrd)):
    
        # print (yr[i][0:10] , yr[i][11:17])
    
        dtd.append(pd.to_datetime(yrd[i][0:10] +" " + yrd[i][11:19], format='%Y-%m-%d %H:%M:%S'))
    
    array = {'datetime': dtd,'no2': no2TCd}
    
    df3sd = pd.DataFrame(array)
    
    offset =1 *  float(lon) * 24 / 360 ##Aldine time
    # print (offset)
    frac, whole = np.modf(offset)
    ndf1d=pd.DatetimeIndex(df3sd['datetime']) + pd.DateOffset(hours=whole,minutes=00)
    
    array = {'datetime': ndf1d,'no2': no2TCd}
    ndf3d = pd.DataFrame(array)
    
    
    ndf4d= ndf3d.groupby([pd.Grouper(freq='H', key='datetime')]).mean().reset_index()
    
    ndf5d= ndf3d.groupby([pd.Grouper(freq='H', key='datetime')]).std().reset_index()
    
    
    
    #####Plotting
    
    plt.errorbar(ndf4['datetime'],ndf4['no2'],yerr=ndf5['no2'],color="k", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markeredgecolor='k',markersize=6,alpha=0.8, label='Pandora MAX-DOAS')
    
    plt.errorbar(ndf4d['datetime'],ndf4d['no2'],yerr=ndf5d['no2'],color="b", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=6,markeredgecolor='b',alpha=0.8, label='Pandora Direct Sun')
    
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    
    # plt.xlabel("Date")
    plt.ylim(0e16, 5e16)
    plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
    plt.ylabel("NO2 column (molec/cm2)")
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    # ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
    
    plt.text(np.datetime64(new+' 23:00'),4.5e16,'(a)', fontweight='bold', fontsize=22)
    
    
    
    #####Diurnal
    plt.subplot(3,2,2)
    #ax1.plot(range(10), color='red')
    ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
    nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]
    
    ###Direct Sun
    ix_nrtd=ndf4d[ndf4d.datetime.dt.normalize() == date].index.values
    nrtd=ndf4d.iloc[ix_nrtd]; nrt1d=ndf5d.iloc[ix_nrtd]
    
    
    ix_all=ndf3[ndf3.datetime.dt.normalize() == date].index.values
    ndf4all= ndf3.iloc[ix_all]
    
    plt.scatter(ndf4all['datetime'],ndf4all['no2'], marker= 'o', facecolors='r', edgecolors='r', linewidths=3.5, alpha=0.7, label='MAX-DOAS_'+str(date))
    ##DS
    ix_alld=ndf3d[ndf3d.datetime.dt.normalize() == date].index.values
    ndf4alld= ndf3d.iloc[ix_alld]
    
    # plt.errorbar(nrtd['datetime'],nrtd['no2'],yerr=nrt1d['no2'],color="g", marker='o',linestyle='dashed',markerfacecolor='r',linewidth=2.2,markersize=8,alpha=0.9, label=str(date))
    
    
    plt.scatter(ndf4alld['datetime'],ndf4alld['no2'], marker= 'o', facecolors='g', edgecolors='g', linewidths=3.5, alpha=0.7, label='Direct Sun_'+str(date))
    
    
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    # plt.text(np.datetime64(date+' 08:00'), 1.7e16,'30 Days Average', fontsize=18, color='k',fontweight='bold')
    plt.ylim(0e16, 3e16)
    plt.text(np.datetime64(date+' 07:00'),2.5e16,'(d)', fontweight='bold', fontsize=22)
    
    ####Hourly Average
    
    hr_av=[];obs=[]; hr_std=[]
    for i in range(6,19):
        ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_loc)).size)>1:

            obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
            # print (sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
            hr_av.append(np.nanmean(ndf4.iloc[ix_loc].no2.values))
        else:
            hr_av.append((ndf4.iloc[ix_loc].no2))
            obs.append((np.array(ix_loc)).size)
          
    ####DS
    hr_avd=[];obsd=[]; hr_stdd=[] 
    for i in range(6,19):
        
        ix_locd=(np.squeeze(ndf4d[ndf4d.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_locd)).size)>1:
            obsd.append(((ndf4d.iloc[ix_locd]).dropna()).shape[0])
            # print (sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
            hr_avd.append(np.nanmean(ndf4d.iloc[ix_locd].no2.values))
        else:
            hr_avd.append((ndf4d.iloc[ix_locd].no2))
            obsd.append((np.array(ix_locd)).size)
     
    x_dt=np.array(pd.date_range(date+' 06:00',date+' 18:00',freq='H'))
    
    hr_av1=[]; hr_avd1=[]
    
    for xe in range(len(hr_av)):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        
        ####DS
        plt.annotate(obsd[xe], (x_dt[xe], hr_avd[xe]+5e14))
        plt.ylim(0e16, 3e16)
        # plt.setp(plt.gca().get_yticklabels(), visible=False)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
        hr_av1.append(hr_av[xe]); hr_avd1.append(hr_avd[xe])
    
    plt.errorbar(x_dt, hr_av1, color="k", marker='o',linestyle='solid',markerfacecolor='w', markeredgecolor='k',linewidth=2.2,markersize=14,markeredgewidth=6.0, alpha=0.8, label=' MAX-DOAS Average')
    plt.errorbar(x_dt, hr_avd1,color="b", marker='o',linestyle='solid',markerfacecolor='w',markeredgecolor='b',linewidth=2.2,markersize=14,markeredgewidth=6.0,alpha=0.8, label='Direct Sun Average')
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.ylim(0e16, 3e16)
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    


plt.subplot(3,2,3)

try:
    if QC==1:
        url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rfuh5p1_8.formaldehyde_tropospheric_vertical_column_amount&COMPRESS=0"  # Replace with the URL of the archive file
    
    else:
        url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rfuh5p1_8.formaldehyde_tropospheric_vertical_column_amount&MINIMUM_QUALITY=medium"  # Replace with the URL of the archive file
    resp = urlrq.urlopen(url, cafile=certifi.where())
    
     
    
    df0 = pd.read_csv(resp, sep='\t', encoding= 'unicode_escape')
except HTTPError as e:
    content = e.read()
    print("No data found in URL")

try:
    if QC ==1:
        url1 = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rfus5p1_8.formaldehyde_total_vertical_column_amount&COMPRESS=0"  # Replace with the URL of the archive file
    else:
        url1 = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&FORMAT=ascii&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1)+","+str(lat1)+","+str(lon2)+","+str(lat2)+"&COVERAGE=pandora.L2_rfus5p1_8.formaldehyde_total_vertical_column_amount&MINIMUM_QUALITY=medium"  # Replace with the URL of the archive file
    
    
    
    resp1 = urlrq.urlopen(url1, cafile=certifi.where())

     
    
    df10 = pd.read_csv(resp1, sep='\t', encoding= 'unicode_escape')

except HTTPError as e:
    content = e.read()
    print("No data found in URL")


print (len(df0), len(df10))

if len(df0)>0 and len(df10)==0:

    yr, hchoTC= np.squeeze(df0.iloc[:, [0]].values), np.squeeze(df0.iloc[:, [5]].values)
    hy=np.where(hchoTC>0)
    yr=yr[hy]; hchoTC=hchoTC[hy]
    # site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:24]
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
    
    
    plt.errorbar(ndf4['datetime'],ndf4['hcho'],yerr=ndf5['hcho'],color="k", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=6,markeredgecolor='k',alpha=0.8, label='Pandora MAX-DOAS')
    
    
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    
    # plt.xlabel("Date")
    plt.ylim(0e16, 4e16)
    plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
    plt.ylabel("HCHO column (molec/cm2)")
    # ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
    # plt.text(ndf4['datetime'][len(ndf4)-len(ndf4)/3],4e16,str(site_name), fontweight='bold')
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    plt.text(np.datetime64(new+' 23:00'),3.5e16,'(b)', fontweight='bold', fontsize=22)
    
    plt.subplot(3,2,4)
    #ax1.plot(range(10), color='red')
    ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
    nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    ix_all=ndf3[ndf3.datetime.dt.normalize() == date].index.values
    ndf4all= ndf3.iloc[ix_all]
    
    plt.scatter(ndf4all['datetime'],ndf4all['hcho'], marker= 'o', facecolors='r', edgecolors='r', linewidths=3.5, alpha=0.7, label='MAX-DOAS_'+str(date))
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    
    
        
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    plt.ylim(0e16, 3e16)
    plt.text(np.datetime64(date+' 07:00'),2.5e16,'(e)', fontweight='bold', fontsize=22)
    
    
    hr_av=[];obs=[]; hr_std=[]
    for i in range(6,19):
        ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_loc)).size)>1:
            obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
            hr_av.append(np.nanmean(ndf4.iloc[ix_loc].hcho.values))
        else:
            hr_av.append((ndf4.iloc[ix_loc].hcho))
            obs.append((np.array(ix_loc)).size)

         
    hr_av1=[]; hr_avd1=[]
    for xe in range(len(hr_av)):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        
        plt.ylim(0e16, 3e16)
        # plt.setp(plt.gca().get_yticklabels(), visible=False)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
        hr_av1.append(hr_av[xe])
    plt.errorbar(x_dt, hr_av1, color="k", marker='o',linestyle='solid',markerfacecolor='w', markeredgecolor='k',linewidth=2.2,markersize=14,markeredgewidth=6.0, alpha=0.8, label=' MAX-DOAS Average')
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.ylim(0e16, 3e16)
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)

if len(df0)==0 and len(df10)>0:

    yr, hchoTC= np.squeeze(df10.iloc[:, [0]].values), np.squeeze(df10.iloc[:, [5]].values)
    hy=np.where(hchoTC>0)
    yr=yr[hy]; hchoTC=hchoTC[hy]
    # site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:24]
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
    
    
    plt.errorbar(ndf4['datetime'],ndf4['hcho'],yerr=ndf5['hcho'],color="b", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=6,markeredgecolor='b',alpha=0.8, label='Pandora Direct Sun')
    
    
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    
    # plt.xlabel("Date")
    plt.ylim(0e16, 4e16)
    plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
    plt.ylabel("HCHO column (molec/cm2)")
    # ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
    # plt.text(ndf4['datetime'][len(ndf4)-len(ndf4)/3],4e16,str(site_name), fontweight='bold')
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    plt.text(np.datetime64(new+' 23:00'),3.5e16,'(b)', fontweight='bold', fontsize=22)
    
    plt.subplot(3,2,4)
    #ax1.plot(range(10), color='red')
    ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
    nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    ix_all=ndf3[ndf3.datetime.dt.normalize() == date].index.values
    ndf4all= ndf3.iloc[ix_all]
    
    plt.scatter(ndf4all['datetime'],ndf4all['hcho'], marker= 'o', facecolors='g', edgecolors='g', linewidths=3.5, alpha=0.7, label='Direct Sun_'+str(date))
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    
    
        
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    plt.ylim(0e16, 3e16)
    plt.text(np.datetime64(date+' 07:00'),2.5e16,'(e)', fontweight='bold', fontsize=22)
    
    
    hr_av=[];obs=[]; hr_std=[]
    for i in range(6,19):
        ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_loc)).size)>1:
            obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
            hr_av.append(np.nanmean(ndf4.iloc[ix_loc].hcho.values))
        else:
            hr_av.append((ndf4.iloc[ix_loc].hcho))
            obs.append((np.array(ix_loc)).size)

         
    hr_av1=[]; hr_avd1=[]
    for xe in range(len(hr_av)):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        
        plt.ylim(0e16, 3e16)
        # plt.setp(plt.gca().get_yticklabels(), visible=False)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
        hr_av1.append(hr_av[xe])
    plt.errorbar(x_dt, hr_av1, color="b", marker='o',linestyle='solid',markerfacecolor='w', markeredgecolor='b',linewidth=2.2,markersize=14,markeredgewidth=6.0, alpha=0.8, label=' Direct Sun Average')
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.ylim(0e16, 3e16)
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)



if len(df0)>0 and len(df10)>0:

    yr, hchoTC= np.squeeze(df0.iloc[:, [0]].values), np.squeeze(df0.iloc[:, [5]].values)
    hy=np.where(hchoTC>0)
    yr=yr[hy]; hchoTC=hchoTC[hy]
    # site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:24]
    dt=[]
    
    for i in range(len(yr)):
    
        # print (yr[i][0:10] , yr[i][11:17])
    
        dt.append(pd.to_datetime(yr[i][0:10] +" " + yr[i][11:19], format='%Y-%m-%d %H:%M:%S'))
    
    array = {'datetime': dt,'hcho': hchoTC}
    
    df3s = pd.DataFrame(array)
    
    ndf1=pd.DatetimeIndex(df3s['datetime']) + pd.DateOffset(hours=whole,minutes=00)
    
    array = {'datetime': ndf1,'hcho': hchoTC}
    ndf3 = pd.DataFrame(array)
    ndf01=ndf3
    
    ndf4= ndf3.groupby([pd.Grouper(freq='H', key='datetime')]).mean().reset_index()
    
    ndf5= ndf3.groupby([pd.Grouper(freq='H', key='datetime')]).std().reset_index()
    
    
    ###Direct Sun
    
    yrd, hchoTCd= np.squeeze(df10.iloc[:, [0]].values), np.squeeze(df10.iloc[:, [5]].values)
    hxd=np.where(hchoTCd>0)
    yrd=yrd[hxd]; hchoTCd=hchoTCd[hxd]
    # site_name=np.squeeze(df.iloc[:, [6]].values)[0][0:22]
    dtd=[]
    
    for i in range(len(yrd)):
    
        # print (yr[i][0:10] , yr[i][11:17])
    
        dtd.append(pd.to_datetime(yrd[i][0:10] +" " + yrd[i][11:19], format='%Y-%m-%d %H:%M:%S'))
    
    array = {'datetime': dtd,'hcho': hchoTCd}
    
    df3sd = pd.DataFrame(array)
    
    offset =1 *  float(lon) * 24 / 360 ##Aldine time
    # print (offset)
    frac, whole = np.modf(offset)
    ndf1d=pd.DatetimeIndex(df3sd['datetime']) + pd.DateOffset(hours=whole,minutes=00)
    
    array = {'datetime': ndf1d,'hcho': hchoTCd}
    ndf3d = pd.DataFrame(array)
    
    
    ndf4d= ndf3d.groupby([pd.Grouper(freq='H', key='datetime')]).mean().reset_index()
    
    ndf5d= ndf3d.groupby([pd.Grouper(freq='H', key='datetime')]).std().reset_index()
    
    
    
    
    
    plt.errorbar(ndf4['datetime'],ndf4['hcho'],yerr=ndf5['hcho'],color="k", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=6,markeredgecolor='k',alpha=0.8, label='Pandora MAX-DOAS')
    
    plt.errorbar(ndf4d['datetime'],ndf4d['hcho'],yerr=ndf5d['hcho'],color="b", marker='o',linestyle='dashed',markerfacecolor='gray',linewidth=1.2,markersize=6,markeredgecolor='b',alpha=0.8, label='Pandora Direct Sun')
    
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    
    # plt.xlabel("Date")
    plt.ylim(0e16, 4e16)
    plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
    plt.ylabel("HCHO column (molec/cm2)")
    # ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
    # plt.text(ndf4['datetime'][len(ndf4)-len(ndf4)/3],4e16,str(site_name), fontweight='bold')
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    plt.text(np.datetime64(new+' 23:00'),3.5e16,'(b)', fontweight='bold', fontsize=22)
    
    plt.subplot(3,2,4)
    #ax1.plot(range(10), color='red')
    ix_nrt=ndf4[ndf4.datetime.dt.normalize() == date].index.values
    nrt=ndf4.iloc[ix_nrt]; nrt1=ndf5.iloc[ix_nrt]
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    ix_all=ndf3[ndf3.datetime.dt.normalize() == date].index.values
    ndf4all= ndf3.iloc[ix_all]
    
    plt.scatter(ndf4all['datetime'],ndf4all['hcho'], marker= 'o', facecolors='r', edgecolors='r', linewidths=3.5, alpha=0.7, label='MAX-DOAS_'+str(date))
    
    ###DS
    ix_nrtd=ndf4d[ndf4d.datetime.dt.normalize() == date].index.values
    nrtd=ndf4d.iloc[ix_nrtd]; nrt1d=ndf5d.iloc[ix_nrtd]
    
    ix_alld=ndf3d[ndf3d.datetime.dt.normalize() == date].index.values
    ndf4alld= ndf3d.iloc[ix_alld]
    
    plt.scatter(ndf4alld['datetime'],ndf4alld['hcho'], marker= 'o', facecolors='g', edgecolors='g', linewidths=3.5, alpha=0.7, label='Direct Sun_'+str(date))
    
    
    
    legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    
    
        
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    
    plt.ylim(0e16, 3e16)
    plt.text(np.datetime64(date+' 07:00'),2.5e16,'(e)', fontweight='bold', fontsize=22)
    
    
    hr_av=[];obs=[]; hr_std=[]
    for i in range(6,19):
        ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
        if ((np.array(ix_loc)).size)>1:
            obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
            hr_av.append(np.nanmean(ndf4.iloc[ix_loc].hcho.values))
        else:
            hr_av.append((ndf4.iloc[ix_loc].hcho))
            obs.append((np.array(ix_loc)).size)
     
    ###DS
    hr_avd=[];obsd=[]; hr_stdd=[]
    for i in range(6,19):
        ix_locd=(np.squeeze(ndf4d[ndf4d.datetime.dt.hour.values==i].index.values))
        x00=(ndf4d.iloc[ix_locd]).shape[0]
        # print (i,ndf4d.iloc[ix_locd],(np.array(ix_locd)).size)
        if ((np.array(ix_locd)).size)>1:
            obsd.append(((ndf4d.iloc[ix_locd]).dropna()).shape[0])
            x00=(ndf4d.iloc[ix_locd]).shape[0]
            hr_avd.append(np.nanmean(ndf4d.iloc[ix_locd].hcho.values))
        else:
            hr_avd.append((ndf4d.iloc[ix_locd].hcho))
            obsd.append((np.array(ix_locd)).size)
     
    
    
    hr_av1=[]; hr_avd1=[]
    for xe in range(len(hr_av)):
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5e14))
        
        ####DS
        plt.annotate(obsd[xe], (x_dt[xe], hr_avd[xe]+5e14))
        plt.ylim(0e16, 3e16)
        # plt.setp(plt.gca().get_yticklabels(), visible=False)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
        hr_av1.append(hr_av[xe]); hr_avd1.append(hr_avd[xe])
    
    plt.errorbar(x_dt, hr_av1, color="k", marker='o',linestyle='solid',markerfacecolor='w', markeredgecolor='k',linewidth=2.2,markersize=14,markeredgewidth=6.0, alpha=0.8, label=' MAX-DOAS Average')
    plt.errorbar(x_dt, hr_avd1,color="b", marker='o',linestyle='solid',markerfacecolor='w',markeredgecolor='b',linewidth=2.2,markersize=14,markeredgewidth=6.0,alpha=0.8, label='Direct Sun Average')
    legend=plt.legend(loc="upper right", ncol=2, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22},labelcolor='linecolor')
    
    plt.ylim(0e16, 3e16)
    # plt.setp(plt.gca().get_yticklabels(), visible=False)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
    
    plt.setp(plt.gca().get_xticklabels(), visible=False)

# PM25:::::::::https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&COVERAGE=airnow.pm25&TIME=2022-07-01T00:00:00Z/2022-07-07T23:59:59Z&BBOX=-77.29000,37.250000,-77.110000,37.400000&FORMAT=ascii
###Ozone
url = "https://ofmpub.epa.gov/rsig/rsigserver?SERVICE=wcs&VERSION=1.0.0&REQUEST=GetCoverage&COVERAGE=airnow.ozone&TIME="+str(new)+"T00:00:00Z/"+date+"T23:59:59Z&BBOX="+str(lon1-0.06)+","+str(lat1-0.06)+","+str(lon2+0.06)+","+str(lat2+0.06)+"&FORMAT=ascii"  # Replace with the URL of the archive file


resp = urlrq.urlopen(url, cafile=certifi.where())

dfo = pd.read_csv(resp, sep='\t', encoding= 'unicode_escape')



yr, lato, lono,oz, site_id= np.squeeze(dfo.iloc[:, [0]].values), np.squeeze(dfo.iloc[:, [2]].values),np.squeeze(dfo.iloc[:, [1]].values),np.squeeze(dfo.iloc[:, [4]].values),np.squeeze(dfo.iloc[:, [5]].values)
# site_name=np.squeeze(df.iloc[:, [5]].values)

i1=np.where((oz>=0) &  (oz<=500))
yr, lato, lono,oz, site_id=yr[i1], lato[i1], lono[i1],oz[i1], site_id[i1] 
dt=[]
for i in range(len(yr)):

    # print (yr[i][0:10] , yr[i][11:17])

    dt.append(pd.to_datetime(yr[i][0:10] +" " + yr[i][11:19], format='%Y-%m-%d %H:%M:%S'))

array = {'datetime': dt,'ozone': oz}

df3s = pd.DataFrame(array)
offset =1 *  float(lon) * 24 / 360 ##Aldine time
# print (offset)
frac, whole = np.modf(offset)
ndf1=pd.DatetimeIndex(df3s['datetime']) + pd.DateOffset(hours=whole,minutes=00)

array = {'datetime': ndf1,'ozone': oz, 'lat': lato, 'lon': lono, 'site':site_id }
ndf3 = pd.DataFrame(array)
ndf3= ndf3[(ndf3['datetime'].dt.hour >= 6) & (ndf3['datetime'].dt.hour <= 18)]

dfs,nm_d = {},[]

for frame, data in ndf3.groupby('site'):
    dfs[f'{frame}'] = data
    nm_d.append(frame)

from math import sin, cos, sqrt, atan2, radians  
dst,ist=[],[]
for st in range(0,len(dfs)):
    if st>6:
        continue
    lat11 = radians(float(lat))
    lon11 = radians(float(lon))
    lat21 = radians(dfs[str(nm_d[st])]['lat'].iloc[0])
    lon21 = radians(dfs[str(nm_d[st])]['lon'].iloc[0])
    
    dlon = lon21 - lon11
    dlat = lat21 - lat11
    R = 6373.0
    a = np.sin(dlat / 2)**2 + np.cos(lat11) * np.cos(lat21) * np.sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    dst.append(distance); ist.append(st)
    
st=np.squeeze(np.where((dst==np.min(dst))))

plt.subplot(3,2,5)
plt.errorbar(dfs[str(nm_d[st])]['datetime'],dfs[str(nm_d[st])]['ozone'],yerr=None,color='gray', marker='o',linestyle='dashed',markerfacecolor='k',linewidth=2.2,markersize=6,markeredgecolor='k',alpha=0.8, 
             label=str(str(nm_d[st])+"_(PGN_dist:"+str(round(distance,1))+"km)"))


plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.3,prop={'size':22})

# plt.xlabel("Date")
plt.ylim(0, 100)
plt.xlim((np.datetime64(new+' 00:00'), np.datetime64(date+' 18:00')))
plt.ylabel("Ozone (ppbv)")
plt.text(np.datetime64(new+' 23:00'),90,'(c)', fontweight='bold', fontsize=22)

plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.rc('xtick', labelsize=10) 
# plt.rc('ytick', labelsize=8) 
# ix_loc=ndf4[ndf4.datetime.dt.day.values==25].index.values
# plt.text(ndf4['datetime'][len(ndf4)-len(ndf4)/3],4e16,str(site_name), fontweight='bold')


#ax1.plot(range(10), color='red')
ix_nrt=dfs[str(nm_d[st])][dfs[str(nm_d[st])].datetime.dt.normalize() == date].index.values

nrt=dfs[str(nm_d[st])].loc[ix_nrt]
# print (len(nrt), clr[st])
plt.subplot(3,2,6)
if (len(nrt))>0:
    plt.errorbar(nrt['datetime'],nrt['ozone'],yerr=None, marker='o',linestyle='dashed',color='r', markerfacecolor='r', markeredgecolor='r',linewidth=3.2,markersize=8,markeredgewidth=6.0, alpha=0.8)
    # legend=plt.legend(loc="upper right", ncol=1, numpoints=1, handlelength=1,framealpha=0.5,prop={'size':22})
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks( rotation=35, fontsize=14, fontweight='bold')
    plt.yticks( rotation=0, fontsize=14, fontweight='bold')
    plt.ylim(0, 100)

    plt.text(np.datetime64(date+' 12:00'), 5,'Local hours', fontsize=18, color='red', fontweight='bold')
    plt.text(np.datetime64(date+' 15:30'), 85,str(date), fontsize=22, color='r',fontweight='bold')
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')

    
    plt.text(np.datetime64(date+' 06:00'), -4,'06', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 08:00'), -4,'08', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 10:00'), -4,'10', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 12:00'), -4,'12', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 14:00'), -4,'14', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 16:00'), -4,'16', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 18:00'), -4,'18', fontsize=18, color='red',fontweight='bold')

else:
    plt.text(np.datetime64(date+' 10:00'), 5,'No data', fontsize=18, fontweight='bold')
    
    plt.xlim((np.datetime64(date+' 06:00'), np.datetime64(date+' 18:00')))
    plt.xticks( rotation=35, fontsize=14, fontweight='bold')
    plt.yticks( rotation=0, fontsize=14, fontweight='bold')
    plt.ylim(0, 100)
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')

    plt.text(np.datetime64(date+' 06:00'), -4,'06', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 08:00'), -4,'08', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 10:00'), -4,'10', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 12:00'), -4,'12', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 14:00'), -4,'14', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 16:00'), -4,'16', fontsize=18, color='red',fontweight='bold')
    plt.text(np.datetime64(date+' 18:00'), -4,'18', fontsize=18, color='red',fontweight='bold')

ndf4=dfs[str(nm_d[st])]
plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')
plt.text(np.datetime64(date+' 07:00'),90,'(f)', fontweight='bold', fontsize=22)


ndf4 = ndf4.reset_index(drop=True)
hr_av=[];obs=[]; hr_std=[]
for i in range(6,19):
    ix_loc=(np.squeeze(ndf4[ndf4.datetime.dt.hour.values==i].index.values))
    obs.append(((ndf4.iloc[ix_loc]).dropna()).shape[0])
    # print (sum(~np.isnan(ndf4.iloc[ix_loc].no2.values)))
    hr_av.append(np.nanmean(ndf4.iloc[ix_loc].ozone.values))
    hr_std.append(np.nanstd(ndf4.iloc[ix_loc].ozone.values))

x_dt=np.array(pd.date_range(date+' 06:00',date+' 18:00',freq='H'))
if  ((sum(~np.isnan(hr_av))))==13:
    for xe in range(len(hr_av)):
        plt.errorbar(x_dt[xe], hr_av[xe], yerr=hr_std[xe], xerr=None, marker= 'o', color='k', linestyle=None,markersize=8, linewidth=4,elinewidth=4, capsize=5, ecolor='gray',markerfacecolor='k', alpha=0.75)
    
        plt.annotate(obs[xe], (x_dt[xe], hr_av[xe]+5))
        plt.ylim(0, 100)
        plt.setp(plt.gca().get_xticklabels(), visible=False)
        plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
        plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')


else:
    
    plt.errorbar(x_dt,hr_av,yerr=None,color="k", marker='o',linestyle='None',markerfacecolor='k',linewidth=2.2,markersize=8,alpha=0.9, label=str(date))
    plt.setp(plt.gca().get_xticklabels(), visible=False)
    plt.xticks(color='red', rotation=35, fontsize=14, fontweight='bold')
    plt.yticks(color='red', rotation=0, fontsize=14, fontweight='bold')

plt.figtext(0.5, 1, str(sitename[ixd-1]), ha="center", fontsize=34, color='k', fontweight='bold')

# plt.savefig("/Users/prawat/Desktop/STAQS_PGN_quickL/Figures/Figure_"+str(date)+".pdf", dpi=300)
plt.show()   
##"""