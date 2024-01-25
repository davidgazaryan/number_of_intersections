def count_intersections(inputList: list):
    intersections = 0
  
    if not inputList: return 0 
    
    start_points = inputList[:len(inputList)//2] #O(k) elements
    end_points = inputList[len(inputList)//2:]
    #Given each point should have start and end we can split the list in half 
    combined_list = list(zip(start_points,end_points))
    print(combined_list)
    
    for i in range(len(combined_list)):
        print(i) 
      #If angle(end1 > angle start 2) add 1 
    
    
count_intersections([0.78,1.47,1.77,3.92])


x = [1.78,1.47,1.77,3.92]
y = ['e1','s1','e2','s2']
def number_of_intersections(input_list_values,input_list_points):
    if not input_list_values or not input_list_points: return 0
    
    combined_list = list(zip(input_list_values,input_list_points))
    print(combined_list)
    
    points_to_values = {}
    for value, point in combined_list:
        if point.startswith('s'):
            points_to_values[point] = value
        elif point.startswith('e'):
            points_to_values[point] = value


    pairs = [[points_to_values[f's{i}'], points_to_values[f'e{i}']] for i in range(1, len(combined_list) // 2 + 1)]

    sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
    print(sorted_pairs)
        
    events = []

    # Create events for start and end points
    for i, (start, end) in enumerate([[0.78, 1.77], [1.47, 3.92],[1.55,4.5],[2.5,5],[3.1,1.3],[1.6,3.3]]):
        if start > end:
            start,end = end,start

        events.append((start, 1, i))  # 1 represents the start of an interval
        events.append((end, -1, i))  # -1 represents the end of an interval
    
    # Sort events based on points and event types
    events.sort()
    print(events)# Try set with variable seen 
    
    seen = set()
    qlength = 0
    q = deque([])
    #Seen and unseen two sets find diff between 
    
    for val, event_type, idx in events:
        if event_type == -1 and q[0][2] == idx:
            q.append((val,event_type,idx))
            while q and q[0][2] == q[-1][2]:
                q.popleft()
                if q: 
                    print(q)
                    qlength += len(q) - len(seen)
                    seen = set(list(q))
                
        elif event_type == -1 and q[0][2] != idx:
            q.append((val,event_type,idx))
        else:
            q.append((val,event_type,idx))
        
        print(val,qlength)
        
        
    return qlength
    
    
print(number_of_intersections([0.78,1.47,1.77,3.92],['e1','s1','e2','s2']))
