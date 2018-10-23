import os

os.environ["CUDA_VISIBLE_DEVICES"]="2,3"  #<------ SET WHICH GPU TO USE

import sys
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM


from keras.utils.training_utils import multi_gpu_model #<------------------Esential for multi GPUs usage


# BUILD MODEL FUNCTION

def BuildToyModel():
    # generate some dummy data
    n_examples = 1000
    n_features = 100

    x_train = np.random.random((n_examples, n_features))
    x_train = np.round(x_train, 2)
    x_train *= 100
    x_train = np.array(x_train, dtype=int)

    n_words = np.max(x_train)

    y_train = np.random.random(n_examples)

    # number of units in LSTM
    n_units = 256
    # numbe rof words
    n_words = 100500   #vocabulary size
    size_emb = 300     #size of embedding has to match
    size_seq = 50

    embedding_matrix = np.random.random((n_words+2, size_emb))

    # build model
    model = Sequential()
    model.add(Embedding(input_dim=(n_words+2), output_dim=size_emb, weights=[embedding_matrix],
                    mask_zero=False, trainable=False))
    # LSTM LAYER/S
    model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2))

    # TREAT AS REGRESSION PROBLEM
    model.add(Dense(1, activation='sigmoid'))
    
    return model, x_train, y_train

# Build model
model, x_train, y_train = BuildToyModel()

# Add how many GPUs you want/have
model = multi_gpu_model(model, gpus=2)          #<------------------Esential Part to run on GPUs

# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])

# model summary
print(model.summary())                          #<------------------See lambda layers distributed on each GPU

# batches
n_batch = 32       #<------------------make sure your batch is not too small
# epochs
n_epoch = 20

# train model
model.fit(x_train, y_train, epochs=n_epoch, batch_size=n_batch, verbose=1)

print("\nFinished!\n")
