import json
import numpy as np
import matplotlib.pyplot as plt

# NUM, AVG_delay, timeTrip, num_CL, excutionTime_kol, delay_first_priority, delay_second_priority, excutionTime_IM, fail
def plot_result():
    def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    
        # Check if colors where provided, otherwhise use the default color cycle
        if colors is None:
            colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    
        # Number of bars per group
        n_bars = len(data)
    
        # The width of a single bar
        bar_width = total_width / n_bars
    
        # List containing handles for the drawn bars, used for the legend
        bars = []
        patterns =('-', '.', 'x', '+','//','O','\\','*','\\\\')
#         hatches = [p for p in patterns for i in range(n_bars)]
        # Iterate over all data
        for i, (name, values) in enumerate(data.items()):
            
            # The offset in x direction of that bar
            x_offset = (i - n_bars / 2) * bar_width + bar_width / 2
    
            # Draw a bar for every value of that type
            x = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
            for x, y in enumerate(values):
    #             x= x /100
                bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)], hatch=patterns[i])
               
            bars.append(bar[0])
        # Draw legend if we need
        if legend:
            ax.legend(bars, data.keys(),loc= 'upper left', facecolor="khaki", handleheight= 1.5, handlelength= 3, prop={"size":9.5})
        handles, labels = bars, data.keys()
        return(handles, labels)   
    
    
    json_data=[]
    file = open("AVG_kol.json", "r")
    
    for line in file:
        json_line = json.loads(line)
        for i in json_line:
            json_data.append(json_line[i])
    file.close()   
    # print(df)
    # print(asd)
    prim= []
    for i in json_data:
        for j in i:
            prim.append(j)
    
    # print(prim)
    
    def extract_data(num_col):
        ex = []
        c = 1
        d = 0
        temp = []
        for i in prim:
            if d % 9 != 0: 
                temp.append(i[num_col])
            if c % 9 == 0:
                ex.append(temp)
                temp = []
            d+=1
            c+= 1
        
    #     print(ex)
        ex = np.array(ex)
        ex= ex.T
        ex = ex.tolist()
        loop = ['Robust intersection management (RIM)','RIM with weighted priority assignment policy',
                        'RIM with changing the lane','RIM with weighted priority assignment policy and changing the lane',
                        'RIM with priority assignment based on MCTS',
                        'RIM with priority assignment based on MCTS and changing the lane',
                        'RIM with weighted priority assignment and priority assignment based on MCTS',
                        'RIM with weighted priority assignment, priority assignment based on MCTS, and changing the lane']
        # loop = ['0.01','0.02','0.03','0.04','0.05','0.06','0.07','0.08','0.09','0.1']
        dic = {}
    #     print(ex)
        for i in range(8):
            dic[loop[i]] = ex[i]
    #     print(dic)
        return(dic)
    # drawing chart according number of column
    num_col = 1
    data = extract_data(num_col)
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(14,6))
    # fig = plt.figure(figsize=(10, 8))
    # ax=plt.subplot()
    
    ax1.set_xlabel("Flow rate")
    # labels = ['0.01','0.02','0.03','0.04','0.05','0.06','0.07','0.08','0.09','0.1']
    ax1.set_xticks((0,1,2,3,4,5,6,7,8,9))
    ax1.set_xticklabels(('0.01','0.02','0.03','0.04','0.05','0.06','0.07','0.08','0.09','0.1'))
    ax1.set_title('Delay comparison')
    ax1.set_ylabel('Average delay (Second)')
    handles, labels = bar_plot(ax1, data, total_width=.8, single_width=.9,legend = False)
    
    num_col = 7
    data = extract_data(num_col)
    ax2.set_xlabel("Flow rate")
    ax2.set_xticks((0,1,2,3,4,5,6,7,8,9))
    ax2.set_xticklabels(('0.01','0.02','0.03','0.04','0.05','0.06','0.07','0.08','0.09','0.1'))
    ax2.set_title('Execution time comparison')
    ax2.set_ylabel('Time (second)')
    handles, labels= bar_plot(ax2, data, total_width=.8, single_width=.9,legend = False)
    fig.legend(handles, labels, loc='upper left')
    plt.show()


