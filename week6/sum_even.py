def even_sum(nums):
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    total = 0
    for even in even_numbers:
        total = total + even
    return total
sum_even = even_sum([1,2,3,4,5, 6])



count = 0
while (count < 10):
    print(count)
    count = count +1 