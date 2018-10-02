## Terminal Snippets:

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




