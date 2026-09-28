class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bello = [-x for x in nums]
        heapq.heapify(bello)
        # bst = [-i for i in bst]
        for i in range(k-1):
            heapq.heappop(bello)
        return -bello[0]

            

        