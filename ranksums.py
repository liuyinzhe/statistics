import scipy.stats as ss
# ranksums
# 秩和检验
x = [0.16910235172664467, 0.2020437094569132, 0.6924720854383165, 0.5262249846925307, 0.7309038310126759, 0.972498016667232, 0.6576645372688086, 0.6169914457716444]
y = [5.060202647284982, 5.7298963211653895, 5.0386386764253155, 5.625106039575542, 5.962911362302517, 5.731971211803443, 5.4344784457821005, 5.6345062250337, 5.847658639360786, 5.7380763398004735]

stats_m,p_m = ss.mannwhitneyu(x,y,alternative='two-sided')
print('p_2sided:',format(p_m, '.10f'))
stats_m,p_m = ss.mannwhitneyu(x,y,alternative='less')
print('p_less:',format(p_m, '.10f'))
stats_m,p_m = ss.mannwhitneyu(x,y,alternative='greater')
print('p_greater:',format(p_m, '.10f'))


# alternative表示备择假设的情况。默认alternative = 'two-sided。

# alternative = 'two-sided' 表示备择假设（H1）为两组数据有显著差异；  # 原假设H0: x,y 两者没有显著差异
# alternative = 'less'      表示备择假设（H1）为 x<y；              # 原假设H0: x !< y # x 不小于 y
# alternative = 'greater'   表示备择假设（H1）为 x>y；              # 原假设H0: x !> y # x 不大于 y

# p_2sided:     0.0000457059
# p_less:       0.0000228530
# p_greater:    1.0000000000

#p_2sided < 0.05 ：说明拒绝原假设H0，接受备择假设H1，结论是x和y有显著差异
#p_less   < 0.05 ：说明拒绝原假设H0，接受备择假设H1，结论是x比y小
#p_greater> 0.05 ：说明接受原假设H0，拒绝备择假设H1，结论是x不比y大