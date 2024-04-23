from scipy.stats import kruskal,wilcoxon,mannwhitneyu
import numpy as np

def calc_quantile(numlist,method='nearest'):
    '''
    input : numlist 
    method
    ['linear', 'lower', 'higher', 'midpoint', 'nearest']
    https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
    '''
    lower_q = float(np.quantile(numlist,0.25,method=method))
    median = float(np.quantile(numlist,0.5,method=method))
    higher_q = float(np.quantile(numlist,0.75,method=method))
    
    return lower_q,median,higher_q

def calc_KruskalWallis(groups_set):
    # # 多组独立样本的数据
    # group1 = [1, 2, 3, 4, 5]
    # group2 = [6, 7, 8, 9, 10]
    # group3 = [11, 12, 13, 14, 15]

    # 执行Kruskal-Wallis H检验
    statistic, p_value = kruskal(*groups_set)

    # 打印结果
    # print("Kruskal-Wallis H statistic:", statistic)
    # print("p-value:", p_value)
    return statistic, p_value


def calc_wilcoxon(group1,group2):
    # 执行wilcoxon 检验
    if len(group1) == len(group2):
        result = wilcoxon(group1,group2,alternative='two-sided')
    else:
        result = mannwhitneyu(group1,group2,alternative='two-sided')
    
    statistic = result.statistic
    pvalue = result.pvalue

    return statistic, pvalue
