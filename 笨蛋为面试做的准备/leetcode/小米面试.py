# coding=utf-8

def Function(nums):
    wavecrest = []
    for i in range(len(nums)):
        if (i == 0 or nums[i] > nums[i-1]) and (i == len(nums)-1 or nums[i] > nums[i+1]):
            wavecrest.append([nums[i],i])

    slope = []
    for i in range(len(wavecrest)-1):
        slope.append((wavecrest[i+1][0]-wavecrest[i][0])/(wavecrest[i+1][1]-wavecrest[i][1]))

