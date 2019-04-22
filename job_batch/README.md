## Example of  Batch Job:


### Slurm Commands to write in your *.job* file


* #### Command used (always leave it like this):
```
 #!/bin/bash
```

* ####    Defines the partition which may be used to execute this job (Always keep public).
```
 #SBATCH -p public
```

* ####    Defines the job name - it can be any name you want
```
 #SBATCH -J job_name
```

* ####    Defines the output file name. %j will add the JOBID to the output_name.o file
```
 #SBATCH -o output_name.o%j
```

* ####    Defines the error file name. %j will add the JOBID to the error_name.o file
```
 #SBATCH -e error_name.e%j
```

* ####    Defines the Quality of Service (**QOS**) the job will be executed. Options to use: (debug, general, large)
  * **debug** - 2 hour and 2 node limit with **high priority**
  * **general** - 72 hour and 560 CPU cores limit with default partition
  * **large** - limit to 20 nodes, unlimited hours, allow exclusive jobs and **low priority**
 
 For example if you use **general**:
```
     #SBATCH --qos general
```

* ####    Sets the job to be exclusive not allowing other jobs to share the compute node.  This is required for all large QOS submissions.
```
 #SBATCH --exclusive
```

* ####    Sets up the WallTime Limit for the job in hh:mm:ss.
```
 #SBATCH -t 80:00:00
```

* ####    Defines the total number CPU cores:
```
 #SBATCH -n 84
```

* ####    Defines the number of compute nodes requested:
```
 #SBATCH -N 3
```

* ####    Defines the number of tasks per node:
```
 #SBATCH --ntasks-per-node 28
```

* ####    Requests the c6320 compute nodes. (Also can request r420, r720, and r730 compute nodes). [More Info](https://hpc.unt.edu/talon-compute-nodes)
```
 #SBATCH -C c6320
```

* ####    Use GPUs:
For example if you request **2 GPUs**
```
 #SBATCH --gres=gpu:2
```

* ####    Sets up email notification.
```
 #SBATCH --mail-user=user@my.unt.edu
```

* ####    Email user when:
  * **job begins:**
  ```
   #SBATCH --mail-type=begin
  ```
  * **job finishes:**
  ```
   #SBATCH --mail-type=end
  ```
  * **or both:**
   ```
   #SBATCH --mail-type=ALL
  ```

### Commands/process to execute on compute node:
* #### Load Modules.
For example if you want to load certain version of **python**:
   ```
   module load python/3.6.5
  ```
  * **To see all modules available, type this in your terminal (NOT the job file):**
  ```
  module avail
  ```
  * **To see all loaded modules, type this in your terminal (NOT the job file):**
  ```
  module list
  ```
  * **Remove module, type this in your terminal (NOT the job file):**
  ```
  module list
  ```
  * **Remove all modules, type this in your terminal (NOT the job file):**
  ```
  module purge
  ```

</br>

* #### Copy any files from home directory to scratch or change directory if needed:
```
 cp /home/$USER/file_name /storage/scratch2/euid123/file_name
 cd  /storage/scratch2/euid123/
```

      Where $USER is your EUID.

* #### Running code:
```
 python file_name
```

* #### Copy any files back to home directory if needed:
```
 cp /storage/scratch2/euid123/file_name /home/$USER/file_name
 ```

### There is no need to use all commands. Your job file can look as simple as:
```
 #SBATCH -J job_name
 #SBATCH -o output_job.o%j
 #SBATCH -e error_job.e%j
 #SBATCH -p public
 #SBATCH --qos general
 #SBATCH -N 1
 #SBATCH -n 1

 module load python

 python test.py
```
 

 
 
 ### To run this example use:
 

```
 $ sbatch job_template.job
```

### List jobs:


```
 $ squeue -u euid123
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


<br/>

### [< Go Back](https://github.com/gmihaila/unt_hpc)
