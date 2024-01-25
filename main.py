def number_of_intersections(input_list_values,input_list_points):
    if len(input_list_values) < 4 or  len(input_list_points) < 4: return 0 # Need at least two chords to form an intersection
    
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
    
     count = 0
    
    qlength = 0
    q = deque([])
    
    for val, event_type, idx in events:
        if q and event_type == -1 and q[0][2] == idx:
            print('first',q)
            q.popleft()
            if q: 
                while len(q) > 1 and q[0][-1] == q[-1][-1]:
                    qlength += count - 1 
                    q.popleft()
                else: 
                    qlength += count - 1
                count -= 1
                
        elif q and event_type == -1 and q[0][2] != idx:
            if q[-1][2] == idx:
                q.pop()
                count -= 1
            else:
                q.append((val,event_type,idx))
                count -= 1 
        else:
            q.append((val,event_type,idx))
            count += 1
        
        if count < 0: count = 0
    
    
    return qlength
    
    
print(number_of_intersections([0.78,1.47,1.77,3.92],['e1','s1','e2','s2']))
