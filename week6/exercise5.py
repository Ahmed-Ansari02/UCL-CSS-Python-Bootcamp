#[1,3,-4,-5,7,10,0,-56]

def remove_negatives(nums_list):
    resultList = []
    
    for num in nums_list:
        if num >= 0:
            resultList.append(num)
        
    return resultList

input = [1,3,-4,-5,7,10,0,-56]
print(remove_negatives(input))
        