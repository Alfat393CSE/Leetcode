class Solution(object):
    def maximumLength(self, nums):
        maxcnt=0
        cnt=0
        even=False
        for i in range(len(nums)):
            if nums[i]%2==0:
                if not even:
                    cnt+=1
                    even=True
            else:
                if even:
                    cnt+=1
                    even=False
        maxcnt=max(maxcnt,cnt)

        even= True
        cnt=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                if not even:
                    cnt+=1
                    even=True
            else:
                if even:
                    cnt+=1
                    even=False
        maxcnt=max(maxcnt,cnt)
        cnteven=cntodd=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                cnteven+=1
            else:
                cntodd+=1
        maxcnt=max(maxcnt,cnteven,cntodd)

        return maxcnt

# Test cases
print(Solution().maximumLength([1,2,3,4]))       # 4
print(Solution().maximumLength([1,2,1,1,2,1,2])) # 6
print(Solution().maximumLength([1,3]))           # 2
