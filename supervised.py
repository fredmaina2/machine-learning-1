from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#the  dataset hours studied
x = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

#the examinaition score
y = [30,40,45,55,65,70,80,85,90,95] 

#the linear regretion model 
model = LinearRegression()

#training the model using the data
model.fit(x, y)

#to allow the user to enter the number of hours studied 
user_input = float(input("Enter hours studied please: "))

#to use input to predict the examination scores
prediction = model.predict([[user_input]])[0]

#to display the prediction rounded to two decimal places 
rounded_prediction = round (prediction, 2)
print(f"Predicted exam score: {rounded_prediction}")
