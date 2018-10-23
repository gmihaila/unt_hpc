## Keras with multi GPU


If you want to use certain GPU's, specify the name of GPUs you want to use.

To find out what GPU's you have, use the command:



```
 $ nvidia-smi
```

![snpa](https://github.com/gmihaila/machine_learning_platform_gpu/blob/master/snaps/smi_nvidia.png)



```
os.environ["CUDA_VISIBLE_DEVICES"]="2,3"
```

