#least squares

y = [input().split() for _ in range(5)]

from sklearn import linear_model
import numpy as np

lm = linear_model.LinearRegression()
lm.fit(x,y)

def formula(x,a,b):
	return a + b*x

print(formula(80, lm.intercept_, lm.coef_[0]))
