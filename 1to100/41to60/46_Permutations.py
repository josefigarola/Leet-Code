class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr = []):
            if(len(curr) == len(nums)):
                out.append(curr[:])
                print('out',out)
                return

            for num in nums:
                if(num not in curr):
                    curr.append(num)
                    #print(curr)
                    backtrack(curr)
                    curr.pop()
                    #print(curr)

        out = []
        backtrack()
        return out