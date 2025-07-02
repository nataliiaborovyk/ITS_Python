'''
Given an array of integers nums and an integer target, return indices of the two numbers
 such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''
#Example 1:
nums_1= [2,7,11,15]
target_1= 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:
nums_2= [3,2,4]
target = 6
#Output: [1,2]

#Example 3:
nums_3 = [3,3]
target = 6
#Output: [0,1]


def sums(array:list, target:int):
    for i in range(len(array)):
        for k in range(i+1,len(array)):
            if target == array[i] + array[k]:
                return i, k


print(*sums(nums_1,target_1))
print(*sums(nums_2,target))
print(*sums(nums_3,target))