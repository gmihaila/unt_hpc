# Terminal Snippets:

<br>

## Modules:

**See available modules**

```
 $ module avail
```

**Load modules**

```
 $ module load name_of_module
```

**Unload module**

```
 $ module unload unload name_of_module
```

**Pre-Load modules when login to Talon:**

If you have modules you're using everytime you can pre-load them everytime you login to Talon.

This way you avaoid having to do module load everytime.

Terminal commands:
```
 $ cd
 $ vim .bashrc
```
Now you opened the bash file and you should see:


```
 module load gcc slurm
```
On the same line add any module you want loaded when ever you login to Talon. 

For example, to load python 3.6.5 anytime we login:


```
 module load gcc slurm python/3.6.5
```




<br>

## Job details:

**Find out your job id:**
```
 $ squeue -u euid123
```
 
**\$JOB_ID** can be seen under **JOBID** column

```
 $ scontrol show job $JOB_ID
```

**Kill a job. Users can kill their own jobs, root can kill any job.**

```
 $ scancel $JOB_ID
```

** Hold a job:**

```
 $ scontrol hold $JOB_ID
```


** Release a job:**

```
 $ scontrol release $JOB_ID
 ```
 
 <br>
 
 ## See Resources:
 
 ### Login to your node:

**Find out your node name:**
```
 $ squeue -u euid123
```
**\$NODE_NAME** can be seen under **NODELIST** column

**To login your node:**
```
 $ slogin $NODE_NAME
```
### Once logged in the node, use following commands:
**See load on CPUs:**

```
 $ mpstat -P ALL 
```
**See process running on CPUs:**

```
 $ pidstat
```

<br>

## Show breakdown of jobs by user


```
 $ squeue -h | awk '{print $4}' | sort | uniq -c | sort -rn
```

<br>

## Show queue statue by a particular user


```
$ squeue -u euid123
```

<br>


## Code on your computer and run it straight to an alocated node on Talon:
This can be very usefull when you have code on your personal computer that you want to run on Talon.

You will need your  **\$NODE_NAME** for this. 

**You run this command from your personal computer's terminal!**

```
$ ssh euid123@talon3.hpc.unt.edu slogin $NODE_NAME python < your_local_file.py 
```
*your_local_file.py* is a file located on your personal computer.

If you require certain modules to be loaded, pre-load them in your .bashrc file - See previous.


