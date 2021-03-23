```
import matplotlib.pyplot as plt
import numpy as np

# Figure -> Axes -> Axis -> Artist
# 在画图时，肯定有当前的Figure和Axes

# 设置显示中文
plt.rcParams['font.sans-serif'] = ['SimHei'] 
# 设置显示特殊字符
plt.rcParams['axes.unicode_minus'] = False

plt.ion() # 打开交互模式，每一步都会实时在图片反应，关闭命令plt.ioff()
fig = plt.gcf() # 获得当前的figure对象
ax = plt.gca() # 获取当前axes
art = plt.gci() # 获取当前artist

# 函数画图
plt.subplot(221) #参数必须三个数字，每次只建立并定位1个子图
plt.plot(x,y)
plt.subplot(222) #定位第2个子图
plt.scatter(x,y)

# 对象画图
# 一次性建立
fig, axes = plt.subplots(2, 2) 
ax1 = axes[0,0]
ax2 = axes[0,1]
ax3 = axes[1,0]
ax4 = axes[1,1]


fig = plt.figure()
# 一次性建立
axes = fig.subplots(2,2)
# 多次建立
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# 新增
ax = fig.add_subplot(331)
ax = fig.add_axes([a,b,c,d]) # a left margin b bottom margin c width% d height%
ax = fig.axes[0]

# 绘图命令
ax.scatter('a', 'b', c='c', s='d', data=data) # 散点图。data={'a':,'b':,'c':,'d':}
n, bins, patches = ax.hist(x, 50, density=1, facecolor='g', alpha=0.75) # 直方图
lines = ax.plot(x1, y1, x2, y2) # 折线图
ax.text(60, .025, r'$\mu=100,\ \sigma=15$') #在固定位置加入文字
ax1 = ax.twinx() #设置双坐标轴，此时公用x轴，ax1的y轴为右边的竖坐标轴


--------------------------------------------------------------------------------------------------
# 绘图命令 ---直方图
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75) #alpha透明度 patches就是组成直方图的每个小矩形


--------------------------------------------------------------------------------------------------
# 绘图命令 ---散点图
ax.scatter(x,y, c=color, s=volume, alpha=0.5) #透明度


--------------------------------------------------------------------------------------------------
# 绘图命令 --- 竖条形图并列

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')
# 如果是横条形图，用barh 

# 如果是横条形图，用set_yticks
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=90)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)


--------------------------------------------------------------------------------------------------
# 绘图命令 --- 竖条形图累积

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()



--------------------------------------------------------------------------------------------------
# 绘图命令 --- 横条形图

plt.barh(x,men_means,tick_label=labels)


--------------------------------------------------------------------------------------------------
# 绘图命令 --- 饼状图
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = [0, 0.1, 0, 0]  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


--------------------------------------------------------------------------------------------------
# 绘图命令 ---等高线
X, Y = np.meshgrid(x, y) # 把x,y数据生成mesh网格状的数据，因为等高线的显示是在网格的基础上添加上高度值
plt.contourf(X, Y, f(X, Y), 20, cmap=plt.cm.hot) # 填充等高线
C = plt.contour(X, Y, f(X, Y), 20) # 添加等高线
plt.clabel(C, inline=True, fontsize=12)

--------------------------------------------------------------------------------------------------
# 绘图命令 --- 添加表格
# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

--------------------------------------------------------------------------------------------------
# 绘图命令 ---三维
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

ax = plt.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False) # X，Y必须是数组

--------------------------------------------------------------------------------------------------
# 绘图命令 --- 填充颜色的多边形
plt.fill(x, y, facecolor='lightsalmon', edgecolor='orangered', linewidth=3)