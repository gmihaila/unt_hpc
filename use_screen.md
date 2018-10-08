## How to use screen

**For more info [here](https://www.rackaid.com/blog/linux-screen-tutorial-and-how-to/)**

**Talon 3 comes with screen installed.**

**It is very useful to use when you want to close a terminal session without interrupting (especially when you use Job Interactive).**

**After you login to Talon:**



```
$ ssh euid123@talon3.hpc.unt.edu
```
**You can type:**


```
$ screen --help
```
To find out some commands.

### To create a new screen:


```
$ screen -S screen_name
```
It will open up a new terminal window in the same current window with the screen_name (*it can be any name you want*) you specified.

Here you can request a node, or just run any code. Once you want to log-out/**detach**, but keep the terminal running just type:

### CTRL + a + d

It will detach from the terminal and come back to your previous terminal.

**You can have as many screens setup as you want.**

### To see all your screens type:


```
$ screen -ls
```

### To login back in one of the screens (attach):


```
$ screen -r screen_name
```


### Create a new screen and detach:


```
$ screen -dmS screen name
```
This is very useful when you are doing an interactive job.

### srun + screen + detach


```
$ screen -dmS screen_name srun -p public --qos general --mail-user=user@unt.edu --mail-type=ALL -N 1 --pty bash
```
Opens up a screen, runs the *srun* command with email notification and then it detaches.

Now you just need to wait for email notification when node was allocated so you can screen back in using the screen_name you provided.

This way you can shutdown your computer, or move to a different computer. It is also very useful when you have a bad internet connection, you can lose your place in the queue if terminal session ends!


