import json

def writefile(temp,t):
    f=open("sample1.json", "a")
    json.dump({t:temp}, f) 
    f.write("\n")
    f.close()
# def readfile(om1):

def readfile_Runs(loop):
    a=[]
    data=[]
    with open('Runs.json', 'r') as f: 
        for line in f:
            file_line=json.loads(line)
            for i in file_line:
                if i==str(loop):
                    c=file_line[i]
                    for j in range(len(c)):
                        for k in c[j]:
                            a.append(c[j][k])
                    break   
    for i in a:
        data.append(i)
    f.close()
    return(data)
def main_readfile(om1,counterTime,data):
    for i in data[counterTime]:
        om1.append(i)
    return(om1)


def write_for_check(om1,om0,t):
    item_om1=[]
    item_om0=[]
    f=open("sample.json", "a")
    if om1!=[]:
        for i in range(len(om1)):
            c=(om1[i][4],om1[i][5])
            item_om1.append(c)
#             json.dump({t:om1[i][4]}, f) 
    if om0!=[]:
        for i in range(len(om0)):
            c=(om0[i][4],om0[i][5])
            item_om0.append(c)
#             json.dump({t:om0[i][4]}, f)
    
    if om1!=[]or om0!=[]:
        json.dump({t:item_om1+item_om0}, f)
        f.write("\n")
    f.close()
    
def Runs(loop):
    json_data=[]
    file = open("sample1.json", "r")
    for line in file:
        json_line = json.loads(line)
        json_data.append(json_line)
    f=open("sample1.json", "w")
    f.close()
    file = open("Runs.json", "a")
    json.dump({loop:json_data}, file) 
    file.write("\n")
    file.close()  
       
def Average(loop,counter,AVG,av,Num_change,runtime,sum1,sum2,sum_runtime_IM,fail,len_pri1,len_pri2):
    file = open("Average.json", "a")
    json.dump({loop:[counter,AVG,av,Num_change,runtime,sum1,sum2,sum_runtime_IM,fail,len_pri1,len_pri2]}, file) 
    file.write("\n")
    file.close()
def write_AVG_kol(AVG_kol,rate):
    f=open("AVG_kol.json", "a")
    json.dump({rate:AVG_kol}, f) 
    f.write("\n")
    f.close()
    f=open("Average.json", "w")
    f.close()
    f=open("Runs.json", "w")
    f.close()
        
def clear_file():
    f=open("Average.json", "w")
    f.close()
    f=open("Runs.json", "w")
    f.close()
    f=open("MainAverage.json", "w")
    f.close()
    f=open("AVG_kol.json", "w")
    f.close()