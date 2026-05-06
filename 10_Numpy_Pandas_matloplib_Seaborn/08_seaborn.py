import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#글꼴 깨짐 방지나 스타일은 보통 import 나 from 아래 작성
plt.rcParams['font-family'] = 'D2Coding'
plt.rc['axes.unicode_minus']
#


# Seaborn에 존재하는 데이터 갖고오기
# 식장 팁 데이터럼 존재하는 데이터 갖고오기

#샘플 데이터(seaborn 내장>
#샘플
#
#
df = sns.load_dataset('tips')
sns.histplot(df['total_bill'], kde=True)
plt.show()
sns.scatterplot(x='total_bill', y='tip', data=df)





sns.set_theme(style='whitegrid')
sns.set_palette('pastel')