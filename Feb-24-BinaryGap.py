
class Solution:
    
    def binaryGap(self, N):
        
        bin_str = bin(N)
        bin_list= [i for i in range(2,len(bin_str)) if bin_str[i] =="1"]
        
        if len(bin_list) == 1:
            gap = 0
        else:
            gap = max([bin_list[j+1] - bin_list[j] for j in range(len(bin_list)-1)])
        
        
        return gap
     
