# Given an array of integers, return indices of the two numbers
#  such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def pair_sum_indices(lst: list, nums_sum):
    if not lst:
        return False
    seen = dict()
    for i in range(len(lst)):
        pair = nums_sum - lst[i]
        if pair in seen:
            return [seen[pair], i]
        else:
            seen.update({lst[i]: i})
            print(seen)
    return


# Merge two sorted arrays
# Input: [0,3,4,30] [4,6,31]
# Output: [0,3,4,4,6,30,31]

def merge_sorted_lists(list_1, list_2):
    if not list_1 or not list_2:
        return list_1 + list_2
    merged_lst = []
    indx_1 = 0
    indx_2 = 0

    while indx_1 < len(list_1) and indx_2 < len(list_2):
        if list_1[indx_1] < list_2[indx_2]:
            merged_lst.append(list_1[indx_1])
            indx_1 += 1
        else:
            merged_lst.append(list_2[indx_2])
            indx_2 += 1
        print(merged_lst)
    return merged_lst + list_1[indx_1:] + list_2[indx_2:]


# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move_zeros(nums):
    i = count = 0
    len_nums = len(nums)
    while count < len_nums:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i += 1
        count += 1
    return nums


# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

def roman_to_int(romans_str: str) -> int:
    roman_val = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    # one-line for loop, collect all roman values from input str
    tmp_list = [roman_val[item.lower()] for item in romans_str]
    total = 0
    input_length = len(tmp_list)
    if input_length == 1:
        return roman_val[romans_str.lower()]
    # compare two indexes to see if 'i + 1' is greater than 'i'
    for i in range(input_length - 1):
        if tmp_list[i + 1] > tmp_list[i]:
            tmp_list[i], tmp_list[i + 1] = 0, (tmp_list[i + 1] - tmp_list[i])
        total += tmp_list[i]
    return total + tmp_list[-1]  # the last el was not added as for loop range was (input_length - 1)


# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_longest_sub_str(self, s: str) -> int:
    if s == " ":
        return 1
    max_count = count = 0
    seen = dict()
    start_indx = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start_indx:
            start_indx = seen[char] + 1
            count = i - seen[char]
            seen[char] = i
        else:
            count += 1
            seen[char] = i
            max_count = max(max_count, count)
    return max(max_count, count)
