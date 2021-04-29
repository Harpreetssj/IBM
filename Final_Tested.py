import os,sys
import datetime
import time
import tkinter as tk
from tkinter import ttk,filedialog
from tkinter.ttk import *
from bs4 import BeautifulSoup
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates


from tkcalendar import Calendar, DateEntry #may need to install this library

#---------------try1.py------------------------
class try1:
    def brn(soup1):
        mData=[]
        d=[]  
        tables= soup1.find("table",{"summary":"This table displays Foreground Wait Events and their wait statistics"})
        x=tables.find_all('td')
        tablesV= soup1.find("table",{"summary":"This table displays wait class statistics ordered by total wait time"})
        y=tablesV.find_all('td')
        
        s=0
        j=4
        ja=4
        m=6
        val=[]
        vala=[]
        eV=0
        dV=4
        evV=[]
        jap=0
        datV=[]
        fk=['Network', 'Concurrency', 'Other', 'DB CPU', 'System I/O', 'User I/O', 'Application', 'Cluster', 'Commit', 'Configuration', 'Administrative']
        k=['rowcachelock', 'librarycachelock', 'librarycachepin', 'DLMcrossinstcallcompletion', 'dbfilesequentialread', 'PGAmemoryoperation', 'DiskfileoperationsI/O', 'logfilesync', 'gccrgrant2-way', 'enq:TM-contention', 'SQL*Netbreak/resettoclient', 'gccurrentgrant2-way', 'reliablemessage', 'enq:RO-fastobjectreuse', 'dbfilescatteredread', 'enq:CR-blockrangereuseckpt', 'CSSinitialization', 'enq:TS-contention', 'gccrmultiblockgrant', 'KJC:Waitformsgsendstocomplete', 'CSSoperation:action', 'gccurrentblock2-way', 'controlfilesequentialread', 'localwritewait', 'RFSattach', 'RFSdispatch', 'gccurrentgrantbusy', 'dbfileparallelread', 'KSVmasterwait', 'gccrblock2-way', 'gccurrentblockbusy', 'CSSoperation:dataquery', 'gccurrentmultiblockrequest', 'enq:PS-contention', 'IPCsendcompletionsync', 'enq:FB-contention', 'CSSgroupmembershipquery', 'SQL*Netmessagetoclient', 'name-servicecallwait', 'PXDeq:SlaveSessionStats', 'enq:IV-contention', 'PXqreflatch', 'FailedLogonDelay', 'PXDeq:reapcredit', 'PXDeq:SignalACKEXT', 'ASMfilemetadataoperation', 'switchlogfilecommand', 'oraclethreadbootstrap', 'enq:JS-jobrunlock-synchronize', 'gccrblocklost', 'controlfileparallelwrite', 'logfileswitchcompletion', 'JSkglgetobjectwait', 'cursor:pinSwaitonX', 'logswitch/archive', 'latchfree', 'CSSoperation:query', 'gccrblockcongested', 'gccurrentretry', 'gcbufferbusyacquire', 'TCPSocket(KGAS)', 'directpathread', 'bufferbusywaits', 'librarycache:mutexX', 'CRScallcompletion', 'SQL*Netmoredatatoclient', 'librarycacheloadlock', 'latch:sharedpool', 'Datafileinitwrite', 'enq:HW-contention', 'gccurrentblocklost', 'latch:gesresourcehashlist', 'SQL*Netmessagefromdblink', 'SQL*Netmoredatafromdblink', 'SyncASMrebalance', 'rdbmsipcreply', 'utl_fileI/O', 'Globaltransactionacquireinstancelocks', 'cursor:pinS', 'enq:TX-rowlockcontention', 'SQL*Netmoredatatodblink', 'undosegmentextension', 'SQL*Netmoredatafromclient', 'enq:TX-contention', 'readbyothersession', 'logbufferspace', 'latch:messages', 'SQL*Netmessagetodblink', 'directpathwritetemp', 'rowcachemutex', 'ASMIOfornon-blockingpoll', 'enq:UL-contention', 'ADRblockfileread', 'gcindexoperation', 'latch:cachebufferschains', 'latch:undoglobaldata', 'enq:TX-indexcontention', 'directpathreadtemp', 'waitlistlatchfree', 'enq:HV-contention', 'directpathwrite', 'enq:TX-allocateITLentry', 'kksfbcchildcompletion', 'latch:MGAsharedcontextlatch', 'processterminate', 'SQL*Netvectordatafromclient', 'gccrmultiblockmixed', 'gccrmultiblockrequest', 'enq:AE-lock', 'gccrblockbusy', 'gcbufferbusyrelease', 'gccurrentblockcongested', 'gccrgrantcongested', 'latch:callallocation', 'enq:PR-contention', 'enq:JS-queuelock', 'latch:enqueuehashchains', 'gccurrentgrantcongested', 'externaltableopen', 'enq:TO-contention']
        [val.append("") for i in range(121)]
        [vala.append("") for fd in range(11)]    
        f=[]
        while(1):
            try:
                if jap!=1:
                    evV.append(y[eV].text)
                    datV.append(y[dV].text)
                    eV+=6
                    dV+=6
            except:
                jap=1
                continue

            if(x[m].text!='\xa0' and x[m].text!='0.00'):
                        value = (x[s].text).replace(" ","")
                        d.append(value)
                        s+=7
                        #F-->US/MS/S
                        if 'us' in x[ja].text:
                            jabe=float(float(x[ja].text[:-2])/1000)
                        if 'ns' in x[ja].text:
                            jabe=float(float(x[ja].text[:-2])/1000000)
                        if 's' in x[ja].text and 'us' not in x[ja].text and 'ms' not in x[ja].text and 'ns' not in x[ja].text:
                            jabe=float(float(x[ja].text[:-1])*1000)
                        if 'ms' in x[ja].text:
                            jabe=float(x[ja].text[:-2])
                        if 's' not in x[ja].text and 'us' not in x[ja].text and 'ms' not in x[ja].text and 'ns' not in x[ja].text:
                            jabe=float(x[ja].text)
                        f.append(jabe)
                        ja+=7
                        m+=7
                        
            else:
                        break
                
            
        for i in range(len(evV)):
            for j in range(len(fk)):
                try:
                    if evV[i] == fk[j]:
                        vala[j] = float(datV[i])
                    else:
                        pass
                except:
                    continue
        for i in range(len(d)):
            for j in range(len(k)):
                if d[i] == k[j]:            
                    val[j]=f[i]
                else:
                    pass
        
        return(val,vala)



class dateF:
    def dateFilter(a):
        vrn={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        a1=a.split()
        a11=a1[0].split('-')
        a12=a1[1].split(':')
        a11[2]+='20'
        a11[1]=vrn[a11[1]]
        a11=[int(i) for i in a11]
        a12=[int(i) for i in a12]
        a1=datetime.datetime(a11[2],a11[1],a11[0],a12[0],a12[1],a12[2])
        return(a1)
    def dateFilterNA(a):
        a1=a.split('\n')
        a11=a1[1].split('-')
        a12=a1[0].split(':')
        a11=[int(i) for i in a11]
        a12=[int(i) for i in a12]
        a1=datetime.datetime(a11[0],a11[1],a11[2],a12[0],a12[1],a12[2])
        return(a1)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Scrapping !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Awr_report:
    plot = []
    Afk=['Network', 'Concurrency', 'Other', 'DB CPU', 'System I/O', 'User I/O', 'Application', 'Cluster', 'Commit', 'Configuration', 'Administrative']
    mainData=['rowcachelock', 'librarycachelock', 'librarycachepin', 'DLMcrossinstcallcompletion', 'dbfilesequentialread', 'PGAmemoryoperation', 'DiskfileoperationsI/O', 'logfilesync', 'gccrgrant2-way', 'enq:TM-contention', 'SQL*Netbreak/resettoclient', 'gccurrentgrant2-way', 'reliablemessage', 'enq:RO-fastobjectreuse', 'dbfilescatteredread', 'enq:CR-blockrangereuseckpt', 'CSSinitialization', 'enq:TS-contention', 'gccrmultiblockgrant', 'KJC:Waitformsgsendstocomplete', 'CSSoperation:action', 'gccurrentblock2-way', 'controlfilesequentialread', 'localwritewait', 'RFSattach', 'RFSdispatch', 'gccurrentgrantbusy', 'dbfileparallelread', 'KSVmasterwait', 'gccrblock2-way', 'gccurrentblockbusy', 'CSSoperation:dataquery', 'gccurrentmultiblockrequest', 'enq:PS-contention', 'IPCsendcompletionsync', 'enq:FB-contention', 'CSSgroupmembershipquery', 'SQL*Netmessagetoclient', 'name-servicecallwait', 'PXDeq:SlaveSessionStats', 'enq:IV-contention', 'PXqreflatch', 'FailedLogonDelay', 'PXDeq:reapcredit', 'PXDeq:SignalACKEXT', 'ASMfilemetadataoperation', 'switchlogfilecommand', 'oraclethreadbootstrap', 'enq:JS-jobrunlock-synchronize', 'gccrblocklost', 'controlfileparallelwrite', 'logfileswitchcompletion', 'JSkglgetobjectwait', 'cursor:pinSwaitonX', 'logswitch/archive', 'latchfree', 'CSSoperation:query', 'gccrblockcongested', 'gccurrentretry', 'gcbufferbusyacquire', 'TCPSocket(KGAS)', 'directpathread', 'bufferbusywaits', 'librarycache:mutexX', 'CRScallcompletion', 'SQL*Netmoredatatoclient', 'librarycacheloadlock', 'latch:sharedpool', 'Datafileinitwrite', 'enq:HW-contention', 'gccurrentblocklost', 'latch:gesresourcehashlist', 'SQL*Netmessagefromdblink', 'SQL*Netmoredatafromdblink', 'SyncASMrebalance', 'rdbmsipcreply', 'utl_fileI/O', 'Globaltransactionacquireinstancelocks', 'cursor:pinS', 'enq:TX-rowlockcontention', 'SQL*Netmoredatatodblink', 'undosegmentextension', 'SQL*Netmoredatafromclient', 'enq:TX-contention', 'readbyothersession', 'logbufferspace', 'latch:messages', 'SQL*Netmessagetodblink', 'directpathwritetemp', 'rowcachemutex', 'ASMIOfornon-blockingpoll', 'enq:UL-contention', 'ADRblockfileread', 'gcindexoperation', 'latch:cachebufferschains', 'latch:undoglobaldata', 'enq:TX-indexcontention', 'directpathreadtemp', 'waitlistlatchfree', 'enq:HV-contention', 'directpathwrite', 'enq:TX-allocateITLentry', 'kksfbcchildcompletion', 'latch:MGAsharedcontextlatch', 'processterminate', 'SQL*Netvectordatafromclient', 'gccrmultiblockmixed', 'gccrmultiblockrequest', 'enq:AE-lock', 'gccrblockbusy', 'gcbufferbusyrelease', 'gccurrentblockcongested', 'gccrgrantcongested', 'latch:callallocation', 'enq:PR-contention', 'enq:JS-queuelock', 'latch:enqueuehashchains', 'gccurrentgrantcongested', 'externaltableopen', 'enq:TO-contention']
    vrn={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    root_dict={'e':5}
    keys=[]
    date=[]
    time=[]
    snap=[]
    dbTime=[]
    d=[]
    gamble=2
    f=[]
    k=[]
    waitT=[]
    mData=[]
    graphT=[]
    vall=[]
    def yearS(sdate):
        a=int(sdate[2])
        b=a%10
        a=int(a/10)
        a=a%10
        sdate[2]=str(a)+str(b)
        date=sdate[0]+"-"+sdate[1]+"-"+sdate[2]
        return(date)
    def get_data(self,file,ch):
                soup = BeautifulSoup(open(file), 'html.parser')
                tables = soup.find_all("table")
                tablesinfo= soup.find("table",{"summary":"This table displays snapshot information"})
                table4_datalist = tablesinfo.find_all('td')
                table2_datalist = tables[1].find_all('td')
                memory= soup.find("table",{"summary":"This table displays memory statistics"})
                mStat = memory.find_all('td')
                for var1 in range(2,10,3):
                    if mStat[var1].text.strip()=='':
                        Awr_report.mData.append(float(0))
                    else:
                        Awr_report.mData.append((float(mStat[var1].text.strip().replace(",","")))/1000)
                vrn,newV=try1.brn(soup)
                self.begin_snap = table4_datalist[1].text
                self.snap_time = table4_datalist[2].text
                self.elapsed = table4_datalist[14].text
                self.db_time = table4_datalist[20].text
                
                self.db_time=float(self.db_time.replace("(mins)","").strip())
                for i in range(len(tables)):
                    ta = tables[i].find_all('th')
                    for j in range(len(ta)):
                        if ta[j].text.lower() == 'inst num':
                                ta1 = tables[i].find_all('td')
                                self.instance_number = ta1[j].text
                                break
                date=self.snap_time.split()
                for key in Awr_report.root_dict.keys() :
                    Awr_report.keys.append(key)
                  
                for dict in Awr_report.keys:
                     try:
                         del Awr_report.root_dict['e']
                     except:
                         pass
                     if self.instance_number not in Awr_report.keys:
                         Awr_report.root_dict[self.instance_number]=[Awr_report.date,Awr_report.time,Awr_report.snap,Awr_report.vall,Awr_report.waitT,Awr_report.mData,Awr_report.dbTime]
                         
                          
                      
                          #print(Awr_report.root_dict[self.instance_number])
                     val=Awr_report.root_dict[self.instance_number]
                     val[0].append(date[0])
                     val[1].append(date[1])
                     val[2].append(int(self.begin_snap))
                     val[3].append(vrn)
                     val[4].append(newV)
                     val[5]=Awr_report.mData
                     val[6].append(self.db_time)
                     Awr_report.root_dict[self.instance_number]=val
                     Awr_report.date=[]
                     Awr_report.time=[]
                     Awr_report.snap=[]
                     Awr_report.avgW=[]
                     Awr_report.vall=[]
                     Awr_report.waitT=[]
                     Awr_report.dbTime=[]
                     Awr_report.mData=[]
                  
                         #Awr_report.date.append(date[0])
                         #Awr_report.root_dict[self.instance_number]=[Awr_report.date]
                         
                     break


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!! Main Function !!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class GUI:

    def __init__(self):
            # Creating tkinter window 
            window = tk.Tk() 
            window.title('WINDOW') 
            window.geometry('900x740') 
            window.resizable(False, False)
            #print('this is date',Awr_report.)
            # label
            ttk.Label(window, text = "!! Select Interval !!", 
                            font = ("Times New Roman", 25)).grid(column = 2, 
                            row = 0, padx = 0, pady = 10, columnspan=2)
            ttk.Label(window, text = "Start Date :", 
                            font = ("Times New Roman", 15)).grid(column = 0, 
                            row = 1, padx = 10, pady = 15)

            ttk.Label(window, text = "Time (Hours)  :", 
                            font = ("Times New Roman", 15)).grid(column = 2, 
                            row = 1, padx = 10, pady = 15)

            ttk.Label(window, text = "Minutes  :", 
                            font = ("Times New Roman", 15)).grid(column = 4, 
                            row = 1, padx = 10, pady = 15)

            ttk.Label(window, text = "End Date  :", 
                            font = ("Times New Roman", 15)).grid(column = 0,
                            row = 2, padx = 10, pady = 15)

            ttk.Label(window, text = "Time (Hours)  :", 
                            font = ("Times New Roman", 15)).grid(column = 2, 
                            row = 2, padx = 10, pady = 15)

            ttk.Label(window, text = "Minutes  :", 
                            font = ("Times New Roman", 15)).grid(column = 4, 
                            row = 2, padx = 10, pady = 15)
            
            ttk.Label(window, text = "Instance Number  :", 
                            font = ("Times New Roman", 15)).grid(column = 1, 
                            row = 3, padx = 10, pady = 15)
            ttk.Label(window, text = "Foreground Event  :", 
                            font = ("Times New Roman", 15)).grid(column = 3, 
                            row = 3, padx = 10, pady = 15)
            result_list=ttk.Label(window, text = "", font = ("Times New Roman", 10))
            
            result_list.grid(column = 0,columnspan='12',row = 5, padx = 10, pady = 15)


            # Combobox creation 
            n1 = tk.StringVar()
            n2 = tk.StringVar()
            n3 = tk.StringVar()
            n4 = tk.StringVar()
            n5 = tk.StringVar()
            n6 = tk.StringVar()
            n7 = tk.StringVar()
            
            #xyz=[]
            #print('before',Awr_report.root_dict['1'][0])
            #for i in Awr_report.root_dict['1'][0]:
            #    xyz.append(i.replace('-',' '))
            #xyz.sort(key = lambda date: datetime.datetime.strptime(date, '%d %B %y')) 
            #d_strt = xyz[0].split(' ')
            #d_end = xyz[-1].split(' ')
            #print('sorted',xyz)
            startDate = DateEntry(window,state="readonly",width=15,bg="darkblue",fg="white",date_pattern='dd-mm-y') 
            startHours = ttk.Combobox(window, state="readonly", width = 15, textvariable = n1)
            startMinutes = ttk.Combobox(window, state="readonly", width = 15, textvariable = n2)
            endDate = DateEntry(window,state="readonly",width=15,bg="darkblue",fg="white",date_pattern='dd-mm-y')#year=int('20'+d_end[-1]),month=int('0'+str(Awr_report.vrn[d_strt[1]]))
            endHours = ttk.Combobox(window, state="readonly", width = 15, textvariable = n3)
            endMinutes = ttk.Combobox(window, state="readonly", width = 15, textvariable = n4)
            instance = ttk.Combobox(window, state="readonly", width = 15, textvariable = n5)
            foreground_event = ttk.Combobox(window, state="readonly", width = 35, textvariable = n6)
            baseoptions = ttk.Combobox(window, state="readonly", width = 25, textvariable = n7)
            


            # Adding combobox drop down list 
            startHours['values'] = tuple(range(0,24))
            startMinutes['values'] = tuple(range(0,60))
            gg=[]
            gg1=['All']
            endHours['values'] = tuple(range(0,24))
            endMinutes['values'] = tuple(range(0,60))
            for i in Awr_report.root_dict.keys():
                gg.append(i)
                gg1.append(i)
            #instance['values'] = tuple(gg)
            baseoptions['values']= ('foreground event', 'waitclasses','waitclasses(SG)','Memory Statistics','DB Time')
            foreground_event['values'] = ('rowcachelock', 'librarycachelock', 'librarycachepin', 'librarycacherevalidation', 'SQL*Netbreak/resettoclient', 'PGAmemoryoperation', 'librarycache:mutexX', 'DiskfileoperationsI/O', 'dbfilesequentialread', 'logfilesync', 'DLMcrossinstcallcompletion', 'reliablemessage', 'enq:RO-fastobjectreuse', 'gccrgrant2-way', 'enq:TM-contention', 'enq:CR-blockrangereuseckpt', 'gccurrentblock2-way', 'gccrblock2-way', 'gccurrentgrant2-way', 'librarycacheloadlock', 'CSSinitialization', 'gccurrentblockbusy', 'KJC:Waitformsgsendstocomplete', 'gccrmultiblockmixed', 'gccurrentgrantbusy', 'localwritewait', 'CSSoperation:action', 'controlfilesequentialread', 'RFSattach', 'RFSdispatch', 'SQL*Netmessagetoclient', 'KSVmasterwait', 'SQL*Netmoredatatoclient', 'CSSoperation:dataquery', 'IPCsendcompletionsync', 'enq:PS-contention', 'IPCgroupservicecall', 'CSSgroupmembershipquery', 'latch:messages', 'dbfilescatteredread', 'PXDeq:JoinACK', 'gccrmultiblockgrant', 'PXDeq:SlaveSessionStats', 'name-servicecallwait', 'enq:OD-SerializingDDLs', 'cursor:pinS', 'CSSoperation:query', 'watchdogmainloop', 'SQL*Netmessagefromclient', 'single-taskmessage', 'PL/SQLlocktimer', 'PXDeq:ExecutionMsg', 'gccrblocklost', 'undosegmentextension', 'enq:TS-contention', 'enq:HW-contention', 'gccrblockbusy', 'gcbufferbusyrelease', 'PXDeq:reapcredit', 'directpathwrite', 'rdbmsipcreply', 'PXDeq:ExecuteReply', 'PXDeqCredit:sendblkd', 'PXDeq:ParseReply', 'PXDeq:MsgFragment', 'gccurrentmultiblockrequest', 'enq:MS-contention', 'XDBSGAinitialization', 'gcbufferbusyacquire', 'bufferbusywaits', 'readbyothersession', 'ASMIOfornon-blockingpoll', 'gccurrentblockcongested', 'latchfree', 'gesresourcedirectorytobeunfrozen', 'oraclethreadbootstrap', 'enq:DL-contention', 'enq:ZH-compressionanalysis', 'gccurrentblocklost', 'processdiagnosticdump', 'enq:SV-contention', 'SQL*Netmoredatafromclient', 'gccrgrantcongested', 'rowcachemutex', 'gccrgrantbusy', 'enq:TO-contention', 'enq:RC-ResultCache:Contention', 'enq:CF-contention', 'enq:FB-contention', 'dbfileparallelread', 'enq:UL-contention', 'servicemonitor:instrecoverycompletion')
            
            startHours.current(0)
            startMinutes.current(0)
            endHours.current(23)
            endMinutes.current(0)
            baseoptions.current(0)
            #instance.current(0)
            foreground_event.current(0)
            if baseoptions.get()=='foreground event':
                instance['values'] = ('All',)+tuple(gg)
                instance.current(0)
            def callback(eventObject):
                if baseoptions.get()=='waitclasses':
                    instance['values'] = tuple(gg)
                    foreground_event['values'] = ('Network', 'Other', 'Concurrency', 'DBCPU', 'System I/O', 'Application', 'User I/O', 'Configuration', 'Cluster', 'Commit','Administrative')
                    foreground_event.current(0)
                    instance.current(0)
             
                if baseoptions.get()=='foreground event':
                    instance['values'] = ('All',)+tuple(gg)
                    foreground_event['values'] = ('rowcachelock', 'librarycachelock', 'librarycachepin', 'DLMcrossinstcallcompletion', 'dbfilesequentialread', 'PGAmemoryoperation', 'DiskfileoperationsI/O', 'logfilesync', 'gccrgrant2-way', 'enq:TM-contention', 'SQL*Netbreak/resettoclient', 'gccurrentgrant2-way', 'reliablemessage', 'enq:RO-fastobjectreuse', 'dbfilescatteredread', 'enq:CR-blockrangereuseckpt', 'CSSinitialization', 'enq:TS-contention', 'gccrmultiblockgrant', 'KJC:Waitformsgsendstocomplete', 'CSSoperation:action', 'gccurrentblock2-way', 'controlfilesequentialread', 'localwritewait', 'RFSattach', 'RFSdispatch', 'gccurrentgrantbusy', 'dbfileparallelread', 'KSVmasterwait', 'gccrblock2-way', 'gccurrentblockbusy', 'CSSoperation:dataquery', 'gccurrentmultiblockrequest', 'enq:PS-contention', 'IPCsendcompletionsync', 'enq:FB-contention', 'CSSgroupmembershipquery', 'SQL*Netmessagetoclient', 'name-servicecallwait', 'PXDeq:SlaveSessionStats', 'enq:IV-contention', 'PXqreflatch', 'FailedLogonDelay', 'PXDeq:reapcredit', 'PXDeq:SignalACKEXT', 'ASMfilemetadataoperation', 'switchlogfilecommand', 'oraclethreadbootstrap', 'enq:JS-jobrunlock-synchronize', 'gccrblocklost', 'controlfileparallelwrite', 'logfileswitchcompletion', 'JSkglgetobjectwait', 'cursor:pinSwaitonX', 'logswitch/archive', 'latchfree', 'CSSoperation:query', 'gccrblockcongested', 'gccurrentretry', 'gcbufferbusyacquire', 'TCPSocket(KGAS)', 'directpathread', 'bufferbusywaits', 'librarycache:mutexX', 'CRScallcompletion', 'SQL*Netmoredatatoclient', 'librarycacheloadlock', 'latch:sharedpool', 'Datafileinitwrite', 'enq:HW-contention', 'gccurrentblocklost', 'latch:gesresourcehashlist', 'SQL*Netmessagefromdblink', 'SQL*Netmoredatafromdblink', 'SyncASMrebalance', 'rdbmsipcreply', 'utl_fileI/O', 'Globaltransactionacquireinstancelocks', 'cursor:pinS', 'enq:TX-rowlockcontention', 'SQL*Netmoredatatodblink', 'undosegmentextension', 'SQL*Netmoredatafromclient', 'enq:TX-contention', 'readbyothersession', 'logbufferspace', 'latch:messages', 'SQL*Netmessagetodblink', 'directpathwritetemp', 'rowcachemutex', 'ASMIOfornon-blockingpoll', 'enq:UL-contention', 'ADRblockfileread', 'gcindexoperation', 'latch:cachebufferschains', 'latch:undoglobaldata', 'enq:TX-indexcontention', 'directpathreadtemp', 'waitlistlatchfree', 'enq:HV-contention', 'directpathwrite', 'enq:TX-allocateITLentry', 'kksfbcchildcompletion', 'latch:MGAsharedcontextlatch', 'processterminate', 'SQL*Netvectordatafromclient', 'gccrmultiblockmixed', 'gccrmultiblockrequest', 'enq:AE-lock', 'gccrblockbusy', 'gcbufferbusyrelease', 'gccurrentblockcongested', 'gccrgrantcongested', 'latch:callallocation', 'enq:PR-contention', 'enq:JS-queuelock', 'latch:enqueuehashchains', 'gccurrentgrantcongested', 'externaltableopen', 'enq:TO-contention')
                    instance.current(0)
                    foreground_event.current(0)
                if baseoptions.get()=='waitclasses(SG)':
                    instance['values'] = tuple(gg)
                    foreground_event['values'] = ('All')
                    instance.current(0)
                    foreground_event.current(0)
                    
                if baseoptions.get()=='Memory Statistics':
                    instance['values'] = tuple(gg)
                    foreground_event['values'] = (tuple('-'))
                    instance.current(0)
                    foreground_event.current(0)
                    
                if baseoptions.get()=='DB Time':
                    instance['values'] = ('All',)+tuple(gg)
                    foreground_event['values'] = (tuple('-'))
                    instance.current(0)
                    foreground_event.current(0)
            baseoptions.bind("<<ComboboxSelected>>",callback)
            
            btn = tk.Button(window,width='15',height='2' ,text = 'SUBMIT',command = lambda: self.main(startDate,startHours,startMinutes,endDate,endHours,endMinutes,instance,foreground_event,result_list,window,baseoptions,show='inscreen'))
            btn2 = tk.Button(window,width='15',height='2' ,text = 'Show',command = lambda: self.main(startDate,startHours,startMinutes,endDate,endHours,endMinutes,instance,foreground_event,result_list,window,baseoptions,show='fullscreen'))
            
            btn.grid(column = 0 , row = 4, columnspan=12)
            btn2.grid(column = 4 , row = 4, columnspan=12)

            startDate.grid(column = 1, row = 1) 
            startHours.grid(column = 3, row = 1) 
            startMinutes.grid(column = 5, row = 1) 
            endDate.grid(column = 1, row = 2) 
            endHours.grid(column = 3, row = 2) 
            endMinutes.grid(column = 5, row = 2)
            instance.grid(column = 2, row = 3)
            foreground_event.grid(column=4, row=3,columnspan=2)
            baseoptions.grid(column = 0, row = 0,columnspan=2)

            
            window.mainloop()

   

    def main(self,startDate,startHours,startMinutes,endDate,endHours,endMinutes,instance,foreground_event,result_list,window,baseoptions,show):#base options also here
                #Awr_report.plot=[]
                #print(baseoptions.get())#this is current baseoption
                ch=foreground_event.get()  #foreground
                xx=str(instance.get())
                #for subdir, dirs, files in os.walk('./'):   
                 #   for file in files:
                  #      if file=='ibm.py' or file=='code.py':
                   #         continue
                    #    print(file)
                     #   obj1 = Awr_report()
                      #  obj1.get_data(file,ch)
                
                instance=str(instance.get())
                jeev=[]
                if instance!='All':
                    alpha=Awr_report.root_dict[instance]
                    if baseoptions.get()=='foreground event':
                        filter=alpha[3]
                    if baseoptions.get()=='waitclasses':
                        filter=alpha[4]
                    if baseoptions.get()=='waitclasses(SG)':
                        filter=alpha[4]
                    if baseoptions.get()=='Memory Statistics':
                        filter=alpha[5]
                    lst=Awr_report.root_dict[instance]

                    if baseoptions.get()=='DB Time':
                        filter=alpha[6]
                if instance=='All' and (baseoptions.get()=='DB Time' or baseoptions.get()=='foreground event'):
                    for lp in Awr_report.root_dict.keys():
                        jeev.append(lp)
                    
                
                
                
                #input("Intsance : ")
                month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
                s_raw=startDate.get().split('-')
                s_raw[1]=month[int(s_raw[1])]
                date=s_raw[0]+'-'+s_raw[1]+'-'+s_raw[2]
                e_raw=endDate.get().split('-')
                e_raw[1]=month[int(e_raw[1])]
                date1=e_raw[0]+'-'+e_raw[1]+'-'+e_raw[2]
                #date1=str(endDate.get()) 
                stime=str(startHours.get())+':'+str(startMinutes.get())
                etime=str(endHours.get())+':'+str(endMinutes.get())
                stime=stime.split(":")
                stime=list(map(int,stime))
                etime=etime.split(":")
                etime=list(map(int,etime))
                sdate=date.split("-")
                edate=date1.split("-")
                date=Awr_report.yearS(sdate)
                date1=Awr_report.yearS(edate)
                #ftime=input("fT : ")
                #print(Awr_report.root_dict)
                
                if instance!='All':
                    for i in range(len(lst[0])):
                        Dvr=lst[0][i].split("-")
                        Dvr[1]=Awr_report.vrn[Dvr[1]]
                        Dvr=list(map(int,Dvr))
                        sdate=date.split("-")
                        sdate[1]=Awr_report.vrn[sdate[1]]
                        sdate=list(map(int,sdate))
                        #print(Dvr)
                        fileTime1 = datetime.datetime( Dvr[2],Dvr[1],Dvr[0])
                        initTime = datetime.datetime( sdate[2],sdate[1],sdate[0])
                        if fileTime1>=initTime:
                                vr=lst[1][i].split(":")
                                vr=list(map(int,vr))
                                edate=date1.split("-")
                                edate[1]=Awr_report.vrn[edate[1]]
                                edate=list(map(int,edate))
                                Filetime = datetime.datetime( Dvr[2],Dvr[1],Dvr[0] ,hour=vr[0], minute=vr[1], second=vr[2])
                                stim=datetime.datetime(sdate[2],sdate[1],sdate[0],hour=stime[0], minute=stime[1], second=0)
                                etim=datetime.datetime(edate[2],edate[1],edate[0],hour=etime[0], minute=etime[1], second=0)
                    
                                if Filetime>=stim and Filetime<=etim:
                                        #pass
                                        Filetime=str(Filetime).split()
                                        sd=Filetime[0].replace('00','20')
                                        Filetime[0]=sd
                                        Filetime=Filetime[1]+"\n"+Filetime[0]
                                        Awr_report.graphT.append(Filetime)
                                        if baseoptions.get() == 'waitclasses(SG)':
                                                Awr_report.plot.append(filter[i])
                                                Awr_report.gamble=2
                                                #gamble
                                        if baseoptions.get() == 'Memory Statistics':
                                            Awr_report.plot=alpha[5]
                                            Awr_report.gamble=3
                                            #gamble
                                        if baseoptions.get() == 'DB Time':
                                            Awr_report.plot.append(filter[i])
                                            Awr_report.gamble=4
                                            #gamble
                                        if baseoptions.get() == 'waitclasses' or baseoptions.get()== 'foreground event' and baseoptions.get() != 'waitclasses(SG)':
                                            Awr_report.gamble=0
                                            #gamble
                                            for j in range(len(filter[i])):
                                                if baseoptions.get() == 'foreground event':
                                                    try:
                                                        if ch==Awr_report.mainData[j]:
                                                            if filter[i][j]=='':
                                                                Awr_report.plot.append(0.0)
                                                            else:
                                                                Awr_report.plot.append(float(filter[i][j]))       
                                                            break
                                                    except:
                                                        Awr_report.plot.append(0)
                                                if baseoptions.get() == 'waitclasses':
                                                    try:
                                                        if ch==Awr_report.Afk[j]:
                                                            float(filter[i][j])
                                                            Awr_report.plot.append(float(filter[i][j]))
                                                    except:
                                                        Awr_report.plot.append(0)
                                                    
                                                else:
                                                    pass
                #print(Awr_report.graphT)
                if instance=='All' and (baseoptions.get()=='DB Time' or baseoptions.get()=='foreground event'):
                    
                    Awr_report.gamble=5
                    for rnd in jeev:
                        plot=[]
                        graphT=[]
                        lst=Awr_report.root_dict[rnd]
                        alpha=Awr_report.root_dict[rnd]
                        if baseoptions.get()=='DB Time':
                            filter=alpha[6]
                            filterD=alpha[0]
                            filterT=alpha[1]
                        if baseoptions.get()=='foreground event':
                            filter=alpha[3]
                            ch=foreground_event.get()
                            filterD=alpha[0]
                            filterT=alpha[1]
                        for i in range(len(lst[0])):
                            Dvr=lst[0][i].split("-")
                            Dvr[1]=Awr_report.vrn[Dvr[1]]
                            Dvr=list(map(int,Dvr))
                            sdate=date.split("-")
                            sdate[1]=Awr_report.vrn[sdate[1]]
                            sdate=list(map(int,sdate))
                            
                            fileTime1 = datetime.datetime( Dvr[2],Dvr[1],Dvr[0])
                            initTime = datetime.datetime( sdate[2],sdate[1],sdate[0])
                            if fileTime1>=initTime:
                                    vr=lst[1][i].split(":")
                                    vr=list(map(int,vr))
                                    edate=date1.split("-")
                                    edate[1]=Awr_report.vrn[edate[1]]
                                    edate=list(map(int,edate))
                                    Filetime = datetime.datetime( Dvr[2],Dvr[1],Dvr[0] ,hour=vr[0], minute=vr[1], second=vr[2])
                                    stim=datetime.datetime(sdate[2],sdate[1],sdate[0],hour=stime[0], minute=stime[1], second=0)
                                    etim=datetime.datetime(edate[2],edate[1],edate[0],hour=etime[0], minute=etime[1], second=0)
                        
                                    if Filetime>=stim and Filetime<=etim:
                                            #pass
                                            Filetime=str(Filetime).split()
                                            sd=Filetime[0].replace('00','20')
                                            Filetime[0]=sd
                                            Filetime=Filetime[1]+"\n"+Filetime[0]
                                            
                                            if baseoptions.get() == 'DB Time':
                                                plot.append(filter[i])
                                                graphT.append(filterD[i]+' '+filterT[i])
                                                
                                            if baseoptions.get() == 'foreground event':
                                                for j in range(len(filter[i])):
                                                    if ch==Awr_report.mainData[j]:
                                                        try:
                                                            float(filter[i][j])
                                                            if filter[i][j]!='':
                                                                plot.append(float(filter[i][j]))
                                                        except:
                                                            plot.append(0)
                                                        graphT.append(filterD[i]+' '+filterT[i] )
                                                        break
                                                
                        Awr_report.plot.append(plot)
                        Awr_report.graphT.append(graphT)
                                                #gamble
#
#   Graph Code!
#
#
                numricdata=[]
                #print(Awr_report.graphT)
                
                
                #print(Awr_report.plot)
                #print(Awr_report.gamble)
                fig = plt.figure(figsize=(8, 4), dpi=100)
                plt.tight_layout()

                if Awr_report.gamble==0:
                    #print("Linear Graph")
                    inc_out=0
                    lngth_out=len(Awr_report.plot)
                    while inc_out!=lngth_out:
                        if Awr_report.plot[inc_out]=='':
                                Awr_report.plot[inc_out]=0
                        
                        inc_out+=1
                    a=Awr_report.graphT
                    for i in range(len(a)):
                           a[i] = dateF.dateFilterNA(a[i])
                    Awr_report.graphT=a
                    plt.clf()
                    plt.plot(Awr_report.graphT,Awr_report.plot, label='Instance '+xx)
                    myFmt = mdates.DateFormatter('%Y-%m-%d\n%H:%M')
                    plt.gca().xaxis.set_major_formatter(myFmt)
                    plt.xlabel('x')
                    plt.ylabel('Avg. Wait Time')
                    plt.xticks(fontsize=6,rotation=45) 
                    plt.legend()
                    plt.title(foreground_event.get())
                    plt.xticks(fontsize=6,rotation=45)
                    plt.subplots_adjust(bottom=0.25,top=0.85)
                    if show=='fullscreen':
                        fig.show()
                    else:
                        canvas = FigureCanvasTkAgg(fig, master=window)
                        canvas.get_tk_widget().grid(row=6,column=0,columnspan=12)
                    
                    Awr_report.plot=[]
                    Awr_report.graphT=[]
                    
                if Awr_report.gamble==2:
                    #print("Stack Graph")
                    a=Awr_report.plot
                    for i in range(len(a)):
                        for j in range(len(a[i])):
                            if a[i][j]=='':
                                a[i][j]='0'
                            else:
                                a[i][j]=float(a[i][j])
                    
                    plt.clf()
                    Network = [float(i[0]) for i in a]
                    Concurrency = [float(i[1]) for i in a]
                    Other = [float(i[2]) for i in a]
                    DBCPU = [float(i[3]) for i in a]
                    SystemIO = [float(i[4]) for i in a]
                    UserIO = [float(i[5]) for i in a]
                    Application = [float(i[6]) for i in a]
                    Cluster = [float(i[7]) for i in a]
                    Commit = [float(i[8]) for i in a]
                    Configuration = [float(i[9]) for i in a]
                    Administrative = [float(i[10]) for i in a]
                    
                    colors=['blue','orange','green','red','purple','brown','pink','gray','olive','cyan','lime']
                    all_variables=[Network,Concurrency,Other,DBCPU,SystemIO,UserIO,Application,Cluster,Commit,Configuration]
                    all_variables_name=['Network','Concurrency','Other','DBCPU','SystemIO','UserIO','Application','Cluster','Commit','Configuration']
                    for i in range(len(all_variables_name)):
                        plt.plot([],[],color=colors[i],label=all_variables_name[i])
                    a=Awr_report.graphT
                    for i in range(len(a)):
                           a[i] = dateF.dateFilterNA(a[i])
                    Awr_report.graphT=a
                    plt.stackplot(Awr_report.graphT,*all_variables)
                    myFmt = mdates.DateFormatter('%Y-%m-%d\n%H:%M')
                    plt.gca().xaxis.set_major_formatter(myFmt)
                    plt.legend()
                    plt.title(foreground_event.get())
                    plt.xticks(fontsize=6)
                    plt.subplots_adjust(bottom=0.25,top=0.85)
                    plt.xlabel('x')
                    plt.ylabel('Avg. Wait Time')
                    plt.xticks(fontsize=6,rotation=30)
                    #plt.show()
                    if show=='fullscreen':
                        fig.show()
                        
                    else:
                        
                        canvas = FigureCanvasTkAgg(fig, master=window)
                        canvas.get_tk_widget().grid(row=6,column=0,columnspan=12)
                    

                if Awr_report.gamble==3:
                    plt.clf()
                    switch=Awr_report.plot[0]
                    sample=Awr_report.plot
                    sample[0]=Awr_report.plot[0]-Awr_report.plot[1]-Awr_report.plot[2]

                    
                    _label = ['Total Memory', 'SGA', 'PGA']
                    sizes = sample
                    
                    Awr_report.plot[0]=switch
                    
                    wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
                    plt.pie(sizes,labels=_label, explode = [0.1,0.2,0.3],shadow=True, wedgeprops = wp,autopct='%1.1f%%')
                    plt.xticks(fontsize=6)
                    plt.title(foreground_event.get())
                    plt.xlabel('Avg. Wait Time(%)')
                    plt.xticks(fontsize=6,rotation=45)
                    if show=='fullscreen':
                        fig.show()
                    else:
                        canvas = FigureCanvasTkAgg(fig, master=window)
                        canvas.get_tk_widget().grid(row=6,column=0,columnspan=12)
                    sample=[]

                if Awr_report.gamble==4:
                    
                    inc_out=0
                    lngth_out=len(Awr_report.plot)
                    while inc_out!=lngth_out:
                        if Awr_report.plot[inc_out]=='':
                                Awr_report.plot[inc_out]=0
                        
                        inc_out+=1
                    
                    a=Awr_report.graphT
                    for i in range(len(a)):
                           a[i] = dateF.dateFilterNA(a[i])
                    Awr_report.graphT=a
                    plt.clf()
                    
                    plt.plot(Awr_report.graphT,Awr_report.plot, label='Instance '+xx)
                    myFmt = mdates.DateFormatter('%Y-%m-%d\n%H:%M')
                    plt.gca().xaxis.set_major_formatter(myFmt)
                    plt.title(foreground_event.get())
                    plt.xlabel('x')
                    plt.ylabel('Avg. Wait Time')
                    plt.xticks(fontsize=6,rotation=45)
                    plt.legend()
                    plt.subplots_adjust(bottom=0.25,top=0.85)
                    if show=='fullscreen':
                        fig.show()
                    else:
                        canvas = FigureCanvasTkAgg(fig, master=window)
                        canvas.get_tk_widget().grid(row=6,column=0,columnspan=12)
                    
                                        
                    Awr_report.plot=[]
                    Awr_report.graphT=[]


                if Awr_report.gamble==5:
                    pass
                
                    inc_out=0
                    lngth_out=len(Awr_report.plot)
                    while inc_out!=lngth_out:
                        if Awr_report.plot[inc_out]=='':
                                Awr_report.plot[inc_out]=0
                        #print(Awr_report.plot[inc_out])
                        inc_out+=1
                    #print('All-Awr_report.graphT :---',Awr_report.graphT,'\n','Awr_report.plot:---',Awr_report.plot)
                    a=Awr_report.graphT
                    for i in range(len(a)):
                        for j in range(len(a[i])):
                           a[i][j] = dateF.dateFilter(a[i][j])
                    Awr_report.graphT=a
                    j=1
                    for i in range(len(Awr_report.plot)):
                        #print(i)
                        plt.plot(Awr_report.graphT[i],Awr_report.plot[i], label='Instance '+str(i+1))
                        j+=1
                    plt.xlabel('x')
                    plt.ylabel('Avg. Wait Time')
                    plt.legend()
                    plt.title(foreground_event.get())
                    plt.xticks(fontsize=6,rotation=45)
                    plt.subplots_adjust(bottom=0.25,top=0.85)
                    if show=='fullscreen':
                        fig.show()
                    else:
                        canvas = FigureCanvasTkAgg(fig, master=window)
                        canvas.get_tk_widget().grid(row=6,column=0,columnspan=12)
                    
                    
                    Awr_report.plot=[]
                    Awr_report.graphT=[]



                
                Awr_report.graphT=[]
                Awr_report.plot=[]
                            

class upload_files:
    def start_init(self,root):
        
        #self.progress_counter = tk.StringVar()
        #self.progress_counter.set("0%")
        ttk.Label(root, text = "!! Select Folder !!", 
                            font = ("Times New Roman", 25)).grid(row=1,padx=200,pady=25)
 
        label = tk.Label(root, text = '0%', 
                            font = ("Times New Roman", 15))
        label.grid(column = 0, row = 3, padx = 10, pady = 25)


        self.btn = tk.Button(root,width=20 ,text = 'UPLOAD',command = lambda: self.select_folder(label,root) )
        self.btn.grid(column = 0 , row = 2, pady = 25)
        #root.withdraw()



    def select_folder(self,label,root):
        self.path_work = filedialog.askdirectory()
        
        self.ch='1'
        counter=0
        for subdir, dirs, files in os.walk(self.path_work):
                    numberOfFiles = len(files)
                    self.percent=int(100/numberOfFiles)
                    for file in files:
                        if (file)[-4:] == "html":
                            counter+=self.percent
                            
                            label.config(text=str(counter)+'%')
                            
                            root.update_idletasks()
                            #self.progress_counter.set(str(counter)+'%')
                            #root.after(100, update_label)
                            self.obj1 = Awr_report()
                            self.obj1.get_data(self.path_work+'/'+file,self.ch)
                        else:
                            continue
                    #print(Awr_report.root_dict)
        root.destroy()
        self.gui_call()
        
    def gui_call(self):
        self.gui = GUI()

file_upload = upload_files()
root = tk.Tk()
root.title('WINDOW') 
root.geometry('600x350')
root.resizable(False, False)
file_upload.start_init(root)
root.update()

