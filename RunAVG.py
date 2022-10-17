import json
# json_data=[]
# avgD=0
# avgD_CL=0
# avg_pri1=0
# avg_pri2=0
# c=0
# c_CL=0
# avgT=0
# avgT_CL=0
# avg_pri1_A=0
# avg_pri2_A=0
# runtime_IM=0
# runtime_IM_CL=0
# file = open("Average.json", "r")
# for line in file:
#     json_line = json.loads(line)
#     for i in json_line:
#         json_data.append(json_line[i])
# file.close()
# print(json_data)
# for i in range(0,len(json_data),5):
#     for j in range(5):
#         if j==1:
#             c=c+1
#             avgD+=json_data[i][1]
#             avgT+=json_data[i][2]
#             avg_pri1+=json_data[i][5]
#             avg_pri2+=json_data[i][6]
#             runtime_IM+=json_data[i][7]
#         elif(j==4):
#             c_CL=c_CL+1
#             avgD_CL+=json_data[i][1]
#             avgT_CL+=json_data[i][2]
#             avg_pri1_A+=json_data[i][5]
#             avg_pri2_A+=json_data[i][6]
#             runtime_IM_CL+=json_data[i][7]
# print("avgD,c:" ,avgD,c,avgD/c)
# print("avgT,c:" ,avgT,c,avgT/c)
# print(avg_pri1,c,avg_pri1/c)
# print(avg_pri2,c,avg_pri2/c)
# print("avgD_CL,c_CL:" ,avgD_CL,c_CL,avgD_CL/c_CL)
# print("avgT_CL,c_CL:" ,avgT_CL,c_CL,avgT_CL/c_CL)
# print(avg_pri1_A,c_CL,avg_pri1_A/c_CL)
# print(avg_pri2_A,c_CL,avg_pri2_A/c_CL)
# print("avg_runtime:",runtime_IM/c)
# print("avg_runtime_CL:", runtime_IM_CL/c_CL)
def write_MainAverage(rate):
    file = open("Average.json", "r")
    file1=open("MainAverage.json","a")
    json.dump(rate,file1)
    file1.write('\n')
    for line in file:
        json_line = json.loads(line)
        json.dump(json_line,file1)
        file1.write('\n')
    file1.write(100*'*********')
    file1.write('\n')
    file1.close()
    file.close()

# ********************************************************************************
def Calculat_AVG(rate, num_case_experiment):
    json_data=[]
    # avg is a list that contain nine item for averages of eight experiment and one item for check.
    avg=[[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
    write_MainAverage(rate)
    file = open("Average.json", "r")
    for line in file:
        json_line = json.loads(line)
        for i in json_line:
            json_data.append(json_line[i])
    file.close()
    # print(json_data)
#     for i in range(0,len(json_data),num_case_experiment):
#         for j in range(num_case_experiment):
#             for k in range(11):
#                 avg[j][k]=avg[j][k]+json_data[i+j][k]
    len_num_case = len(num_case_experiment)
    for i in range(0,len(json_data),len_num_case):
        for j in range(len_num_case):
            for k in range(11):
                avg[num_case_experiment[j]][k]=avg[num_case_experiment[j]][k]+json_data[i+j][k]
    # print(avg)
#     for i in json_data:
#         print(i)
#     print("*"*150)
#     for i in avg:
#         print(i)
#     print("*"*150)
    for i in avg:
        for j in range(len(i)):
            i[j]=i[j]/(len(json_data)/len_num_case)
#     print(avg)
    return(avg)
