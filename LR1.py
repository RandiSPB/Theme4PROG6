import pandas
from pandas import read_csv
import re
import string
parced_csv = pandas.read_csv('train.csv',sep=',', index_col='PassengerId', quotechar='"')

train = read_csv("train.csv")
sex = train[train.Sex == u'male']
print('Task_1:', len(sex), 'male', 'and', len(train) - len(sex), 'female')
print('Task_1:', (len(sex)*100)/len(train), '%male', 'and', 100 - (len(sex)*100)/len(train), '%female')
port_s = train[train.Embarked == u'S']
port_c = train[train.Embarked == u'C']
port_q = train[train.Embarked == u'Q']
print('Task_2:', 'port S -', len(port_s), 'port C -', len(port_c), 'port Q -', len(port_q))
died = train[train.Survived == 0]
print('Task_3:', 'Died', len(died), '%Died', len(died)/len(train)*100)
class_t = train[train.Pclass ==  3]
class_s = train[train.Pclass ==  2]
class_f = train[train.Pclass ==  1]
print('Task_4:', 'First class -', len(class_f)/len(train)*100,'Second class -', len(class_s)/len(train)*100,'Third class -', len(class_t)/len(train)*100)
cor1 = train["SibSp"].corr(train["Parch"], method = 'pearson')
print('Task_5:', 'find corr sibsp parch =', cor1)
cor2 = train["Age"].corr(train["Survived"], method = 'pearson')
print('Task_6.1:', 'find corr age survived =', cor2)
#cor3 = train["Sex"].corr(train["Survived"], method = 'pearson')
print('Task_6.2:', 'find corr sex survived = TypeError: unsupported operand type(s) for /: str and int')
cor4 = train["Pclass"].corr(train["Survived"], method = 'pearson')
print('Task_6.3:', 'find corr Pclass survived =', cor4)
print('Task_7:', 'Avg =', train["Age"].mean(), 'median =', train["Age"].median())
print('Task_8:', 'Avg =', train["Fare"].mean(), 'median =', train["Fare"].median())
name = train
name.reset_index(inplace = True, drop = True)
for i in range(len(name)):
    str = name["Name"][i]
    res = re.sub('['+string.punctuation+']', '', str).split()
    name.loc[i, 'Name'] =  res[2]
nameMan = name.loc[name["Sex"] == 'male']
print('Task_9: Popular man name', nameMan["Name"].value_counts().index[0])
nameMan = nameMan.loc[nameMan["Age"] > 15]
print('Task_10: Popular man name, when age > 15', nameMan["Name"].value_counts().index[0])
nameWoman = name.loc[name["Sex"]  == 'female']
nameWoman = nameWoman.loc[nameWoman["Age"] > 15]
print('Task_10: Popular woman name, when age > 15', nameWoman["Name"].value_counts())
