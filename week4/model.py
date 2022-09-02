import numpy as np
import pickle
import xlrd

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
workbook = xlrd.open_workbook(r"US_trade_in_goods_and_services.xls")
sheet = workbook.sheet_by_index(0) # sheet 1
X = np.zeros((56,3))
BOP = np.zeros((56)) # goods' Balance of Payment

count = 0
for i in range(sheet.nrows):
    if isfloat(sheet.cell_value(i,0)):
        X[count,0] = sheet.cell_value(i,0) # year
        X[count,1] = sheet.cell_value(i,2) # Goods
        X[count,2] = sheet.cell_value(i,3) # services
        
        count +=1

count = 0       
for i in range(sheet.nrows):
    if isfloat(sheet.cell_value(i,1)):
        BOP[count] = sheet.cell_value(i,1)
        count +=1

# fitting model with training data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, BOP)

# saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2016,-500361,261993]]))