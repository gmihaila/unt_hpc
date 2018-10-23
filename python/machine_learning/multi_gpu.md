## Keras with multi GPU

### NOTE: Keras will use1 GPU by default if it's properly installed!

If you want to use certain GPU's, specify the name of GPUs you want to use.

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


