## Keras with multi GPU

<br>

### Code example [here](https://github.com/gmihaila/unt_hpc/blob/master/python/machine_learning/multi_gpu.py)

<br>

### IMPORTANT:
### Avoid interrupting a python file when using GPU's. Any unexpected interruption will leave the memory allocated on the GPU's.This will make the GPUs unusable and you will have to request another GPU node.

<br>

### Make sure you load the proper modules on Talon:

```
 module load tensorflow/1.10.1-gpu keras/2.2.0
```
<br>

## Using 1 GPU:
If you are running your code on a GPU node on Talon, Keras will use by default 1 GPU, BUT will do something VERY bad.
**It will allocate memory on all GPU's on the node and only use 1. In other words, it will make all GPUs on that node unavailable and use only 1. This is bad only when you requested more then 1 GPU!**
To avoid this you need to add this to at the beginning of your python code:

```
 import os
 os.environ["CUDA_VISIBLE_DEVICES"]="0"
```

<br>

## Using 2 GPUs or more:

**If you want to use certain GPU's, specify the name of GPUs you want to use.**

<br>

To find out what GPU's you have, use the command:


```
 $ nvidia-smi
```
You can see each GPU  number on the left side 0, 1, 2, 3:

![snpa](https://github.com/gmihaila/machine_learning_platform_gpu/blob/master/snaps/smi_nvidia.png)

If you only want to use GPUs 2 and 3 add this to your python file:

```
 os.environ["CUDA_VISIBLE_DEVICES"]="2,3"
```

In your import libraries you will want to import multi_gpu_model from Keras:



```
 from keras.utils.training_utils import multi_gpu_model
```

Then you can start coding your model in Keras and right before calling **compile** you need to distributed the model accross all GPUs:



```
 model = multi_gpu_model(model, gpus=2)
```


**Make sure the gpus= is not greater than the number of gpu's you asked! **


### These 3 lines of code are the only thing you need to add in order to run you python Keras model on 2 or more GPUs!

### *NOTE:* What if you have multiple models running on the same machine, but want to avoid using GPUs?
Since Keras will grab 1 GPU by default, you can specify what GPU's to use to nothing:

```
 os.environ["CUDA_VISIBLE_DEVICES"]=""
```

<br>

### *NOTE:* If you don't use the multi_gpu_model in Keras and you are using a multi GPU node on Talon, Keras will do something VERY bad.
**It will allocate memory on all GPU's on the node and only use 1. In other words, it will make all GPUs on that node unavailable and use only 1.**

<br/>

### [< Go Back](https://github.com/gmihaila/unt_hpc/blob/master/python/README.md)
