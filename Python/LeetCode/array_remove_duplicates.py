class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)   # длина входного массива
        k = 0           # индексация по новому массиву из уникальных элементов
        for i in range(n - 1):         # идем по элементам массива
            if nums[i] != nums[i + 1]: # если следующий не равен текущему -- записываем в новый массив (перезаписываем в старый, потому что экономим место)
                nums[k] = nums[i] 
                k += 1
                                        # если следующий равен предыдущему -- просто пропускаем его

        nums[k] = nums[n - 1]   # в цикле не доходим до последнего элемента -- рассматриваем его отдельно
                                # если он не равен предыдущему -- он записывается в следующее место массива
                                # если он равен предыдущему -- он запишется на то же место, тк k в этом случае не увеличивалось
        del nums[k+1::]         # в первых k элементах массива -- теперь уникальные элементы
                                # поэтому удаляем всё что осталось от исходного массива после k-го элемента
        return k+1

# nums = input()
# expectedNums = input() # The expected answer with correct length

nums = [1, 2, 2, 3, 4, 4, 4, 5, 5]
expectedNums = [1, 2, 3, 4, 5]

s = Solution()
k = s.removeDuplicates(nums) #Calls your implementation

print(k)
print(nums)

k = len(expectedNums)
for i in range(0, k):
    assert nums[i] == expectedNums[i]


