import copy

def pp() :
    # zero is the lowest priority
    p_info = []
    process_order = []

    # getting input from the user: processid, arrival time, burst time and priority
    
    print('NOTE: 0 IS TAKEN AS THE LOWEST PRIORITY.')
    n = int(input('ENTER THE NUMBER OF PROCESSES: '))
    print('ENTER THE PROCESS ID, ARRIVAL TIME, BURST TIME AND PRIORITY RESPECTIVELY: ')
    for _ in range(n) :
       temp_list = list(map(int, input().split()))
       temp_list.append(0)
       p_info.append(temp_list)

    original_p_info = copy.deepcopy(p_info)

    # p_info contains all the information of a process
    # each list(process) of p_info has [processid, arrival time, burst time, priority completion time]


    # sorting on the basis of arrival time
    
    p_info.sort(key = lambda k : k[1])
    original_p_info.sort(key = lambda p: p[1])

    # current time in the gantt chart

    cur_time = 0     
    
    # total time required for completion of all the jobs

    tot_time_req = 0
    for i in range(n) :
        tot_time_req += p_info[i][2]

    counter = 0
    j = 0 

    while(counter < tot_time_req) :
        max_pt = -1
        p_no = None
        for j in range(n) :
            if p_info[j][2] != 0 :
                if p_info[j][1] <= cur_time :
                    if p_info[j][3] > max_pt :
                        max_pt = p_info[j][3]
                        p_no = p_info[j][0] 
        if p_no is None :
            process_order.append(-1)
            cur_time += 1
        else:
            process_order.append(p_no)
            cur_time += 1
            counter += 1
            for k in range(n) :
                if p_no == p_info[k][0] :
                    p_info[k][2] -= 1
                    p_info[k][4] = cur_time
    
    # preparing gantt chart

    gantt_chart = []
    i = 0
    ct = 0
    while i < len(process_order):
        x = 1
        for j in range(i + 1, len(process_order)):
            if process_order[i] == process_order[j]:
                x += 1
                if j == len(process_order) - 1:
                    ct += x
                    break
            else:
                ct += x
                break
        gantt_chart.append([process_order[i], ct])
        i += x

    # printing gantt chart 

    print('\nGANTT CHART: ')
    for p in range(len(gantt_chart)):
        if gantt_chart[p][0] == -1:
            print('IDLE\t|', end='')
        else:
            print('P{}\t|'.format(gantt_chart[p][0]), end='')
    print()
    print('0', '\t', end='')
    for p in range(len(gantt_chart)):
        print(gantt_chart[p][1], '\t', end='')

    # sorting on the basis of process time

    p_info.sort(key=lambda k: k[0])
    original_p_info.sort(key=lambda p: p[0])

    print("\n\nTABLE:\n")

    print('PROCESS NO.\tARRIVAL TIME\tBURST TIME\tPRIORITY\tCOMPLETION TIME\t\tTURN AROUND TIME\tWAITING TIME\t')
    for i in range(n) :
        print(original_p_info[i][0], '\t\t', original_p_info[i][1], '\t\t', original_p_info[i][2],
              '\t\t', p_info[i][3], '\t\t', p_info[i][4], '\t\t\t', p_info[i][4] - p_info[i][1], '\t\t\t\t', p_info[i][4] - p_info[i][1] - original_p_info[i][2])

    tot_tat = 0               
    tot_wt = 0
   
    for i in range(n) :
        tot_tat += p_info[i][4] - p_info[i][1]
        tot_wt += p_info[i][4] - p_info[i][1] - original_p_info[i][2]

    avg_tat = tot_tat / n
    avg_wt = tot_wt / n 
    
    print('\nAVERAGE TURN AROUND TIME: ', avg_tat)
    print('AVERAGE WAITING TIME: ', avg_wt)

pp()
