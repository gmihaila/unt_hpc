#!/bin/bash
######################################
# Example of a SLURM job script for Talon3
# 
# SBATCH -p public
#	Defines the partition which may be used to execute this job.
# 
# SBATCH -J job_name
#	Defines the job name.
# 
# SBATCH -o JOB.o%j
#	Defines the output file name.
# 
# SBATCH -e JOB.e%j
#	Defines the error file name.
#
# SBATCH --qos general
#	Defines the QOS the job will be executed. (debug, general, 
#	large are the only options)
#
#
# SBATCH --exclusive
#	Sets the job to be exclusive not allowing other jobs to 
#	share the compute node.  This is required for all large QOS submissions.
# 
# SBATCH -t 80:00:00
#	Sets up the WallTime Limit for the job in hh:mm:ss.
#
# SBATCH -n 84
#	Defines the total number of mpi tasks.
#
# SBATCH -N 3
#	Defines the number of compute nodes requested.
#
# SBATCH --ntasks-per-node 28
#	Defines the number of tasks per node.
#
# SBATCH -C c6320
#	Requests the c6320 compute nodes.
#	(Also can request r420, r720, and r730 compute nodes)
#
# SBATCH --mail-user=user@unt.edu
#	Sets up email notification.
#
# SBATCH --mail-type=begin
#	Email user when job begins.
#
# SBATCH --mail-type=end
#	Email user when job finishes.
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
