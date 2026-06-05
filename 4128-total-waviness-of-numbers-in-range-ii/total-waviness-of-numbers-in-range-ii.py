class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            memo = {}

            def dp(pos, tight, started, length_state, a, b):
                key = (pos, tight, started, length_state, a, b)

                if key in memo:
                    return memo[key]

                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wavy = 0

                for d in xrange(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            0,
                            0
                        )
                        total_count += cnt
                        total_wavy += wav

                    elif not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            1,
                            0,
                            d
                        )
                        total_count += cnt
                        total_wavy += wav

                    elif length_state == 1:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            2,
                            b,
                            d
                        )
                        total_count += cnt
                        total_wavy += wav

                    else:
                        add = 1 if ((b > a and b > d) or
                                    (b < a and b < d)) else 0

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            2,
                            b,
                            d
                        )

                        total_count += cnt
                        total_wavy += wav + add * cnt

                memo[key] = (total_count, total_wavy)
                return memo[key]

            return dp(0, True, False, 0, 0, 0)[1]

        return solve(num2) - solve(num1 - 1)