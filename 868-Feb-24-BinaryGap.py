class Solution:
    
    def binaryGap(self, N):
        
        bin_str = bin(N)
        bin_list= [i for i in range(2,len(bin_str)) if bin_str[i] =="1"]
        
        if len(bin_list) == 1:
            gap = 0
        else:
            gap = max([bin_list[j+1] - bin_list[j] for j in range(len(bin_list)-1)])
        
        
        return gap
    
    '''
哈哈！居然在Github上写日记，我也真是牛！

今天去了Getty Villa，欣赏了好多希腊的艺术品，原来palmyra也遭遇过和圆明园类似的浩劫。然后有心人搬回来完壁残垣陈列在博物馆橱窗里。
里面的玉器用的词是chalcedony而非jade，我也不知道这两者究竟有什么区别。

第一次做二进制的题，找到二进制为1的数字跨度最大的数。先开始想通过index或者（find），通过索引，然后计算跨度，未成功。
又试了试rfind从右边找，还是不成功

后来我意识到原来理解错题意了，问的是相邻的1，oh no
躺在床上想题，翻来覆去也睡不着。突然强迫症又发作了，有种小时候解应用题的感觉。

第二天刷Leetcode，虽然不建议一道题用超过一个小时，但我是通过刷题顺便学习嘛，时间花得长点也无所谓，因为我感兴趣。
刚才才弄好，
我就是手动设置一个元素，gap为0

网易轻松一刻大波儿经常说的一句话：再来一段（道）儿

'''
     
