import random
import copy
from conflicts import calculation_conflicts
from conflict1 import conflict_kol, com_conflict, Intersection
import math
from numpy.core.shape_base import _size

class _Node:
    def __init__(self,Id,line,TimeEnter,vlocity,positon,y,TOA,score,visit,UCB,node):
        self.Id=Id
        self.Line=line
        self.TimeEnter=TimeEnter
        self.vlocity=vlocity
        self.positon=positon
        self.y=y
        self.TOA=TOA
        self.score=-1 #maybe UCB
        self.visit=visit
        self.UCB=UCB
        self.children=[]
        self.parent = node
        self.all_parents=[]
        self.temp_data = []
    def num_child(self):
        return len(self.children)  
    
    def rtn_children(self):
        return self.children  
      
    def get_id(self):
        return self.Id
    
    def get_parent(self):
        return self.parent
    
    def add_to_children(self,node):
        self.children.append(node)
        
    def set_all_parents(self,obj):
        self.all_parents.append(obj)
        
    def get_all_parents(self):
        return self.all_parents
    
    def set_parent(self,node):
        self.parent = node
        
    def set_visit(self,num):
        self.visit = num
        
    def get_visit(self):
        return self.visit
    
    def set_score(self, num):
        self.score = num
        
    def get_score(self):
        return self.score
    
    def set_UCB(self,num):
        self.UCB = num
        
    def get_UCB(self):
        return self.UCB
    
    def get_all(self):
        x = []
        x.append(self.Id)
        x.append(self.Line)
        x.append(self.TimeEnter)
        x.append(self.vlocity)
        x.append(self.positon)
        x.append(self.y)
        x.append(self.TOA)
        x.append(self.score)
        x.append(self.visit)
        x.append(self.UCB)
        return x
    
    def set_temp_data(self,obj):
        self.temp_data.append(obj)
        
    def get_temp_data(self):
        return self.temp_data
        
class mcts:
    def __init__(self,all_data, om0,t,lastTime):
        self.root = _Node(None,None,None,None,None,None,None,0,0,0,None)
        self.temp_data = []
        self.all_data = all_data
        self._size = len(self.all_data)
        self.om0 = om0
        self.t = t
        self.last_time=lastTime
        self.best_priority = self.all_data
        self.best_delay = 10000
        self.preprocces()
        
    def preprocces(self):
        for i in self.all_data:
            i.append(0)
            i.append(0)
            i.append(0)
        temp = []
        for i in range(self._size):
            self.temp_data.append(copy.deepcopy(self.all_data[i]))
        for i in self.all_data:
            temp.append(self.create_node(i))
        self.all_data = copy.deepcopy(temp)
        
    def negative_test(self,child_list):
        for i in child_list:
            if i.get_score() == -1:
                return True, i
        return False, None
    
    def create_node(self,t_list):
        Id,line,TimeEnter,vlocity,positon,y,TOA,score,visit,UCB = t_list
        new_node = _Node(Id,line,TimeEnter,vlocity,positon,y,TOA,score,visit,UCB,None)
        return new_node
    
    def selection(self,node):
        #print("main node: ", node.get_id(), "score: ",node.get_score())
        forbiden_nodes = self.not_possible_nodes(node)
        #print("Forbiden Nodes: ",forbiden_nodes)
        child_list = []
        for i in self.all_data:
            if i.get_id() not in forbiden_nodes:
                child_list.append(i)
                #print("childList: ",i.get_id())
        flag, ex_node = self.negative_test(child_list)
        if  flag == True:
            return self.expand(node, ex_node)
        else: #ucb selection 
            child_list = node.rtn_children()
            if len(child_list)==0:
                return(self.simulation(node))
            temp_child_list=[]
            for i in child_list:
                temp_child_list.append(i.get_UCB())
#                 print(min(temp_child_list))
            if len(temp_child_list)==0:
                print("empty")
            index_next_node=temp_child_list.index(min(temp_child_list))
#             print(temp_child_list,index_next_node)
#             index_next_node = child_list.index(random.choice(child_list))
            return self.selection(child_list[index_next_node])
        
    def not_possible_nodes(self,node):
        lst = []
        #temp_list = []
        #for i in range(len(node.all_parents)):
        #    temp_list.append(node.all_parents[i])
        f_list = []
        for i in range(len(node.all_parents)):
            f_list.append(node.all_parents[i].get_id())
        temp1 = node.rtn_children()
        for i in range(len(temp1)):
            f_list.append(node.children[i].get_id())
        for i in range(len(self.all_data)):
            if self.all_data[i].get_id() in f_list:
                lst.append(self.all_data[i].get_id())
        if node.get_id() != None:
            lst.append(node.get_id())
        return lst
    
    def expand(self,node, ex_node):
        for i in range(len(self.temp_data)):
            #print(self.all_data[i].get_id(),ex_node.get_id())
            if self.temp_data[i][0] == ex_node.get_id():
                new_node = self.create_node(self.temp_data[i])
                x = node.get_all_parents()
                for k in x:
                    new_node.set_all_parents(k)
                new_node.set_all_parents(node)
                node.add_to_children(new_node)
                new_node.set_parent(node)
                break
        return self.simulation(new_node)
    
    def simulation(self,node):
        t_node = copy.deepcopy(node)
        x = t_node.get_all_parents()
        #for i in x:
        #    print("i score: ", i.get_score())
        priority_asign = []
        for k in x:
            if k.get_id() != None:
                priority_asign.append(k)
        priority_asign.append(t_node)
        child_list = []
        f_list = []
        for i in self.all_data:
            f_list.append(i.get_id())
        p_list = []
        for i in priority_asign:
            p_list.append(i.get_id())
        for i in range(len(f_list)):
            if f_list[i] not in p_list:
                child_list.append(self.all_data[i])
        while len(child_list)!=0:
            temp=random.choice(child_list)
            priority_asign.append(temp)
            child_list.pop(child_list.index(temp))
        delay_for_this_priority = self.calcuat_delay(priority_asign)
        temp_pro = []
        for i in priority_asign:
            temp_pro.append(i.get_all())
        #print("pro: ",temp_pro)
#         print("best delay: ",self.best_delay,delay_for_this_priority)
        if self.compare(delay_for_this_priority) == True:
#             print("Ali Asghar")
            self.best_priority = temp_pro
            self.best_delay = delay_for_this_priority
        return self.backprobagat(delay_for_this_priority,node)

    def calculate_UCB(self,node):
        if node.get_id() != None:
            c1 = (node.get_score() / node.get_visit())
            c = 2
            c2 = math.sqrt(math.log(node.parent.get_visit())/node.get_visit())
            ucb = c1 + (c*c2)
            node.set_UCB(ucb)
        child_list = node.rtn_children()
        for i in child_list:
            self.calculate_UCB(i)
        return
    def backprobagat(self, _delay,node):
        if node.get_id() == None:
            node.set_visit(node.get_visit()+1)
            return self.calculate_UCB(node)
        node.set_visit(node.get_visit()+1)
        node.set_score(node.get_score()+_delay)
        #self.update_temp(node)
        return self.backprobagat(_delay, node.parent)
     
    def compare(self, delay1):
        if delay1 <= self.best_delay:
            return True
        return False
        
    def calcuat_delay(self,choice):
        _tm = []
        for i in choice:
            _tm.append(i.get_all())
        choice = copy.deepcopy(_tm)
#         print("choise",choice)
        om0 = copy.deepcopy(self.om0)
        t = copy.deepcopy(self.t)
        last_time=copy.deepcopy(self.last_time)
        w1,delay,w2,drop,w3,w4,w5,w6=Intersection(choice,om0,t,0,0,0,[],[],0,last_time,0)
#         print(delay)
#         _tm = []
#         for i in choice:
#             _tm.append(i.get_all())
#         choice = copy.deepcopy(_tm)
# #         print("choise",choice)
#         om0 = copy.deepcopy(self.om0)
#         t = copy.deepcopy(self.t)
#         #print("Omega0: ", om0)
#         #print("Time: ",t)
# #         l_choice=len(choice)
#         delay_kol=[]
#         while choice!=[]:
#             item=choice[0]
#             Vmax=22.3
#             toa_max=(100/Vmax)+t
#             toa_new=0
#             temp1=com_conflict(item,conflict_kol())
#             for k in range(len(om0)):
#                 for m in range(len (temp1)):
#                     if t < om0[k][6]:
#                         if om0[k][1]==temp1[m][0]:
#                             toa=om0[k][6]+(((temp1[m][2])/(Vmax))-((temp1[m][1])/(Vmax)))
#         #                     print("TOA_Car  "+om0[k][0]+":",om0[k][6])
#         #                     print("TimeConflict  "+om1[0]+"+TOA_Car  "+om0[k][0]+":",toa)
#                             if toa > toa_new:
#                                 toa_new=toa
#         #                             conf.append(temp[m])
#                             break
#             if toa_max > toa_new:
#                 toa_new=toa_max 
#             delay_kol.append(toa_new-toa_max)
# #             print(delay_kol)
#             om0.append(item)
#             choice.pop(0)
# #             print("choise:",choice)
# #             print("om0:",om0)
#         sum_delay=0
# #         print((delay_kol))
#         for i in delay_kol:
#             sum_delay+=i
#         sum_d=sum_delay/len(delay_kol)

            #print(item,choice)
        sum_delay=0
#         print((delay_kol))
        for i in delay:
            sum_delay+=i
        sum_d=sum_delay/len(delay)
#         print(sum_d)
        return (sum_d)
    def postprocessing(self):
        _tm = []
        for i in self.best_priority:
#             print(i)
            del i[7:]
            _tm.append(i)
#             print(_tm)
        return _tm
        
    def run(self, it_num):
        self.best_delay= self.calcuat_delay(self.all_data)
        comper_temp=copy.deepcopy(self.best_delay)
#         print(self.best_delay)
        for _ in range(it_num):
            self.selection(self.root)
#             for i in range(len(self.root.rtn_children())):
#                 print("child score: ",self.root.children[i].get_score())
#             _tm = []
#             for i in self.best_priority:
#                 _tm.append(i.get_all())
#             print("Best Priority:  ",_tm)
#             x = self.root.rtn_children()
#             for i in x:
#                 print(i.get_UCB())
#             input()
#             print("Best priority: ", self.best_priority)
        self.best_priority=self.postprocessing()
        print("Best priority: ", self.best_priority)
#         input()
        if comper_temp!=self.best_delay:
            print(comper_temp, self.best_delay)
        return self.best_priority
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    