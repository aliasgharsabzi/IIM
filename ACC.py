from ChangeLine import determination_line


def control_distance(m,last_om1):
#     hg=0
    l_lom1=len(last_om1)
    temp_line=determination_line(m[1])
    V_R=0
    print(last_om1)
    if last_om1!=[]:
        for i in range(l_lom1-1,-1,-1):
            if last_om1[i][1] in temp_line:
                distance_safe=((m[3]*3600)/15000)*6
                d=(abs(m[4])-abs(last_om1[i][4]))
                print(d)
                if d<= distance_safe:
                    m[3]=(d/1.44)*10
                    print(m[3],m)
                    n=input("prompt120")
#                 if d>=100:
#                     d=99
#                 V_R=(96.76*last_om1[i][3])/(100-d)
# #                             V_R=(82/((last_om1[i][4]-160)/last_om1[i][3]))
#                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@V_R",V_R,d,m,last_om1[i])
#                 if V_R<m[3]:
#                     m[3]=V_R
#                     n=input("vvvvvvvvv")
#                 elif V_R>22.3:
#                     m[3]=22.3
            
            break
                    
    return(m)
def safety_dis(om1,om0):
    om=om1+om0
    for item in om1:
        for item2 in om:
            temp_line=determination_line(item2[1])
            if item[1] in [76,73,82,91,910,109,106,115,124,121]:
                if item[0]!=item2[0] and item[1] in temp_line and item[4]>item2[4]:
                    distance_safe=round((((item[3]*3600)/15000)*6)*0.1,1)
                    d=round(abs(item[4]-item2[4]),1)
#                     print(item[3],item2[3])
                    print("d=",d,"distance_safe:",distance_safe)
                    if d<distance_safe:
                        v=(d/1.44)*10
                        if v>22.3:
                            item[3]=22.3
                        else:
                            item[3]=v
#                         print(item,item2)
                        print("d=",d,"distance_safe:",distance_safe)
#                         n=input("asd0")
                        break
            elif item[0]!=item2[0] and item[1] in temp_line and abs(item[4]-60)>abs(item2[4]-60):
                if om0!=[]:
                    print(om0)
                distance_safe=round((((item[3]*3600)/15000)*6)*0.1,1)
                d=round(abs(item[4]-item2[4]),1)
                print(item[3],item2[3])
                print("d=",d,"distance_safe:",distance_safe)
                if d<distance_safe:
                    v=(d/1.44)*10
                    if v>22.3:
                        item[3]=22.3
                    else:
                        item[3]=v
                    print(item,item2)
                    print("d=",d,"distance_safe=",distance_safe,"v_new=",item[3])
#                     n=input("asd1")
                    break 
#     for item in om0:
#         for item2 in om0:
#             temp_line=determination_line(item2[1])
#             if item[1] in [76,73,82,91,910,109,106,115,124,121]:
#                 if item[0]!=item2[0] and item[1] in temp_line and item[4]>item2[4]:
#                     distance_safe=((item[3]*3600)/15000)*6
#                     print(item[3],item2[3])
#                     if(abs(item[4]-item2[4]))<distance_safe:
#     #                     item[3]=item2[3]
#                         print(item,item2)
#                         print(abs(item[4]-item2[4]),distance_safe)
#                         n=input("asd20")
# #                         break
#                 elif item[0]!=item2[0] and item[1] in temp_line and abs(item[4]-60)>abs(item2[4]-60):
#                     distance_safe=((item[3]*3600)/15000)*6
#                     print(item[3],item2[3])
#                     if(abs(item[4]-item2[4]))<distance_safe:
#     #                     item[3]=item2[3]
#                         print(item,item2)
#                         print(abs(item[4]-item2[4]),distance_safe)
#                         n=input("asd21")
#                         break  
    return(om1,om0)
    
    
    
    
    
    