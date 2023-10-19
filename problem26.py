<<<<<<< HEAD
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
#
# 26. 删除有序数组中的重复项
#
# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
#
# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
#
# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
# 返回 k 。
#
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
#
# 示例 2：
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
# [0,0,1,1,1,2,2,3,3]
# [0,0,1,1,1,2,2,3,3]
# [0,1,0,1,1,2,2,3,3]
def remove(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    right1 = 0
    right2 = 1
    while right2 < len(nums):
        if nums[right2] > nums[right1]:
            nums[right1 + 1] = nums[right2]
            right1 += 1
        else:
            right2 += 1
    print(nums, right1 + 1)


def remove2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    index = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            nums[index] = nums[i]
            index += 1
    print(nums, index)


remove([1, 1, 2])
remove([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

remove2([1, 1, 2])
remove2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
=======
# https://leetcode.cn/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# // nums
# 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int
# len = removeElement(nums, val);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中
# 该长度范围内
# 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }
#
# 示例1：
#
# 输入：nums = [3, 2, 2, 3], val = 3
# 输出：2, nums = [2, 2]
# 解释：函数应该返回新的长度2, 并且nums中的前两个元素均为2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为2 ，而
# nums = [2, 2, 3, 3]
# 或
# nums = [2, 2, 0, 0]，也会被视作正确答案。
# 示例2：
# 输入：nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# 输出：5, nums = [0, 1, 4, 0, 3]
# 解释：函数应该返回新的长度
# 5, 并且
# nums
# 中的前五个元素为
# 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

# 解题思路:双指针
def remove(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    start, end = 0, len(nums)
    while start < end:
        if nums[start] == val:
            nums[start] = nums[end - 1]
            end -= 1
        else:
            start += 1
    print("数组内容: {}，数组长度: {}".format(nums, start))
    return start


remove([3, 2, 2, 3], 3)
remove([0, 1, 2, 2, 3, 0, 4, 2], 2)
remove([2], 3)
remove([], 0)
>>>>>>> b631ae7eed673141846664d674eedb53d3d79d72
