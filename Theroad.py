#!
# There is a road consisting of N segments (numbered from 0 to N-1) described by an array R 
# of integers. The K-th segment is described by an integer R[K]. If the segment is smooth 
# (there is no pothole in it), then R[K] = 0; otherwise it contains a pothole of depth R[K].
#  Consecutive potholes join together and create a larger group of potholes.
# The pothole indicator is the number of consecutive single potholes that have joined into
# a pothole group, multiplied by the depth of the deepest pothole among them. For example, 
# the indicator for a group of three consecutive joined potholes of sizes [1, 4, 1] is 3*4=12.
#  What is the largest pothole indicator on the entire road?
# Write a function:
# int solution (int R[], int N);
# that, given an array R of N integers, returns the largest pothole indicator on the road.
# Examples:
# 1. Given R = [0, 2, 1, 1, 0, 4, 1], the function should return 8. The potholes in the fragment 
# [2, 1, 1] join into one pothole group. It is made of three segments and the deepest pothole 
# among them is of depth 2, so its pothole indicator is equal to 3*2=6. The potholes in the fragment 
# [4, 1] join into another pothole group. It is made of two consecutive potholes and the deepest pothole 
# among them is of depth 4, so its pothole indicator is equal to 2*4=8.
# 2. Given R = [1, 4, 1, 0, 5, 2, 3, 0, 8], the function should return 15. The consecutive potholes that
#  join into three larger pothole groups are as follows:
# ⚫ [1, 4, 1] with indicator 3 * 4 = 12;
# ⚫ [5, 2, 3] with indicator 3 * 5 = 15; ⚫ [8] with indicator 1 * 8 = 8.
# The largest pothole indicator is 15.

# solution 
# initialize variable

# def solution(R):
#     max_indicator = 0
#     consecutive_potholes = 0
#     max_pothole_depth = 0

#     for depth in R:
#         if depth > 0:
#             consecutive_potholes += 1
#             max_pothole_depth = max(max_pothole_depth, depth)
#         else:
#             max_indicator = max(max_indicator, consecutive_potholes * max_pothole_depth)
#             consecutive_potholes = 0
#             max_pothole_depth = 0

#         max_indicator = max(max_indicator, consecutive_potholes * max_pothole_depth)

#     return max_indicator

def smooth_path(input_list):
    groups = []
    current_group = []
    for num in input_list:
        if num == 0:
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            current_group.append(num)
    if current_group:
        groups.append(current_group)
    max_sum = 0
    for group in groups:
        group_sum = len(group) * max(group)
        if group_sum > max_sum:
            max_sum = group_sum
    return max_sum

print(smooth_path([0,2,1,1,0,4,1]))

def solution(A):
    from collections import Counter
    counter = Counter(A)
    freqs = sorted(list(counter.values()), reverse=True)
    deletions = 0
    seen = set()
    for freq in freqs:
        while freq in seen:
            freq -= 1
            deletions += 1
        if freq > 0:
            seen.add(freq)
    return deletions

def solution(S):
    from collections import defaultdict
    left_counter = defaultdict(int)
    right_counter = defaultdict(int)
    for c in S:
        right_counter[c] += 1
    splits = 0
    for i in range(len(S) - 1):
        c = S[i]
        left_counter[c] += 1
        right_counter[c] -= 1
        if left_counter['x'] == left_counter['y'] or right_counter['x'] == right_counter['y']:
            splits += 1
    return splits