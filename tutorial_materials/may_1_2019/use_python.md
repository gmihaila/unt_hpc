# Use Python on Talon Workshop



## Load python



Check the modules you have loaded:

```
$ module list
```

See all modules available on Talon:



```
$ module avail
```

Find out what versions of python we have available on Talon.

Write the following command and press TAB twice.

```
$ module load python
```

If you plan on using python 3.6.5:

```
$ module load python/3.6.5
```

To see if it was loaded:

```
$ module list
```

And you will see **SOMETHING** like this:

```
Currently Loaded Modules:
  1) gcc/8.1.0   2) slurm/16.05.8   3) python/3.6.5
```

To see what libraries you have available on that version of Python:

```
$ pip freeze
```

### Let's do a test

Iterractive session:

```
$ srun -p public --qos general -N 1 -C c6320  --pty bash
```
What is c6320? [here](https://hpc.unt.edu/talon-compute-nodes)

This allocates a compute node c6320 and opens a terminal in it.

Now you can interract with the node as you would do in a regular terminal session.

What if I need another terminal open on that node?

```
slogin NODE_NAME
```
How to find **NODE_NAME**?

```
$ squeue -u euid123
```
Batch session:

Create a batch file with extension .job 

```
 #SBATCH -J job_name
 #SBATCH -o output_job.o%j
 #SBATCH -e error_job.e%j
 #SBATCH -p public
 #SBATCH --qos general
 #SBATCH -N 1
 #SBATCH -n 1
 #SBATCH -C c6320

 module load python/3.6.5

 python test.py
```

To run the batch job:

```
$ sbatch file.job
```


## "pip install"

So what if you need to install a library that is not on Talon?

```
$ pip install your_library --user
```
The library is only available to you and only on that main verison of python.



## Virtual Enviroment

### Why? 

* If you start a new project that needs certain libraries you will never use on other projects.

* Or you need to setup a fresh python enviroment with certain libraries.

<br>

Make sure you FIRST load version of python you want to create the virtual enviroment with:

```
$ module load python/3.6.5
```

Then simply create the virtual enviroment:

```
$ virtualenv env
```

Will create a folder in your current position named env containing the virtual enviroment.

If you need to create it in a different folder:

```
$ virtualenv /what/ever/path/env
```

To activate it simply do :

```
$ source /path/to/env/folder/bin/activate
```

You should see the name of the virtual enviroment in your temrinal line:

```
(env) [euid@t3-login ~]$ 
```

To get out of the virtual enviroment:



```
$ deactivate
```

### Make sure to have the module of python that you used to create the virtual enviroment loaded everytime before you stat using the virtual enviroment:

```
$ module load python/3.6.5
$ virtualenv env
```

Use virtual enviroment in batch file:

```
 #SBATCH -J job_name
 #SBATCH -o output_job.o%j
 #SBATCH -e error_job.e%j
 #SBATCH -p public
 #SBATCH --qos general
 #SBATCH -N 1
 #SBATCH -n 1
 #SBATCH -C c6320

 module load python/3.6.5
 
 source /path/to/virtual/enviroment/bin/activate
 
 python test.py
```

## Keras, Tensorflow, Pytorch

Load Keras:

```
$ module load keras/2.2.0
```

Load Tensorflow

```
$ module load tensorflow/1.10.1
```

Load PyTorch:

```
$ module load pytorch/1.0.1
```

### Each module will load the apropriate version of python that it works with!


## Predict diabetes using Keras

To download all materials:

```
$ git clone https://github.com/gmihaila/unt_hpc.git
```

Path to today workshop files:

```
$ cd unt_hpc/tutorial_materials/may_1_2019/
```

### Iteractive sesion:

Get a compute node:

```
$ srun -p public --qos general -N 1 -C c6320  --pty bash
```

Load module:

```
$ module load keras/2.2.0
```

Run the script:

```
$ python diabetic_nn.py
```

### Batch sesion:

Create a file with extension .job

```
 #SBATCH -J job_name
 #SBATCH -o output_job.o%j
 #SBATCH -e error_job.e%j
 #SBATCH -p public
 #SBATCH --qos general
 #SBATCH -N 1
 #SBATCH -n 1
 #SBATCH -C c6320

 module load keras/2.2.0
  
 python diabetic_nn.py
```

Launch the job:



```
$ sbatch file.job
```


## Use GPU / GPUs


### Batch sesion:

Create a file with extension .job

```
 #SBATCH -J job_name
 #SBATCH -o output_job.o%j
 #SBATCH -e error_job.e%j
 #SBATCH -p public
 #SBATCH --qos general
 #SBATCH -N 1
 #SBATCH -n 1
 #SBATCH -C c6320

 module load keras/2.2.0 tensorflow/1.10.1-gpu
  
 python gpu_diabetic_nn.py
```

Launch the job:

```
$ sbatch file.job
```

