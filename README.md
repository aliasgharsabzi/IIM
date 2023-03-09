# Intelligent Intersection Management for Autonomous Vehicles
Based on the journal paper "Intelligent Intersection Management for Autonomous Vehicles" by A. Sabzi, and M. Shirazi, submitted to IEEE Transactions on Intelligent Transportation Systems.
# Quick Start
1. Open python 3 and create a workspace.
2. Download all files in this repository and paste them into the created workspace, because some functions were imported from these files into the "IM.py".
3. Rum the file "IM.py"

# Parameters
When you would run the IM.py file you can set some parameters such as Rate, iteration, and num_case_experiment in this file.
1. Rate = This is a list that can set the flow rate of entrance vehicles into the intersection. 
2. iteration = Number of runs for each rate
3. num_case_experiment = This is a list that it can have values of 1 to 8. Each number corresponds to one case shown below:
    - case 0 = Robust intersection management (RIM); Generating basic information and storing it in a JSON file. For a fair comparison of different cases, 
    we must store basic information because the basic information is generated randomly.
    - case 1 = Robust intersection management (RIM); Reading basic information from created JSON file
    - case 2 = RIM with weighted priority assignment policy
    - case 3 = RIM with changing the lane
    - case 4 = RIM with weighted priority assignment policy and changing the lane
    - case 5 = RIM with priority assignment based on MCTS
    - case 6 = RIM with priority assignment based on MCTS and changing the lane
    - case 7 = RIM with weighted priority assignment and priority assignment based on MCTS
    - case 8 = RIM with weighted priority assignment, priority assignment based on MCTS, and changing the lane
# Outpus
The outputs include:

1. "AVG_kol.json" is a JSON file that saved the average of the result of runs. <br />
for example:
``` {"0.01": [[48.0, 1.8199199341888812, 23.681109865470845, 0.0, 4.768025159835815, 1.3488255975826577, 5.3475309647385245, 0.022955656051635742, 0.0, 9.0, 2.0],...]} ```
this show that for rate "0.01"  in case 0 average results is for the number of vehicles, AVG_delay, time trip, number of change lane,
excutionTime_overall, delay_first_priority, delay_second_priority, excutionTime_IM, and number of request fail respectively.<br />
2. Also, you can active (uncomment) ``` draw(X_kol,Y_kol,numberkol,line_kol,angle) ``` in the end of code in "IM.py" for showing simulator, but  notice that  you should set: <br /> 
    - Rate = Just one arbitrary rate for example: Rate = [0.05]
    - iteration = 1
    - num_case_experiment = An arbitrary case for example: num_case_experiment = [0,3]. 0 is constant and 3 it means 'RIM with changing the lane' must be run.
