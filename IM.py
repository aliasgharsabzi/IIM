import copy
import random
import math
from conflict1 import Intersection
from G_car import G_car
from Read_write_Infile import writefile, clear_file,main_readfile, Runs, readfile_Runs, Average, write_AVG_kol
from ChangeLine import position
from turn import turn
import time
from draw import draw
from ACC import safety_dis
from RunAVG import Calculat_AVG 
from MCTS import mcts
from plot_result import plot_result

conf_kol=[]

def priority(e):             
    return(e[0][1])


def clculat(om1,om0,conf_kol,t,delay,delaynew,Num_change,X_kol,Y_kol,line_kol,angle,drop,
            AVG_pri1,AVG_pri2,runtime_IM,lastTime,case):
    om1_new=[]
    t_c=0
    current_x=[]
    current_y=[]
    current_line=[]
    current_angle=[]
    
# ************************* check safe distance*************
    om1,om0=safety_dis(om1,om0)
    
# *********************end**********
#     om0_new=[]
#     temp_om1=copy.deepcopy(om1)
    i=0
    while i<len(om1):
        item=om1[i]
        if item[1]in [76,73,82,91,910,109,106,115,124,121]:
            if item[4]>=160:
                item[4]=item[4]-((item[3]*StepTime))
                i=i+1
            else:
                item[4]=item[4]-((item[3]*StepTime))
                item[6]=((item[4]-60)/item[3])+t
                om1_new.append(item)
                c=om1.index(item)
                om1.pop(c)
        else:
            if item[4]<=-100:
                item[4]=item[4]+((item[3]*StepTime))
                i=i+1
            else:
                item[4]=item[4]+((item[3]*StepTime))
                item[6]=-1*((item[4])/(item[3]))+t
                om1_new.append(item)
                c=om1.index(item)
                om1.pop(c)
        current_line.append(item[1])
        if item[1] in [112,19,28,34,37,76,73,82,910,91]:
            current_angle.append(math.radians(90))
        else:
            current_angle.append(math.radians(0))
        if item[1] in[43,412,511,610,67,109,106,115,124,121]:
            current_y.append(item[4])
            current_x.append(item[5])
        else:
            current_y.append(item[5])
            current_x.append(item[4])     
    print('om1:',om1)
    print('om1_new:',om1_new)
    i=0
    while i<len(om0):
        item=om0[i]
        if item[1]in [76,73,82,91,910,109,106,115,124,121]:
            if item[1]==76 and item[5]<0:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[1]==109 and item[5]>60:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[1]==910 and item[5]>60:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[1]==121 and item[5]<0:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[4]<0:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            if t >= item[6]:
                if item[1] in [76,910,109,121]:
                    item=turn(item)
                    i=i+1
                else:
                    item[4]=item[4]-item[7]*StepTime
                    i=i+1
            else:
#                x_t=((A0*(t**3))/6)+((1/2)*B0*(t**2))+v_0*t+x_0
                t_c=t-item[2]
                item[4]=((item[8]*(t_c**3))/6)+((1/2)*item[9]*(t_c**2))-item[3]*t_c+item[10]
                item[5]=position(item)
                i=i+1
#                  v_t=(A0*(t**2)/2)+(B0*t)+v_0
#                 print(abs((item[8]*(t_c**2)/2)+(item[9]*t_c)-item[3]))
#                 mkl=input("dfg")
#                 if abs((item[8]*(t_c**2)/2)+(item[9]*t_c)-item[3])<11.2 or abs((item[8]*(t_c**2)/2)+(item[9]*t_c)-item[3])>22.5 :
#                     print((item[8]*(t_c**2)/2)+(item[9]*t_c)-item[3])
#                     mkl=input("dfg")
        else:
            if item[1]==112 and item[5]>60:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[1]==43 and item[5]<0:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[1]==34 and item[5]<0:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[1]==67 and item[5]>60:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            elif item[4]>60:
                timeInter=item[0]
                timeInter=float(timeInter[2:])
                delaynew.append(t-timeInter+(200/22.3))
                c=om0.index(item)
                om0.pop(c)
            if t >= item[6]:
                if item[1] in [112,67,34,43]:
                    item=turn(item)
                    i=i+1
                else:    
                    item[4]=item[4]+item[7]*StepTime
                    i=i+1
            else:
                t_c=t-item[2]
                item[4]=((item[8]*(t_c**3))/6)+((1/2)*item[9]*(t_c**2))+item[3]*t_c+item[10]
#                 print((0.5*item[8]*(t_c**2))+(item[9]*t_c)+22.3,t_c,item)
#                 input("velocity_current")
                item[5]=position(item)
                i=i+1
#                 item.append((item[7]*(t_c**2)/2)+(item[8]*t_c)+item[3])
#                 item[4]=item[4]+item[3]
#                 print(((item[8]*(t_c**2)/2)+(item[9]*t_c)+item[3]))
#                 mkl=input("dfg")
#                 if ((item[8]*(t_c**2)/2)+(item[9]*t_c)+item[3])<11.2 or ((item[8]*(t_c**2)/2)+(item[9]*t_c)+item[3])>22.5 :
#                     print((item[8]*(t_c**2)/2)+(item[9]*t_c)+item[3])
#                     mkl=input("dfg0")
        current_line.append(item[1])
#         current_angle.append(item[11])
        if item[1] in [112,19,28,34,37,76,73,82,910,91]:
            if t >= item[6] and item[1] in [112,34,76,910]:
                current_angle.append(item[11])
            else:
                current_angle.append(math.radians(90))
        else:
            if t >= item[6] and item[1] in [43,67,109,121]:
                current_angle.append(item[11])
            else:
                current_angle.append(math.radians(0))

        if item[1] in[43,412,511,610,67,109,106,115,124,121]:
            current_y.append(item[4])
            current_x.append(item[5])
        else:
            current_y.append(item[5])
            current_x.append(item[4])
           
#     om0,conf_kol,om0_sch=optimal_time(om1_new, om0,conf_kol,t)
    if current_x!=[] and current_y!=[]:
        angle.append(current_angle)
        line_kol.append(current_line)
        X_kol.append(current_x)
        Y_kol.append(current_y)
#         for i in range(len(current_x)):
#             X_kol.append(current_x[i])
#             Y_kol.append(current_y[i])
    if om1_new !=[]:
        keep_high_priority=[]
        if case in [5,6,7,8] and len(om1_new)>1:
#         if case in [1] and len(om1_new)>1:
            cost_time=100
            temp_om1_new=copy.deepcopy(om1_new)
            temp_om0=copy.deepcopy(om0)
            if case in [7,8]:
                if len(temp_om1_new)>1:
                    temp_om1_new.sort(reverse=True,key=priority)
                    temp_om1_new=copy.deepcopy(temp_om1_new)     
                    print(temp_om1_new)
                i=0
                while i<(len(temp_om1_new)):
                    if temp_om1_new[i][0][1] in ['1','2']:
                        keep_high_priority.append(temp_om1_new[i])
                        temp_om1_new.pop(i)
                        i=i-1
                    i=i+1
                print("keep_high_priority:",keep_high_priority)
                print("temp_om1_new:",temp_om1_new)
            if len(temp_om1_new)>1:
                obj_om1_new=mcts(temp_om1_new,temp_om0,t,lastTime)
                temp_om1_new=obj_om1_new.run(cost_time)
#             for i in range(len(om1_new)):
#                 if temp_om1_new[i]!=om1_new[i]:
#                     print("change priority")
            for item in temp_om1_new:
                keep_high_priority.append(item)
            om1_new=copy.deepcopy(keep_high_priority)
            print("om1_new after assign priority:",om1_new)
        om0,delay,Num_change,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime=Intersection(om1_new,om0,t,Num_change,om1,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime,case)
    print("om0:",om0) 
    return (om1,om0,om0_sch,delay,delaynew,Num_change,X_kol,Y_kol,line_kol,angle,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime)
            
all_vehicle=0
# d={}
# f=open('sample.txt','w')   
# f=open("sample.json", "w") 
clear_file()
# Rate=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
Rate=[0.01]
iteration = 1
num_case_experiment = [0,1,2,3,4,5,6,7,8]
# num_case_experiment = [0,3]
for rate  in Rate:
    for loop in range(iteration):
        for case in num_case_experiment:
#             input("promptAli")
            start_time = time.time()
            om1=[]
            om0=[]
            sch3=[]
            om0_sch=[]
            lastTime={112:0,19:0,28:0,37:0,34:0,43:0,412:0,511:0,610:0,67:0,76:0,73:0,82:0,91:0,910:0,109:0,106:0,115:0,124:0,121:0}
            min_v=11.2
            max_v=22.3
            delaynew=[]
            d=[]
            Num_change=0
            SimulationTime=360
            t=0
            counterTime=0
            count=1
            threshold=1/rate
            StepTime = 0.1
            c=0
            drop=0
            AVG_pri1=[]
            AVG_pri2=[]
#             GeneratedCarTimeStamp=[1,1,1,1,1,1,1,1,1,1,1,1]
            GeneratedCarTimeStamp=[0,0,0,0,0,0,0,0,0,0,0,0]
#             GeneratedCarTimeStamp=[1000,1000,1,1000,1000,1000,1000,1000,1000,1000,1000,1000]
            temp=[]
            X_kol=[]
            Y_kol=[]
            line_kol=[]
            angle=[]
            runtime_IM_list=[]
            fail=0
            
#             if case == 0 or 0 not in num_case_experiment:
#                 for i in range(len(GeneratedCarTimeStamp)):
#                     GeneratedCarTimeStamp[i]=threshold*GeneratedCarTimeStamp[i]*random.random()
# #                     GeneratedCarTimeStamp[i]=GeneratedCarTimeStamp[i]+0.2
#                 print(GeneratedCarTimeStamp)
# 
#             else:
#                 input('prompt')
#                 print("*"* 150)
# #                 loop=0
#                 data=readfile_Runs(loop)
#                   print(data)
            
            if case in [1,2,3,4,5,6,7,8]:
                print("*"* 150)
#                 loop=0
                data=readfile_Runs(loop)
        #         print(data)
            else:
                for i in range(len(GeneratedCarTimeStamp)):
                    GeneratedCarTimeStamp[i]=threshold*GeneratedCarTimeStamp[i]*random.random()
#                     GeneratedCarTimeStamp[i]=GeneratedCarTimeStamp[i]+0.2
                print(GeneratedCarTimeStamp)
        
        
            while(t<=SimulationTime):
                runtime_IM=0
                t=count*StepTime
                line_num=[]
                if t<310:
                    if case==0:
                        for i in range(len(GeneratedCarTimeStamp)):
                            if t>=GeneratedCarTimeStamp[i]:
                                line_num.append(i+1)
                                GeneratedCarTimeStamp[i]=t+threshold+random.random()
#                                 GeneratedCarTimeStamp[i]=GeneratedCarTimeStamp[i]+10
                        om1,all_vehicle,temp=G_car(om1,t,all_vehicle,line_num)
                        writefile(temp,t)
                    else:
                        om1=main_readfile(om1,counterTime,data)
                    print("Time:",t,line_num)
                    
                    delay=[]
                    om1,om0,om0_sch,delay,delaynew,Num_change,X_kol,Y_kol,line_kol,angle,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime=clculat(om1,om0,conf_kol,t,delay,delaynew,
                                                                                           Num_change,X_kol,Y_kol,line_kol,angle,drop,AVG_pri1,AVG_pri2,
                                                                                           runtime_IM,lastTime,case)
                    d=d+delay
                    runtime_IM_list.append(runtime_IM)
                    fail+=drop
                    drop=0
                    om0_sch = copy.deepcopy(om0_sch)
                    sch3.append([i for i in om0_sch])
        #             write_for_check(om1,om0,counterTime)
            #         sch3.extend(om0_sch)
                
                else:
                    print("Time:",t)
                    delay=[]
                    om1,om0,om0_sch,delay,delaynew,Num_change,X_kol,Y_kol,line_kol,angle,drop,AVG_pri1,AVG_pri2,runtime_IM,lastTime=clculat(om1,om0,conf_kol,t,delay,delaynew,
                                                                                           Num_change,X_kol,Y_kol,line_kol,angle,drop,AVG_pri1,AVG_pri2,
                                                                                           runtime_IM,lastTime,case)
                    d=d+delay
#                     print("AVG_pri1,AVG_pri2",AVG_pri1,AVG_pri2)
                    runtime_IM_list.append(runtime_IM)
                    fail+=drop
                    drop=0
        #             om0_sch = copy.deepcopy(om0_sch)
        #             sch3.append([i for i in om0_sch])
        #             write_for_check(om1,om0,counterTime)
                            
                count+=1
                counterTime+=1
            if case==0:    
                Runs(loop)
            end_time=time.time()
            runtime=(end_time - start_time)
            print("allvehicle:",all_vehicle)
            AVG=0
            counter=0
            for avg in d:
                if avg>=0:
                    AVG+=avg
                    counter+=1
                    
            print(len(d),d,AVG,counter) 
            print("sum of vehicle:",counter,"index max delay:",d.index(max(d)),"max delay:",max(d))
            AVG=AVG/counter
            print("AVG:",AVG)  
            ldnew=len(delaynew)
            av=0
            for i in range(ldnew):
                av+=delaynew[i]
            av=av/ldnew
            print("AVG travel time:",av)
            print("d new:",delaynew)
            sum1=0
            sum2=0
            len_pri1=len(AVG_pri1)
            len_pri2=len(AVG_pri2)
            for i in range(len_pri1):
                sum1+=AVG_pri1[i]
            for i in range(len_pri2):
                sum2+=AVG_pri2[i]
            if len_pri1 !=0:
                sum1=sum1/len_pri1
            if len_pri2 !=0:
                sum2=sum2/len_pri2
            print("AVG_priority1:",sum1)
            print("AVG_priority2:",sum2)
            print("Number of change line:",Num_change)
            sum_runtime_IM=0
            for i in range(len(runtime_IM_list)):
                sum_runtime_IM+=runtime_IM_list[i]
            Average(loop,counter,AVG,av,Num_change,runtime,sum1,sum2,sum_runtime_IM,fail,len_pri1,len_pri2)
            print("all of the X:",X_kol)
            numberkol=all_vehicle
        #     for i in X_kol:
        #         if i<-197.77 or 257.77<i:
        #             numberkol+=1
        #     for i in Y_kol:
        #         if i<-197.77 or 257.77<i:
        #             numberkol+=1
        #     print(numberkol)        
            print("all of the Y:",Y_kol)
            print("all of the line:",line_kol)
        #     print(len(X_kol),len(Y_kol), len(angle))
            print("all of the angle:",angle)
            print("fail:",fail)
            print("runtime_IM:",runtime_IM_list)
            print(len(runtime_IM_list),sum_runtime_IM,runtime)
#     input("ali")
    AVG_kol=Calculat_AVG(rate, num_case_experiment)
    write_AVG_kol(AVG_kol,rate)
plot_result()
#     for i in AVG_kol:
#         print(i)

# draw(X_kol,Y_kol,numberkol,line_kol,angle)

# print("--- %s seconds ---" %runtime )
           
# NUM, AVG_delay, timeTrip, num_CL, excutionTime_kol, delay_first_priority, delay_second_priority, excutionTime_IM, fail  





            

