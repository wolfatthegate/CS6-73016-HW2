# HW 2. Question 4
# @author - Waylon Luo
# Big Data Analytics CS 6-73016 

d = 2
E1 = [[2, 6], [3, 5]]
E2 = [[1, 4], [2, 4]]     # 1, 2, 4, 6 

def check_overlapped_recursive(xmin, xmax, ymin, ymax, i): 

	# compare the set, sort by smaller min
	if (xmin < ymin): 
		small_min = (xmin, xmax)
		large_min = (ymin, ymax)
	else: 
		small_min = (ymin, ymax)
		large_min = (xmin, xmax)
	
	if (small_min[1] > large_min[0] ): # i-th dimension overlapped 		
		# check next (i+1)th dimension
		if i == d-1: 
		    return True
		return check_overlapped_recursive(E1[i+1][0], E1[i+1][1], E2[i+1][0], E2[i+1][1], i+1)
	else: 
		# there is no overlapped
		return False


# Test the function
i = 0
overlap = check_overlapped_recursive(E1[i][0], E1[i][1], E2[i][0], E2[i][1], i)

if (overlap): 
	print('E1 and E2 is overlapped')
else: 
	print('E1 and E2 is not overlapped')
