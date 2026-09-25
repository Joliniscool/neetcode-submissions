class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #return smallest amount must eat pe rhour
        #min 
        # plan create list of __ to h 
        #   see if fulfill all condition with binary
        left = 1
        right = max(piles)
        mid = 0
        while left < right:
            # also smaller case 
            mid = (right+left)//2
            if sum([i//mid + 1 if i%mid != 0 else i//mid for i in piles]) <= h:
                right = mid
            else:
                left = mid + 1


        #for each number divide, if mod left over then + 1 
        # if total count > h then no pass and move to next 
        return left

        







        # if len(piles) >= h:
        #     return max(piles)
        # target = h//max(piles)
        # tuple_list = []  #hab to make target -val abs val
        # for val in piles:
        #     tuple_list.append((val, abs(target-val))) 
        # closest = min(tuple_list, key = lambda x: x[1])
        # closest = closest[0]
        
        # return closest





        