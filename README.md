# Algorithm for finding number of intersections between n chords in a unit circle who have starting and ending points from [0,2pi] radians

How To Run: Use the Two lists as inputs in the main function "number_of_intersections."

The algorithm starts off by taking two input lists as instructed. We first check if the size of the input lists are a minimum of 4 since we need at least 2 pairs to form an intersection.
We can then use the python zip function to combine the two lists as we need the labels, not just points, since labels aren't sorted. We then use a hash map or python dict to map each label 
to the value it posseses. This way we can use list comprehension to combine start and end points and make it into a list of pairs. Once we have our pair list, the main algorithm begins.

For this algorithm I went with a line sweep approach. This means that for each iteration of the loop we add 1 for when a point starts and subtract 1 for when it ends and add it to our events list
along with the index of the point, which is important given starting and ending points should have the same index. This allows us to keep track
of which points are currently "open" and which are "closed" which is important for determing the number of intersections. Also I made sure to swap start,end if start is greater than end because if we don't do that
it will mess up which order our points get added to the queue. We make sure to sort the events list so that it's in perfect order and our line is sweeping across the circle from [0,2pi] radians.

Next, we use two variables qlength = 0, count = 0 and a queue data structure to add our points from the events list. The queue runs so that each time we encounter a start point we take into account how many points come after that start point in the queue before said
point closes. This is done for every element in the events list. This is because if a different point has a higher starting point than the one we are looking at, it should intersect with our point given the end is greater than the
end point of the point we are looking at. If it's not greater, the queue deals with that as well, which is the elif part of the loop. If we open at lets say 0.8 and close right away at 0.9 we remove right away from the queue the 0.8 and subtract 1 from our count
because we always subtract when a point is closed. Count is incremented by 1 each time we have an event type that is 1(opening a point) and decremented by 1 when we pop because that signals a point has closed. We add count to our qlength variable if we 
do a popleft and make sure to subtract 1 from count as well because the next opening point we start with is no longer part of our interval aka it's not between [open,closed] since its the current point we are inspecting. 

TIME COMPLEXITY ANALYSIS:
  Overall, this algorithm has a time complexity of o(n logn). The costliest part of the algorithm is when we sort the events list as that is done in o(n logn) in python. The looping and adding elements to the queue is o(n) since accessing elements
  at the start and end of a queue is done in o(1) in python. Thus, we have a o(nlogn) + o(n) which simplifies to o(nlogn) for the time complexity of the algorithm.

