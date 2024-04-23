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
    # Kruskal-Wallis H 检验用于比较三个或以上独立样本的中位数是否相同，也称为方差分析的非参数替代方法
    statistic, p_value = kruskal(*groups_set)

    # 打印结果
    # print("Kruskal-Wallis H statistic:", statistic)
    # print("p-value:", p_value)
    return statistic, p_value


def calc_wilcoxon(group1,group2):
    # 执行wilcoxon 检验
    if len(group1) == len(group2):
        # Wilcoxon Signed-Rank Test(威尔科克森符号秩检验)
        # 用来进行配对样品的非参数检验
        result = wilcoxon(group1,group2,alternative='two-sided')
    else:
        # Mann–Whitney U-test （曼-惠特尼U检验）
        # Mann-Whitney-Wilcoxon Test
        # 用来检验两组独立样品是否来自两组不同的样品。
        result = mannwhitneyu(group1,group2,alternative='two-sided')
    
    statistic = result.statistic
    pvalue = result.pvalue

    return statistic, pvalue
