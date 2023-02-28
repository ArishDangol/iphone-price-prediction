import pandas
# import matplotlib.pyplot as 
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
#print(data.head())  #gives output of the first 5 data
# plt.scatter(data['version'] ,data['price'])
# plt.show()

model = LinearRegression()
model.fit(data[['version']], data[['price']]) #first column name second column , etc
print(model.predict([[14]]))
print(model.predict([[20]]))