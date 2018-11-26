
# coding: utf-8


# data analysis libraries
import numpy as np
import pandas as pd


# data visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns


train = pd.read_csv("Machine Learning/train.csv")
test = pd.read_csv("Machine Learning/test.csv")
train.describe(include='all') #요약하여 통계를 내주는 함수, include = All하면 NaN값들 포함함


train.head()
train.sample()
train.tail()
train.loc()


sns.barplot(x = 'Sex', y = 'Survived', data = train)


print("Percentage of females who survived:", train['Survived'][train['Sex'] == 'female'].value_counts(normalize = True)[1]*100)

print("Percentage of Pclass who survived:", train['Survived'][train['Pclass'] == 1].value_counts(normalize = True)[1]*100)


train["Age"] = train["Age"].fillna(-0.5) #NaN값 채우기


bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
train['AgeGroup'] = pd.cut(train["Age"], bins, labels = labels)
test['AgeGroup'] = pd.cut(test["Age"], bins, labels = labels)
sns.barplot(x="AgeGroup", y="Survived", data=train)
plt.show()


# In[20]:


combine = [train, test]
#combine[0] = train
#combine[1] = test


for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    # dataset에서 Name이라는 col에서 extract 한다. 정규식에 따라서


pd.crosstab(train['Title'], train['Sex'])


for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Capt', 'Col',
    'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
    
    dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

train[['Title', 'Survived']].groupby(['Title'], as_index=False).mean()


title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Royal": 5, "Rare": 6}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0) #해당되지 않는 경우는 0으로 취함

train.head()


#Fare중에서 NaN을 처리할 경우 운임요금의 평균값을 취함
#fill in missing Fare value in test set based on mean fare for that Pclass 
for x in range(len(test["Fare"])):
    if pd.isnull(test["Fare"][x]):
        pclass = test["Pclass"][x] #Pclass = 3
        test["Fare"][x] = round(train[train["Pclass"] == pclass]["Fare"].mean(), 4)
        
#map Fare values into groups of numerical values
train['FareBand'] = pd.qcut(train['Fare'], 4, labels = [1, 2, 3, 4]) #등분을 나누어서 4등급으로 매기겠다
test['FareBand'] = pd.qcut(test['Fare'], 4, labels = [1, 2, 3, 4])

#drop Fare values
train = train.drop(['Fare'], axis = 1)
test = test.drop(['Fare'], axis = 1)


train.head()

test.head()


# ## 지도학습 _ 회귀분석


from sklearn.datasets import load_boston


from sklearn.linear_model import LinearRegression


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#데이터 로드
boston = load_boston()


# #CRIM - 범죄율
# #INDUS - 비소매상업지역 면적 비율
# #NOX - 일산화질소 농도
# #RM - 주택당 방 수
# #LSTAT - 인구 중 하위 계층 비율
# #B - 인구 중 흑인 비율
# #PTRATIO - 학생/교사 비율
# #ZN - 25000평방 피트를 초과 거주지역 비율
# #CHAS - 찰스강의 경계에 위치한 경우는 1, 아니면 0
# #AGE - 1940년 이전에 건축된 주택의 비율
# #RAD - 방사형 고속도로까지의 거리
# #DIS - 직업센터의 거리
# #TAX - 재산세율

X = pd.DataFrame(boston.data, columns = boston.feature_names)
y = pd.DataFrame(boston.target, columns = ["MEDV"])
print(X.head())
print(y.head())


#Linear Regression 클래스 객체 생성
model = LinearRegression(fit_intercept = True) #fit_intercept : 상수항 유무 결정


#fit 메서드로 모형 추정 (Augmentation은 자동 수행)
model_boston = model.fit(X, Y)


print('weight: ', model_boston.coef_)
print('bias: ', model_boston.intercept_)


#생성된 모델로 예측하기 -> 부동산 가치에 가장 많은 영향을 미치는 feature를 뽑는 작업 등으로 응용 가능


#입력데이터의 평균값

print(X.mean())

#입력 데이터의 평균값을 변형하여 만든 가상의 데이터
X_new = [3.6, 12, 12, 0.05, 0.4, 6.5, 79, 4, 9, 400, 19, 354, 12]


#원래 데이터와 동일한 형태의 데이터 프레임을 만들어야 한다
dfx_new= pd.DataFrame(np.array(X_new)[:, np.newaxis].T, columns=boston.feature_names)

print(dfx_new)

predictions_new = model_boston.predict(dfx_new)
print('predictions: ', predictions_new)


#실제 값과 예측값의 비교
predictions = model_boston.predict(X)


plt.scatter(y, predictions)
plt.xlabel(u"Real Value")
plt.ylabel(u"Prediction")
plt.show() #만약 직선과 가까운 모습을 보이고 있다면 잘 추정한 것, 너무 많이 퍼져있다면 예측이 잘못된 것


# ## 지도학습_분류

# Logistic Regression, 회귀분석이라고 말하지만 분류 모델임
# 
# 어떤 값이 주어졌을 때, 가장 연관성이 큰 카테고리를 찾아내는 모형
# 
# 어떤 표본에 대한 데이터가 주어졌을 때, 그 표본이 어떤 카테고리에 속하는지를 알아내는 문제
# 
# 분류모형 - 판별함수 모형..
# 
# 분류의 사례 : ex) Spam or Ham, 양성 or 악성, 카드 사기 분류 등
# 
# 분류하기 위해서는 Linear Regression(선형, 값이 무한대까지)을 0과 1사이로 수렴하도록 만들게 하는 과정이 필요함 <- 합성함수(Sigmoid)
# 
# 로지스틱 함수 : 모든 점에서 기울기가 증가, 0과 1사이의 값을 취함. 이처럼 로지스틱 함수를 이용하여 Linear Regression과 합성하여 수렴시킴
# 
# 이러한 아이디어를 "로지스틱 리그레션"이라 부름
# 
# Cost함수 Convex하게 형성되도록 Gradient Descent를 적용하기 전에 log함수를 취하여 적절하게 변경해줌
# 
# y = 1 (실제값)인 경우 -log(h(X)), y = 0인 경우 -log(1-h(x)) 이를 코딩하려면 if조건문을 사용하기에 한 식으로 바꾸어 만들어줌
# 
# Multinomial Classification -> 0과 1 으로는 구분되지 않는, 카테고리가 3개 이상이 되는 분류 문제를 말함
# 
# A, B, C로 분류가 된다고 한다면, 이를 각각 0~1사이 Sigmoid, 전체의 합을 1로 하는 모델 : Softmax
# 
# Softmax 는 각 y = WX 값을 평균내서 0과 1사이의 값으로 반환함 (각 값을 e의 지수로 하여 평균내고, 가중평균한 값을 구함)


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf


# #Tensorflow의 경우 노드로 각 값을 선언하여 네트워크 그래프를 그림
# #데이터의 기본 단위를 Tensor로 부름 - np array와 같은 형태를 취함
# #a = 1을 선언하고 print(a)를 하면 1 값을 반환하지만, tensorflow의 경우 a tensor에 대한 정보가 뜨게 됨
# #실제 러닝을 해보아야 실행이 되는 부분



def LogisticRegression(X_new):
    x = [[1., 1., 1., 1., 1., 1.,],
        [2., 3., 3., 5., 7., 2.,], #광고 문구 개수
        [1., 2., 5., 5., 5., 5.,]] # 비속어 개수 -> 총 w는 2개 -> +1, 3개
    y = [0, 0, 0, 1, 1, 1] # 0 : ham, 1 : spam
    
    Xdata = tf.placeholder(tf.float32) #값을 넣는 것이 아니라 자리만 잡아두는 식
    Ydata = tf.placeholder(tf.float32)
    
    w = tf.Variable(tf.random_uniform([1, 3], -1, 1)) # (개수, 시작점, 끝점) - weight는 3 by 1(출력차원)로 선언해야함. wx라면 [1,3], xw라면 [3,1]
    
    wx = tf.matmul(w, Xdata) # matmul = 매트릭스 곱
    hypothesis = tf.div(1., 1. + (tf.exp(-wx))) # Sigmoid+
    cost = -tf.reduce_mean(Ydata * tf.log(hypothesis) + (1 - Ydata) * tf.log(1 - hypothesis)) #Cost함수 1줄 식
    learning_rate = tf.Variable(0.1) # learning_code를 변수로 선언하는 것이 쉬움
    
    optimizer = tf.train.GradientDescentOptimizer(learning_rate) #convex한 gradient를 가정했기 때문에 Optimizer, learning_rate 을 변수값으로 취함
    train = optimizer.minimize(cost)
    
    #여기까지가 Tensorflow Build한 과정
    
    sess = tf.Session()
    sess.run(tf.global_variables_initializer()) #session을 열어서 Initializer를 Run하도록 만듦
    
    
    for i in range(10001):
        sess.run(train, feed_dict = {Xdata: x, Ydata: y}) #train만을 Running시키면 됨, Xdata, Ydata는 Placeholder, 거기에 x, y를 넣음
        if i % 200 == 0:
            print(sess.run(cost, feed_dict = {Xdata: x, Ydata: y}), sess.run(w))
            
    print('This mail is', end ='\n')
    mail = ['ham-mail', 'spam-mail']
    pred = sess.run(hypothesis, feed_dict = {Xdata : X_new})
    print(mail[int(round(pred[0][0], 1))])
    sess.close()

X_1 = input('waste: ') #입력받는 값을 str으로 받아 밑에서 float으로 다시 변환
X_2 = input('crazy: ') # 스팸과 비속어 개수를 입력받음

X_new = [[1.], [float(X_1)], [float(X_2)]]
LogisticRegression(X_new) #test
