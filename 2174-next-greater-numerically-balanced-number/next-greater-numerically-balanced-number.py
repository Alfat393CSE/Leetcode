class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import itertools

        # Maximum length needed:
        # n <= 10^6 (6 digits) but next balanced number might be 7 digits (e.g. 1224444),
        # so generate up to length 7.
        MAX_LEN = 7

        nums = set()
        # iterate over all subsets of digits 1..9
        for mask in range(1, 1 << 9):
            mult = []
            total_len = 0
            for i in range(9):
                if (mask >> i) & 1:
                    d = i + 1
                    total_len += d
                    if total_len > MAX_LEN:
                        break
                    mult += [str(d)] * d
            else:
                # total_len > 0 and <= MAX_LEN
                # generate all unique permutations of this multiset
                for perm in set(itertools.permutations(mult)):
                    # no zeros, so leading zero not a problem, but keep guard if it ever appears
                    if perm[0] == '0':
                        continue
                    nums.add(int(''.join(perm)))

        sorted_nums = sorted(nums)
        for x in sorted_nums:
            if x > n:
                return x

        # fallback (shouldn't happen for given constraints)
        return None
