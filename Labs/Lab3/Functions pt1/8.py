def spy_game(nums):
    for i in range(2, len(nums)):
        if nums[i] == 7  and nums[i-1] == nums[i-2] == 0 :
            return True
    return False

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 
