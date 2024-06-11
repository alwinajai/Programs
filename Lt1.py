#Arrange a list of non-negative numbers to form the largest number and return it
def largest_number(nums):
    nums_str=[str(num) for num in nums]
    def compare(a, b):
        return (a + b) > (b + a)
    for i in range(len(nums_str)):
        for j in range(len(nums_str) - 1 - i):
            if not compare(nums_str[j], nums_str[j + 1]):
                nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
    largest_num = ''.join(nums_str)
    if largest_num[0] == '0':
        return '0'
    return largest_num
numbers = [3, 30, 34, 5, 91]
print(largest_number(numbers)) 
