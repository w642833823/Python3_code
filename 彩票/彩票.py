import random
import sys
# 获取参数信息
r_num = int(sys.argv[1])
b_num = int(sys.argv[2])
# 确定参数范围是否合理
if (r_num>5 and r_num<17 and b_num>0 and b_num<17):
# 产生随机数
    x=random.sample(range(1,34),r_num)
    # 排序默认升序从小大大
    x.sort()
    y=random.sample(range(1,17),b_num)
    y.sort()
    for red in x:
        print("\033[31m %s" %red ,end=' ')
    print('+ ',end=' ')
    for blue in y:
        print("\033[34m %s" %blue,end=' ')
    print ("\033[0m 选号完毕！愿君高中！",end=' \n')
else:
     print('输入有误，第一个数应大于5小于17，第二个数应大于0小于17')

