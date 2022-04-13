import pandas as pd
import numpy as np
from functools import reduce 
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
import joblib
#Выберем только те строки, которые требуются в задании
slices = [(180,280),(370,470),(1000,1100),(1540,1640)]
data = pd.read_excel("data.xlsx")
data = data.loc[reduce(lambda x,y :x+y ,[list(range(s[0],s[1])) for s in slices])]

#На основании этой таблицы, создадим матрицу признаков, используя ранее сохраненные скейлер и энкодер
loaded_encoder = joblib.load(open("encoder.pkl", "rb"))
loaded_scaler = joblib.load(open("scaler.pkl", "rb"))

numerical_columns = list(data.columns)
numerical_columns.remove("I")
numerical_columns.remove("grade")

X = data[numerical_columns].values
categorical = loaded_encoder.transform(data["I"].values.reshape(-1, 1))
X = np.hstack((X,categorical))
X = loaded_scaler.transform(X)
#Загружаем модели и добавляем предсказания в таблицу
for loaded_model_name in ["NeuralNet","XGBoost"]:
    loaded_model = joblib.load(open("{}.pkl".format(loaded_model_name), "rb"))
    data[loaded_model_name] = loaded_model.predict(X)
#Сохраним таблицу в формате .xlsx
data.to_excel("result1.xlsx") 