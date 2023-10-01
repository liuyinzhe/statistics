import numpy as np
import pandas as pd
from scipy import stats as sts

data =  [2,23,4,15,26,32,23,36]

# 算数平均数(arithmetic mean): 数值累加除以个数
print("arithmetic mean:",np.mean(data))

# 几何平均数(geometric mean): 数值累乘，之后开n(个数)方
print('geometric mean:',sts.gmean(data))

# 调和平均数(harmonic mean): 数值倒数的平均数的倒数
print('harmonic mean:',sts.hmean(data))

# 中位数(median): 排序后，位置在中间的值
# 偶数个输入会计算两个中间值的平均值
print('median:',np.median(data))

# 众数(mode): 出现次数最多的数字
print(sts.mode(data))
mode_obj=sts.mode(data)
print('mode:',mode_obj.mode)
print('count:',mode_obj.count)

# 极差(range)
print('range:',np.ptp(data))

# 四分位数
print('lower quartile(25%):',sts.scoreatpercentile(data,25)) #25分位数
print('upper quartiles(75%):',sts.scoreatpercentile(data,75)) #75分位数

# 四分位距(interquartile range; IQR)
print('IQR:',sts.scoreatpercentile(data,75)-sts.scoreatpercentile(data,25))


# 方差(variance)
print('variance:',sts.tvar(data,ddof = 0))# ddof=1时,分母为n-1 样本方差 s² ;ddof=0时,分母为n 总体方差 σ²

# 标准差/均方差(StandardDeviation)
print('StandardDeviation:',sts.tstd(data,ddof = 0))# ddof=1时,分母为n-1 样本标准差 s ;ddof=0时,分母为n 总体标准差 σ
    # numpy.std() 
        #默认是除以 $n$ 的 即是有偏的; numpy.std(ddof=1) 加入参数可以计算无偏的
    # pandas.std() 
        #默认是除以 $n-1$ 的 即是无偏的; pandas.std(ddof=0) 加上参数可以计算有偏的

# 手动计算样本标准差
# np.sqrt() 计算非负平方根
#np.sqrt(((data - np.array(data).mean())**2).sum()/(len(data)-1)) # 分母为n-1
#np.sqrt(((data - np.array(data).mean())**2).sum()/len(data))# 分母为n

# Numpy计算标准差
print('有偏（n）',np.std(data) ,'无偏（n-1）',np.std(data,ddof = 1))
# Pandas计算标准差
print('有偏（n）',pd.Series(data).std(ddof=0) ,'无偏（n-1）',pd.Series(data).std(ddof=1))




# 变异系数/离散系数/差异系数(CoefficientOfVariation)

# 当需要比较两组数据离散程度大小的时候，如果两组数据的测量尺度相差太大，或者数据量纲的不同，直接使用标准差来进行比较不合适
# 反映数据离散程度的绝对值。其数据大小不仅受变量值离散程度的影响，而且还受变量值平均水平大小的影响。
print('CoefficientOfVariation:',sts.tstd(data)/sts.tmean(data))
# 原始数据标准差与原始数据平均数的比


# 偏度(Skewness)
# 用来度量随机变量概率分布的不对称性
print('Skewness',sts.skew(data,bias=False)) # bias=False 代表计算的是总体偏度，bias=True 代表计算的是样本偏度


# 峰度(Kurtosis)
# 用来度量随机变量概率分布的陡峭程度
print('Kurtosis',sts.kurtosis(data,bias=False)) # bias=False 代表计算的是总体峰度，bias=True 代表计算的是样本峰度
