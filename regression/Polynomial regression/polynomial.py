# -*- coding: utf-8 -*-
"""polynomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dcqOR4d2e2nuRlK7OpOam-lTMnKg9eQA

# Importing libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""# Importing the dataset

"""

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(x)

"""# Training the linear Regression model on the whole dataset

"""

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

"""# Training the polynimal regression model"""

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)  #transform to matrix of different powers
lin_reg_2 = LinearRegression()  #merge the linear part
lin_reg_2.fit(x_poly, y)

"""# Visualing the linear regression results"""

plt.scatter(x, y , color='red')
plt.plot(x, lin_reg.predict(x), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""# Visualing the Polynomial Regression results"""

#make the plot smooth
x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x, y , color='red', label='observed value')
plt.plot(x, lin_reg_2.predict(x_poly), color='blue', label='predicted value')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.legend()
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

"""# Predicting a new result with linear regression"""

lin_reg.predict([[6.5]])

"""# Predicting a new result with Polynomial regression"""

lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))