class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combinationSumHelper(current_list,listOfLists,candidates,i,number):
            if number < 0:
                return
            elif number == 0:
                listOflists.append(list(current_list))
                return
            else:
                for i in range(i,len(candidates)):
                    current_list.append(candidates[i])
                    combinationSumHelper(current_list,listOfLists,candidates,i,number-candidates[i])
                    current_list.pop()
        
      
        listOflists= []
        current_list = []
        combinationSumHelper(current_list,listOflists,candidates,0,target)
        
        return listOflists
