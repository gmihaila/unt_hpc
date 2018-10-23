## Keras with multi GPU


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

