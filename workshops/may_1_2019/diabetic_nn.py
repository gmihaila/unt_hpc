from keras.layers import Input, Dense
from keras.models import Model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from random import randint

# fix random seed for reproducibility
np.random.seed(seed=7)

# load pima indians dataset
dataset = np.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")

# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# split X and Y into Train 80% and Test 20%
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=7)

# attributes names
att_names = ["Number of times pregnant",
       "Plasma glucose concentration a 2 hours in an oral glucose tolerance test",
       "Diastolic blood pressure (mm Hg)",
       "Triceps skin fold thickness (mm)",
       "2-Hour serum insulin (mu U/ml)",
       "Body mass index (weight in kg/(height in m)^2)",
       "Diabetes pedigree function",
       "Age (years)", "Class variable (0 or 1)"]

# build each layer
model_input = Input(shape=(8,), name='INPUT')
model_layer1 = Dense(units=8, activation='relu', name='DENSE1')(model_input)
model_output = Dense(units=1, activation='sigmoid', name='OUTPUT')(model_layer1)
# assemble model
model = Model([model_input], model_output)
# compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# show summary of model
print(model.summary())

# Fit the model
model.fit(x_train, y_train, epochs=150, batch_size=10,  verbose=2)

# calculate predictions
y_pred = model.predict(x_test)

# round predictions
y_pred = [int(round(x[0])) for x in y_pred]

# make it a nicer format
y_pred = np.array(y_pred)

# accuracy
print("Accuracy: ",accuracy_score(y_test, y_pred))

# show some predictions
n_examp = 3
for i in range(0,n_examp):
  print("\n--- Example %s ---\n"%(i + 1))
  sel = randint(0, (len(x_test) - 1))
  for at, val in zip(att_names, x_test[sel]):
    print(at +":", val)
  print("Predict: ", ("diabetes" if y_pred[sel] else "no diabetes"))
  print("Actual:  ", ("diabetes" if y_test[sel] else "no diabetes"))

print("\nFinished!")
