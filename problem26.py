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
