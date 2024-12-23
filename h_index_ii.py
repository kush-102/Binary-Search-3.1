class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l

    # time complexity is O(logn)
    # space complexity is O(n)
