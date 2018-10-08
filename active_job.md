## Interactive Jobs

[More info](https://hpc.unt.edu/slurm)
>
>
Interactive job sessions can be used on Talon if you need to compile or test software. An example command of starting an interactive sessions is shown below:



```
 $ srun -p public --qos general -N 1  --pty bash
 
```
This launches an interactive job session and lanches a bash shell to a compute node. From there, you can execute software and shell commands that would otherwise not be allowed on the Talon login nodes.

You can use same **Slurm Commands**:



* ####    Defines the partition which may be used to execute this job (Always keep public).
```
  -p public
```

* ####    Defines the job name - it can be any name you want
```
 -J job_name
```

* ####    Defines the output file name. %j will add the JOBID to the output_name.o file
```
  -o output_name.o%j
```

* ####    Defines the error file name. %j will add the JOBID to the error_name.o file
```
 -e error_name.e%j
```

* ####    Defines the Quality of Service (**QOS**) the job will be executed. Options to use: (debug, general, large)
  * **debug** - 2 hour and 2 node limit with **high priority**
  * **general** - 72 hour and 560 CPU cores limit with default partition
  * **large** - limit to 20 nodes, unlimited hours, allow exclusive jobs and **low priority**
 
```
     --qos general
```

* ####    Defines the total number CPU cores:
```
 -n 84
```

* ####    Defines the number of compute nodes requested:
```
 -N 3
```

* ####    Defines the number of tasks per node:
```
 --ntasks-per-node 28
```

* ####    Requests the c6320 compute nodes. (Also can request r420, r720, and r730 compute nodes). [More Info](https://hpc.unt.edu/compute-nodes)
```
 -C c6320
```

* ####    Sets up email notification.
```
 --mail-user=user@unt.edu
```

* ####    Email user when:
  * **node gets allocated begins:**
  ```
   --mail-type=begin
  ```
  * **node gets released finishes:**
  ```
   --mail-type=end
  ```
  * **or both:**
   ```
   --mail-type=ALL
   ```
* ####    Use GPUs.
```
--gres=gpu: NUM_GPUS
```

### Login to your node:

Find out your node name:
```
 $ squeue -u euid123
```
**\$NODE_NAME** can be seen under **NODELIST** column

To login your node:
```
 slogin $NODE_NAME
```


### Get job details:

Find out your job id:
```
 $ squeue -u euid123
```
**\$JOB_ID** can be seen under **JOBID** column

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

### Example of requesting 1 node with email notificaiton:


```
 $ srun -p public --qos general --mail-user=user@unt.edu --mail-type=ALL -N 1 --pty bash
```
#### This is very useful because it notifies you when your node has been allocated to you so you can start work!



