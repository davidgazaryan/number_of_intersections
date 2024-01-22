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
