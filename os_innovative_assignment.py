# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:06:13 2022

@author: vivek
"""

while True:
    print()
    print("*****************")
    print("CHOOSE ANY ONE:")
    print("*****************")
    print("1) FCFS        ")
    print("*****************")
    print("2) SJF         ")
    print("*****************")
    print("3) SRTF        ")
    print("*****************")
    print("4) RR          ")
    print("*****************")
    print("5) EXIT        ")
    print("*****************")
    c=int(input("ENTER YOUR CHOICE : "))
    if c==1:
        f=open("input.txt","r")
        lst = f.read().splitlines()
        sprocess = sorted(lst)
        number = len(sprocess)
        proc= []
        sow=0
        sor=0
        sot=0
        pr=0
        ctr=[]
        thrp=0
        print("arrive_time burst_time process completion_time tat waiting_time response_time")
        prevEnd=wt=tat=ct=0
        for i in sprocess:
            arr=i.split(" ")
            ct=(max(prevEnd,int(arr[0])))+int(arr[1])
            arr.append(ct)
            tat=ct-int(arr[0])
            arr.append(tat)
            wt=tat-int(arr[1])
            arr.append(wt)
            rt=ct-int(arr[1])-int(arr[0])
            arr.append(rt)
            pr= rt + int(arr[0])
            proc.append(pr)
            ctr.append(ct)
            sow=sow+wt
            sot=sot+tat
            sor=sor+rt
            prevEnd=ct
            print("    ",arr[0],"      ",arr[1],"        ",arr[2],"          ",arr[3],"       ",arr[4],"   ",arr[5],"         ",arr[6])
            thrp=int(arr[3])
        print(" ")

        print("avarage turn around time : ",sot/number)
        print("avarage waiting time : ", sow/number)
        print("avarage response time : ",sor/number)
        print("overall throughput : ",thrp/number)
        print()
        print("gantt chart :")
        print("|",end=" ")
        count=0
        spc=0
        for l in sprocess:
            spc = int(l[2])
            while spc>0:
                print(" ",end="")
                spc=spc-1
            print(l[4],end="")
            print("|",end="")
            count=count+1
        print()
        print("  ",end=" ")
        k=0
        for l in sprocess:
            spc = int(l[2])
            while spc>0:
                print(" ",end="")
                spc=spc-1
            print(ctr[k],end=" ")
            count=count+1
            k=k+1

    elif c==2:
        f=open("input.txt","r")
        class obj: 
            def __init__(self,at,bt,pr): 
                self.at = at 
                self.bt = bt
                self.pr = pr
            ct=0
            tat=0
            wt=0
            rt=0
            st=0

        lst = f.read().splitlines()
        sprocess = sorted(lst)
        number=len(sprocess)
        loo=[]
        p=0
        q=0
        r=0
        for i in sprocess:
            m = obj(i[0],i[2],i[4])
            loo.append(m)

        for obj in loo:
            print( obj.at, obj.bt,obj.pr, sep =' ' )
        proc = []
        x=0
        burst=0
        temp=[]
        for i in range(99):
            for m in loo:
                if int(m.at)==i:
                    if x==0:
                        m.st = int(i)
                        burst=m.bt
                        x=1
                    else:
                        temp.append(m)
            burst=int(burst)-1
            if burst>=0:
                continue
            x=0
            minimum=10000
            for m in temp:
                if minimum>int(m.bt):
                    minimum=int(m.bt)
            for m in temp:
                if minimum==int(m.bt):
                    burst = int(m.bt)-1
                    m.st = int(i)
                    temp.remove(m)
                    x=1
        for m in loo:
            m.ct=int(m.st)+int(m.bt)
            m.tat=int(m.ct)-int(m.at)
            m.wt=int(m.tat)-int(m.bt)
            m.rt=int(m.st)-int(m.at)
        newlist = sorted(loo, key=lambda x: x.ct)   
        print("process      arrival           burst         completion         waiting          tat        response")
        sor=0
        thrp=0
        for m in newlist:
            print(m.pr,"\t\t", m.at,"\t\t", m.bt,"\t\t", m.ct,"\t\t", m.wt,"\t\t", m.tat,"\t\t", m.rt)
            sor=sor+m.rt
            thrp=m.ct
        print()
        sow=0
        sot=0
        for m in newlist:
            sow = sow+int(m.wt)
            sot = sot+int(m.tat)
        print("avarage waiting time : ",sow/number)
        print("avarage turn around time : ",sot/number)
        print("avarage response time : ",sor/number)
        print("overall throughput : ",thrp/number)
        print()
        print("gantt chart :")
        print("|",end="")
        spc=0
        for m in newlist:
            spc=int(m.bt)
            while spc>0:
                print(" ",end="")
                spc=spc-1
            print(m.pr,end="")
            print("|",end="")
        print(" ")
        for m in newlist:
            spc=int(m.bt)
            while spc>0:
                print(" ",end="")
                spc=spc-1
            print(" ",end="")
            print(m.ct,end="")
    elif c==3:
        class SJF:
            def sp(process_data):
                start_time = []
                exit_time = []
                s_time = 0
                sequence_of_process = []
                process_data.sort(key=lambda x: x[1])
                while 1:
                    ready_queue = []
                    normal_queue = []
                    temp = []
                    for i in range(len(process_data)):
                        if int(process_data[i][1]) <= s_time and int(process_data[i][3]) == 0:
                            temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                            ready_queue.append(temp)
                            temp = []
                        elif int(process_data[i][3]) == 0:
                            temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                            normal_queue.append(temp)
                            temp = []
                    if len(ready_queue) == 0 and len(normal_queue) == 0:
                        break
                    if len(ready_queue) != 0:
                        ready_queue.sort(key=lambda x: int(x[2]))
                        start_time.append(s_time)
                        s_time = s_time + 1
                        e_time = s_time
                        exit_time.append(e_time)
                        sequence_of_process.append(ready_queue[0][0])
                        for k in range(len(process_data)):
                            if int(process_data[k][0]) == int(ready_queue[0][0]):
                                break
                        process_data[k][2] = int(process_data[k][2]) - 1
                        if int(process_data[k][2]) == 0:
                            process_data[k][3] = 1
                            process_data[k].append(e_time)
                    if len(ready_queue) == 0:
                        if s_time < int(normal_queue[0][1]):
                            s_time = int(normal_queue[0][1])
                        start_time.append(s_time)
                        s_time = s_time + 1
                        e_time = s_time
                        exit_time.append(e_time)
                        sequence_of_process.append(normal_queue[0][0])
                        for k in range(len(process_data)):
                            if int(process_data[k][0]) == int(normal_queue[0][0]):
                                break
                        process_data[k][2] = int(process_data[k][2]) - 1
                        if int(process_data[k][2]) == 0:        #If Burst Time of a process is 0, it means the process is completed
                            process_data[k][3] = 1
                            process_data[k].append(e_time)
                t_time = SJF.caltat(process_data)
                w_time = SJF.cwt(process_data)
                SJF.pd(process_data, t_time, w_time, sequence_of_process)

            def caltat(process_data):
                total_turnaround_time = 0
                for i in range(len(process_data)):
                    turnaround_time = int(process_data[i][5]) - int(process_data[i][1])
                    total_turnaround_time = total_turnaround_time + turnaround_time
                    process_data[i].append(turnaround_time)
                average_turnaround_time = total_turnaround_time / len(process_data)
                return average_turnaround_time

            def cwt(process_data):
                total_waiting_time = 0
                for i in range(len(process_data)):
                    waiting_time = int(process_data[i][6]) - int(process_data[i][4])
                    total_waiting_time = total_waiting_time + waiting_time
                    process_data[i].append(waiting_time)
                average_waiting_time = total_waiting_time / len(process_data)
                return average_waiting_time

            def pd(process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
                process_data.sort(key=lambda x: x[0])
                print("Process_ID  Arrival_Time  Rem_Burst_Time      Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
                for i in range(len(process_data)):
                    for j in range(len(process_data[i])):
                        print(process_data[i][j], end="\t\t\t\t")
                    print()
                    print()
                print(f'Average Turnaround Time: {average_turnaround_time}')
                print(f'Average Waiting Time: {average_waiting_time}')
                print(f'Gantt chart : {sequence_of_process}')
        process=[]
        f=open("input.txt","r")
        lst = f.read().splitlines()
        for i in lst:
            process.append(i.split(" "))
        process_data = []
        for i in process:
            temporary = []
            temporary.extend([i[2],i[0],i[1],0,i[1]])
            process_data.append(temporary)
        SJF.sp(process_data)
        no_of_processes = len(lst)
        sjf = SJF()
    elif c==4:
        f=open("input.txt","r")
        lst = f.read().splitlines()
        sprocess = sorted(lst)
        print(sprocess)
        no_of_processes = int(len(sprocess))
        process_data = []
        for i in sprocess:
            temp = []
            a = i.split(" ")
            process_id = int(a[2])
            arrival_time = int(a[0])
            burst_time = int(a[1])
            temp.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temp)
        time_slice = int(input("--> Time Slice: "))
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)    
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            ct=process_data[i][5]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        process_data.sort(key=lambda x: x[0])
        print("Process_ID  Arrival_Time  Rem_Burst_Time   Completed  Original_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="               ")
            print()
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print("overall throughput: ",ct/len(sprocess))
        print(f'gantt chart: {executed_process}')

    elif c==5:
        break