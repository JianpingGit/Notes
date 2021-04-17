# 目录

* 1 supervised
    * 1.1 linear model
        * 1.1.1 perceptron
    * 1.2 nearest neighbors
        * 1.2.1 KNN 
    * 1.3 decisive tree
        - 1.3.1 Classification
* 2 unspervised
    * 2.1 clustering
        * 2.1.1 K-means
    * 2.2 decomposition
        * 2.2.1 PCA
        * 2.2.2 Factor Analysis

# 1 Supervised
## 1.1 linear Model
### 1.1.1 Perceptron 感知机
***
### [原理简介](https://blog.csdn.net/u011630575/article/details/79396135)  
> 感知机（perceptron）是二类分类的线性分类模型，其输入为实例的特征向量，输出为实例的类别。感知机对应于输入空间（特征空间）中将实例划分为正负两类的分离超平面。感知机是一种线性分类模型。  

感知机实际上表示为输入空间到输出空间的映射函数，如下所示：  

    f(x)=sign(w*x+b)  

### sklearn 实现  
```python
from sklearn.linear_model import Perceptron
# trainX,trainY 为训练数据集
# testX,testY 为测试数据集
p = Perceptron() # 生成类实例  
p = p.fit(trainX,trainY) #训练模型
p.coef_ # 模型生成的w
p.intercept_ # model b
p.score(testX,testY) # model precise rate on test data
p.predicte(data) # classification prediction using model 

```
## 1.2 nearest neighbors
### 1.2.1 KNN
***
原理简介
> 要分类的对象与训练集中，已知类标记的所有对象进行距离对比，由最近邻的
> k个对象决定最终类别。最终类别决定可遵循少数服从多数的投票法则（majority-voting），让未知实例归类为最邻近样本中最多数的类别。
度量距离的方法可采用，欧氏距离，余弦值（cos），相关度（correlation），曼哈顿距离等。  
优点：简单，易于实现，易于理解，通过对K的选择能一定程度上的具备丢噪音数据的健壮性（增大K值）
缺点：需要大量的空间存储已知实例，算法复杂度高（需要比较所有已知实例）。当样本分布不平均时，比如其中一个样本实例过多，容易被归纳为实例多的样本

### sklearn 实现  
```python
from sklearn.neighbor  import KNeighborsClassifier
knn = KNeighborsClassifier() # default k = 5,euclidean distance
knn.fit(xTrain,yTrain)
knn.score(xTest,yTest)
knn.predict(xTest)
```

## 1.3 decisive tree
### 1.3.1 Classification
***
原理简介
> XXX
> 

### sklearn 实现  
```python
import matplotlib.pyplot as plt
from sklearn.tree  import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X = load_iris()['data']
Y = load_iris()['target']
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y)
clf = DecisionTreeClassifier() # criterion{“gini”, “entropy”}, default=”gini”
clf.fit(Xtrain,Ytrain)

clf.predict(Xtest)
clf.score(Xtest,Ytest)
clf.get_depth()
clf.get_n_leaves()
```

# 2 Unsupervised
## 2.1 Clustering
### 2.1.1 K-Means
***
### 原理
在sklearn中，包括两个K-Means的算法，一个是传统的K-Means算法，对应的类是KMeans。另一个是基于采样的Mini Batch K-Means算法，对应的类是MiniBatchKMeans。一般来说，使用K-Means的算法调参是比较简单的。

\qquad用KMeans类的话，一般要注意的仅仅就是k值的选择，即参数n_clusters；如果是用MiniBatchKMeans的话，也仅仅多了需要注意调参的参数batch_size，即我们的Mini Batch的大小。

\qquad当然KMeans类和MiniBatchKMeans类可以选择的参数还有不少，但是大多不需要怎么去调参。下面我们就看看KMeans类和MiniBatchKMeans类的一些主要参数。





## 2.2 Decomposition
### 2.2.1 PCA
 
***  
### 特征值原理
原数据矩阵X  
1. 数据处理，中心化或均一化，得到矩阵A  
2. 计算协方差矩阵C  
3. 特征值分解，得到特征向量矩阵E和特征值D  
4. 根据特征值大小筛选前n个特征向量E'  
5. A.dot(E')即为降维后的主成分A'

Note：A'各成分的方差，即为特征值D

### sklearn实现
```python

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(dat) # 数据矩阵dat
lowDDat = pca.transform(dat) # 得到降维后的主成分
eigVals = pca.singular_values_ # 筛选后的特征值
eigVects = pca.components_ # 筛选后的特征向量
expVar = pca.explained_variance_ # 主成分的方差
expVarPer = pca.explained_variance_ratio_ # 主成分方差占总方差的比例
# expVar = eigVals**2/(m-1), m为样本数量
mean = pca.mean_ # 原数据均值
# lowDDat = (dat-mean).dot(eigVects.T)
datRecon = pca.inverse_transform(lowDDat)   
# 还原数据，但是还原后跟原数据不一样
# datRecon = lowDDat.dot(eigVects)+mean

```

### sklearn实现的数学原理
sklearn的PCA类并没有用协方差来推演得到主成分，而是用SVD  
如下代码同PCV结果等效
```python
import numpy as np

datMean = dat - dat.mean(axis=0) # 数据中心化
m1,eigValsAll,eigVectsAll = np.linalg.svd(datMean) # 奇异值分解  
eigIndex = np.argsort(eigVals)[::-1] # 获得特征值降序排列的index  
eigVects = eigVects[eigIndex][0:n] # 筛选特征向量
lowDDat = datMean.dot(eigVects.T) # 得到降维后主成分

```

### 2.2.2 Factor Analysis
***
类似PCV的逆运算，区别：PCA的主成分是由原数据线性组合而来，FA是用因子表示原数据  



