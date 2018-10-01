## Interactive Jobs 

[More info](https://hpc.unt.edu/slurm)
>
>
Interactive job sessions can be used on Talon if you need to compile or test software. An example command of starting an interactive sessions is shown below:



```
 $ srun -p public --qos general -N 1  --pty bash
```
This launches an interactive job session and lanches a bash shell to a compute node. From there, you can exectue software and shell commands that would otherwise not be allowed on the Talon login nodes.

### Login to your node


```
 slogin $NODE_NAME
```
**\$NODE_NAME** can be seen when **List Jobs** under **NODELIST** column

### List jobs:


```
 $ squeue -u $USER
```




### Get job details:
```
 $ scontrol show job $JOB_ID
```


### Kill a job. Users can kill their own jobs, root can kill any job.
```
 $ scancel $JOB_ID
```

### Hold a job:
```
 $ scontrol hold $JOB_ID
```


### Release a job:
```
 $ scontrol release $JOB_ID
```
