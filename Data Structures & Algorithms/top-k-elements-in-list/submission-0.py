class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appear = Counter(nums)
        final = []
        list_tup = []
        for i in appear.keys():
        #make [(key, # appear), ---]
            list_tup.append((i, appear[i]))
        sort_list_tup = sorted(list_tup, key = lambda x: -x[1])

        #for made list, sort by lambda with index 1 of tuple
        for i in (range(k)):
            final.append(sort_list_tup[i][0])
        #append top 
            

        return final
            

        #return k most frequent 
