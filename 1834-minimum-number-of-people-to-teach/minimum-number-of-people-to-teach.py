class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        # Step 1: Convert each user's known languages into a set for fast lookup
        lang_sets = [set(l) for l in languages]

        # Step 2: Find users involved in problematic friendships
        need_teaching = set()
        for u, v in friendships:
            u, v = u - 1, v - 1  # convert to 0-index
            if lang_sets[u].isdisjoint(lang_sets[v]):  # no common language
                need_teaching.add(u)
                need_teaching.add(v)

        # Step 3: If no one needs teaching, answer is 0
        if not need_teaching:
            return 0

        # Step 4: Count how many users would need teaching for each language
        min_teach = float("inf")
        for lang in range(1, n + 1):
            count = 0
            for user in need_teaching:
                if lang not in lang_sets[user]:  # user needs to learn this language
                    count += 1
            min_teach = min(min_teach, count)

        return min_teach
