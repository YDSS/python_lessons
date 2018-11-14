# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:27:07 2018
Created on Tue Aug 21 14:12:30 2018
@author: lenovo
"""
#######这个程序是以dmi(18)、结合macd的策略
from WindPy import w
w.start();
import pandas as pd
import numpy as np
import datetime
result=pd.DataFrame();
import csv
csv_reader=csv.reader(open('date2.csv'))
date=[];
for row in csv_reader:
    print row
    date.append(row)
    
    #####数据下载
date0=pd.DataFrame(date,columns=['开仓时间','平仓时间']);
date0['信号发出时间']=date0['开仓时间'].apply(lambda x:w.tdaysoffset(-1, x, "").Times[0]);
date0['前5日']=date0['信号发出时间'].apply(lambda x:w.tdaysoffset(-4, x, "").Times[0]);
date0['前10日']=date0['信号发出时间'].apply(lambda x:w.tdaysoffset(-9, x, "").Times[0]);
date0['前15日']=date0['信号发出时间'].apply(lambda x:w.tdaysoffset(-14, x, "").Times[0]);
date0['前20日']=date0['信号发出时间'].apply(lambda x:w.tdaysoffset(-19, x, "").Times[0]);
date0['前30日']=date0['信号发出时间'].apply(lambda x:w.tdaysoffset(-29, x, "").Times[0]);
date0['前60日']=date0['信号发出时间'].apply(lambda x:w.tdaysoffset(-59, x, "").Times[0]);
data=pd.DataFrame();
data['macd']=date0['开仓时间'].apply(lambda x:w.wss("510050.SH", "MACD","tradeDate="+str(x)+";MACD_L=40;MACD_S=20;MACD_N=15;MACD_IO=3;priceAdj=F;cycle=D").Data[0][0]);
data.loc[data['macd']>0,'开仓信号类型']='sell put';
data.loc[data['macd']<0,'开仓信号类型']='sell call';
data.loc[data['macd']>0,'期权类型']='put';
data.loc[data['macd']<0,'期权类型']='call';
data['信号发出时50etf收盘价']=date0['信号发出时间'].apply(lambda x:w.wss("510050.SH", "close","tradeDate="+str(x)+";priceAdj=F;cycle=D").Data[0][0]);
data['开仓当天开盘价']=date0['开仓时间'].apply(lambda x:w.wss("510050.SH", "open","tradeDate="+str(x)+";priceAdj=F;cycle=D").Data[0][0]);
data['平仓当天50etf收盘价']=date0['平仓时间'].apply(lambda x:w.wss("510050.SH", "close","tradeDate="+str(x)+";priceAdj=F;cycle=D").Data[0][0]);
data['持仓期间50etf涨跌幅']=pd.DataFrame((data['平仓当天50etf收盘价']-data['信号发出时50etf收盘价'])/data['信号发出时50etf收盘价']);
data['价格']=0.000;
data['持仓期间最大涨幅']=(date0.apply(lambda x:w.wss("510050.SH", "high_per","startDate="+str(x['开仓时间'])+";endDate="+str(x['平仓时间'])+";priceAdj=F").Data[0][0],axis=1)-data['信号发出时50etf收盘价'])/data['信号发出时50etf收盘价'];
data['持仓期间最大跌幅']=(date0.apply(lambda x:w.wss("510050.SH", "low_per","startDate="+str(x['开仓时间'])+";endDate="+str(x['平仓时间'])+";priceAdj=F").Data[0][0],axis=1)-data['信号发出时50etf收盘价'])/data['信号发出时50etf收盘价'];
data['标的前5日波动率']=date0.apply(lambda x:w.wss("510050.SH", "stdevry","startDate="+str(x['前5日'])+";endDate="+str(x['信号发出时间'])+";period=1;returnType=2").Data[0][0],axis=1);
data['标的前10日波动率']=date0.apply(lambda x:w.wss("510050.SH", "stdevry","startDate="+str(x['前10日'])+";endDate="+str(x['信号发出时间'])+";period=1;returnType=2").Data[0][0],axis=1);
data['标的前15日波动率']=date0.apply(lambda x:w.wss("510050.SH", "stdevry","startDate="+str(x['前15日'])+";endDate="+str(x['信号发出时间'])+";period=1;returnType=2").Data[0][0],axis=1);
data['标的前20日波动率']=date0.apply(lambda x:w.wss("510050.SH", "stdevry","startDate="+str(x['前20日'])+";endDate="+str(x['信号发出时间'])+";period=1;returnType=2").Data[0][0],axis=1);
data['标的前30日波动率']=date0.apply(lambda x:w.wss("510050.SH", "stdevry","startDate="+str(x['前30日'])+";endDate="+str(x['信号发出时间'])+";period=1;returnType=2").Data[0][0],axis=1);
data['标的前60日波动率']=date0.apply(lambda x:w.wss("510050.SH", "stdevry","startDate="+str(x['前60日'])+";endDate="+str(x['信号发出时间'])+";period=1;returnType=2").Data[0][0],axis=1);
####期权档位计算
for n in range(0,len(date0['开仓时间'])):
    if data['macd'].iat[n]>0:
        data['价格'].iat[n]=min(data['信号发出时50etf收盘价'].iat[n],data['开仓当天开盘价'].iat[n]).round(3);
    else:
        data['价格'].iat[n]=max(data['信号发出时50etf收盘价'].iat[n],data['开仓当天开盘价'].iat[n]).round(3);
option_data=pd.DataFrame({'标的价格':data['价格'],'期权类型':data['期权类型']});
def option_gear(option_data):        
    optiongear=pd.DataFrame();
    k=np.hstack((np.linspace(1,2.95,40).round(2),np.linspace(3,5,21).round(2)));
    optiongear['平值期权']=option_data['标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())][0]);
    optiongear['虚一档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(1)][0][0]);
    optiongear.loc[optiongear['虚一档'][np.isnan(optiongear['虚一档'])].index,'虚一档']=option_data.loc[optiongear['虚一档'][np.isnan(optiongear['虚一档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(1)][0][0]);
    optiongear['虚二档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(2)][0][0]);
    optiongear.loc[optiongear['虚二档'][np.isnan(optiongear['虚二档'])].index,'虚二档']=option_data.loc[optiongear['虚二档'][np.isnan(optiongear['虚二档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(2)][0][0]);
    optiongear['虚三档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(3)][0][0]);
    optiongear.loc[optiongear['虚三档'][np.isnan(optiongear['虚三档'])].index,'虚三档']=option_data.loc[optiongear['虚三档'][np.isnan(optiongear['虚三档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(3)][0][0]);
    optiongear['虚四档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(4)][0][0]);
    optiongear.loc[optiongear['虚四档'][np.isnan(optiongear['虚四档'])].index,'虚四档']=option_data.loc[optiongear['虚四档'][np.isnan(optiongear['虚四档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(4)][0][0]);
    optiongear['实一档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(1)][0][0]);
    optiongear.loc[optiongear['实一档'][np.isnan(optiongear['实一档'])].index,'实一档']=option_data.loc[optiongear['实一档'][np.isnan(optiongear['实一档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(1)][0][0]);
    optiongear['实二档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(2)][0][0]);
    optiongear.loc[optiongear['实二档'][np.isnan(optiongear['实二档'])].index,'实二档']=option_data.loc[optiongear['实二档'][np.isnan(optiongear['实二档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(2)][0][0]);
    optiongear['实三档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(3)][0][0]);
    optiongear.loc[optiongear['实三档'][np.isnan(optiongear['实三档'])].index,'实三档']=option_data.loc[optiongear['实三档'][np.isnan(optiongear['实三档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(3)][0][0]);
    optiongear['实四档']=option_data.loc[option_data['期权类型']=='call','标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())-np.array(4)][0][0]);
    optiongear.loc[optiongear['实四档'][np.isnan(optiongear['实四档'])].index,'实四档']=option_data.loc[optiongear['实四档'][np.isnan(optiongear['实四档'])].index,'标的价格'].apply(lambda x:k[np.where(abs(x-k)==abs(x-k).min())+np.array(4)][0][0]);
    return optiongear
    print optiongear  
optiongear=option_gear(option_data);

###策略回测计算
for i in range(0,len(date0['开仓时间'])):
    if  data['开仓信号类型'].iat[i]=='sell put':
        options=w.wset("optionchain",u"date="+str(date0['开仓时间'].iat[i])+u";us_code=510050.SH;option_var=510050OP.SH;call_put=认沽");
    else:
        options=w.wset("optionchain",u"date="+str(date0['开仓时间'].iat[i])+u";us_code=510050.SH;option_var=510050OP.SH;call_put=认购");
    options=pd.DataFrame(zip(*options.Data),columns=options.Fields);
    options=options[options.expiredate>60];###剔除掉剩余日期不到60天的
    options['开仓日期']=date0['开仓时间'].iat[i];
    options['平仓日期']=date0['平仓时间'].iat[i];
    options['平值期权']=optiongear['平值期权'].iat[i];
    options['虚一档']=optiongear['虚一档'].iat[i];
    options['虚二档']=optiongear['虚二档'].iat[i];
    options['虚三档']=optiongear['虚三档'].iat[i];
    options['虚四档']=optiongear['虚四档'].iat[i];
    options['实一档']=optiongear['实一档'].iat[i];
    options['实二档']=optiongear['实二档'].iat[i];
    options['实三档']=optiongear['实三档'].iat[i];
    options['实四档']=optiongear['实四档'].iat[i];
    options['持仓期间标的涨跌幅']=data['持仓期间50etf涨跌幅'].iat[i];
    options['标的前5日波动率']=data['标的前5日波动率'].iat[i];
    options['标的前10日波动率']=data['标的前10日波动率'].iat[i];
    options['标的前15日波动率']=data['标的前15日波动率'].iat[i];
    options['标的前20日波动率']=data['标的前20日波动率'].iat[i];
    options['标的前30日波动率']=data['标的前30日波动率'].iat[i];
    options['标的前60日波动率']=data['标的前60日波动率'].iat[i];
    options['IV']=options.apply(lambda x:w.wss(x['option_code'], "us_impliedvol","tradeDate="+str(x['开仓日期'])).Data[0][0],axis=1);
    options1=options[options.last_tradedate.apply(lambda x :x.date())>=datetime.datetime.strptime(options['平仓日期'].iat[0],'%Y/%m/%d').date()];####平仓时还没到期的期权
    options2=options[options.last_tradedate.apply(lambda x :x.date())<datetime.datetime.strptime(options['平仓日期'].iat[0],'%Y/%m/%d').date()];####平仓时已到期的期权
    if len(options2['option_code']):    
        options1['开仓价格']=options1['option_code'].apply(lambda x:w.wss(x,'vwap',"tradeDate="+str(date0['开仓时间'].iat[i])+";cycle=D;priceAdj=F").Data[0][0]);##开仓前半个小时均价为开仓价格
        options1['平仓价格']=options1['option_code'].apply(lambda x:w.wss(x,'vwap',"tradeDate="+str(date0['平仓时间'].iat[i])+";cycle=D;priceAdj=F").Data[0][0]);####收盘前最后半个小时均价为平仓价格
        options1['保证金']=options1.apply(lambda x:max(w.wsd(x['option_code'],'maint_margin',str(x['开仓日期']),str(x['平仓日期']),'Currency=CNY;PriceAdj=F').Data[0]),axis=1);
        options2['开仓价格']=options2['option_code'].apply(lambda x:w.wss(x,'vwap',"tradeDate="+str(date0['开仓时间'].iat[i])+";cycle=D;priceAdj=F").Data[0][0]);
        options2['平仓价格']=options2['option_code'].apply(lambda x:w.wss(x,'vwap',"tradeDate="+str(date0['平仓时间'].iat[i]).strip('00:00:00')+";cycle=D;priceAdj=F").Data[0][0]);
        options2['保证金']=options2.apply(lambda x:max(w.wsd(x['option_code'],'maint_margin',str(date0['开仓时间'].iat[i][0]),str(x['last_tradedate']).strip('00:00:00'),'Currency=CNY;PriceAdj=F').Data[0]),axis=1);
        options1['持仓期间收益率']=(options1['开仓价格']-options1['平仓价格'])/options1['保证金'];
        options2['持仓期间收益率']=(options2['开仓价格']-options2['平仓价格'])/options2['保证金'];
        result0=options1.append(options2);
        result=result0.append(result);
       
    else:
        options1['开仓价格']=options1['option_code'].apply(lambda x:w.wss(x,'vwap',"tradeDate="+str(date0['开仓时间'].iat[i])+";cycle=D;priceAdj=F").Data[0][0]);##开仓前半个小时均价为开仓价格
        options1['平仓价格']=options1['option_code'].apply(lambda x:w.wss(x,'vwap',"tradeDate="+str(date0['平仓时间'].iat[i])+";cycle=D;priceAdj=F").Data[0][0]);####收盘前最后半个小时均价为平仓价格收盘前最后半个小时均价为options1['持仓期间收益率']=(options1['开仓价格']-options1['平仓平仓价格
        options1['保证金']=options1.apply(lambda x:max(w.wsd(x['option_code'],'maint_margin',str(x['开仓日期']),str(x['平仓日期']),'Currency=CNY;PriceAdj=F').Data[0]),axis=1);
        options1['持仓期间收益率']=(options1['开仓价格']-options1['平仓价格'])/options1['保证金'];
        time1=str(date0['开仓时间'].iat[i]);
        time2=str(date0['平仓时间'].iat[i]);
        options1['最低收益率']=options1.apply(lambda x:(x['开仓价格']-max(w.wsd(x['option_code'],'close',time1,time2,'PriceAdj=F').Data[0])*10000)/x['保证金'],axis=1);
        options1['最高收益率']=options1.apply(lambda x:(x['开仓价格']-min(w.wsd(x['option_code'],'close',time1,time2,'PriceAdj=F').Data[0])*10000)/x['保证金'],axis=1);
        result=options1.append(result);
result=result.sort_values(by=['开仓日期']);
result=result.drop(['us_code','us_name','option_var','exe_type','settle_method','multiplier','first_tradedate','last_tradedate'],axis=1);    
result.to_csv('resultmacd-dmi-iv-hv.csv',encoding='utf-8',index=False);
    
    
   
    
    


