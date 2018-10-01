## Example of  job script:

</br>


* ### Command used (always leave it like this):
```
 #!/bin/bash 
```

</br>


* ###	Defines the partition which may be used to execute this job (Always keep public).
```
 #SBATCH -p public 
```

</br>

* ###	Defines the job name - it can be any name you want
```
 #SBATCH -J job_name
```

</br>

* ###	Defines the output file name. %j will add the JOBID to the output_name.o file
```
 #SBATCH -o output_name.o%j
```

</br>

* ###	Defines the error file name. %j will add the JOBID to the error_name.o file
```
 #SBATCH -e error_name.e%j
```

</br>

* ###	Defines the Quality of Service (**QOS**) the job will be executed. Options to use: (debug, general, large)
 * debug - 2 hour and 2 node limit with **high priority**
 * general - 72 hour and 560 CPU cores limit with default partition
 * large - limit to 20 nodes, unlimited hours, allow exclusive jobs and **low priority**
 
```
     #SBATCH --qos general
```

</br>

* ###	Sets the job to be exclusive not allowing other jobs to share the compute node.  This is required for all large QOS submissions.
```
 #SBATCH --exclusive
```

</br>

* ###	Sets up the WallTime Limit for the job in hh:mm:ss.
```
 #SBATCH -t 80:00:00
```

</br>

* ###	Defines the total number CPU cores:
```
 #SBATCH -n 84
```

</br>

* ###	Defines the number of compute nodes requested:
```
 #SBATCH -N 3
```

</br>

* ###	Defines the number of tasks per node:
```
 #SBATCH --ntasks-per-node 28
```

</br>

* ###	Requests the c6320 compute nodes. (Also can request r420, r720, and r730 compute nodes)
```
 #SBATCH -C c6320
```

</br>

###	Sets up email notification.
\#SBATCH --mail-user=user@unt.edu
```

```

</br>

###	Email user when job begins.
\#SBATCH --mail-type=begin
```

```

</br>

###	Email user when job finishes.
\#SBATCH --mail-type=end
```

```

######################################
 
#SBATCH -J my_example_job
#SBATCH -o ./out/example_job.o%j
#SBATCH -e my_example_job.e%j
#SBATCH -p public
#SBATCH --qos general
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 12:00:00
 
### Loading modules. To see all modules use $ module avail 
module load python
 
python test.py
