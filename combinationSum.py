class Solution:
    def findCombination(self, arr, ind, target, ans, ds):
        if ind == len(arr):
            if target == 0:
                ans.append(ds.copy())
            return
        if arr[ind] <= target:
            ds.append(arr[ind])
            self.findCombination(arr, ind, target - arr[ind], ans, ds)
            ds.pop()
        self.findCombination( arr, ind+1, target, ans, ds)
    def combinationSum(self, candidates, target):
        ans =[]
        self.findCombination(candidates,0, target, ans, [])
        return ans
obj = Solution()
candidates = [2,3,4,7]
target =7
res = obj.combinationSum(candidates, target)
print(res)