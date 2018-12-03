# load library
# https://www.rdocumentation.org/packages/neuralnet/versions/1.33/topics/neuralnet 
library(neuralnet)
library(boot)
library(plyr)
library(matrixStats)



# url('https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/09/07122416/cereals.csv')
data <- read.csv("cereals.csv", head = TRUE)


# Random sampling
samplesize = 0.60 * nrow(data)
set.seed(80)
index = sample( seq_len ( nrow ( data ) ), size = samplesize )

# Create training and test set
datatrain = data[ index, ]
datatest = data[ -index, ]

# Scale data for neural network 2-means apply each column

# get max and min vector of each column
max = apply(data , 2 , max)
min = apply(data, 2 , min)
# scale: center value is subtracted; scale value is divided
scaled = as.data.frame(scale(data, center = min, scale = max - min))



## Fit neural network 

# creating training and test set
trainNN = scaled[index , ]
testNN = scaled[-index , ]

# fit neural network
set.seed(2)
NN = neuralnet(rating ~ calories + protein + fat + sodium + fiber, trainNN, hidden = c(3) , linear.output = T )

# plot neural network
plot(NN)


## Prediction using neural network

predict_testNN = compute(NN, testNN[,c(1:5)])
# rescale back!
predict_testNN = (predict_testNN$net.result * (max(data$rating) - min(data$rating))) + min(data$rating)

plot(datatest$rating, predict_testNN, col='blue', pch=16, ylab = "predicted rating NN", xlab = "real rating")

abline(0,1)

# Calculate Root Mean Square Error (RMSE)
(sum((datatest$rating - predict_testNN)^2) / nrow(datatest)) ^ 0.5

