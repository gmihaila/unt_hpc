# (Mac and Linux Only)
## SSH Temrinal Easy Configuration

In order to login to talon you will have to use SSH command on **your personal computer's temrinal**:


```
$ ssh euid123@talon3.hpc.unt.edu
```

Then it will ask for you password. To make things easier you cna have it save the password and even create a shortcut so you can speed things up:

### Setup alias on you SSH connection:
Make sure you are in your home directory:


```
$ cd ~
```

Check if you have a folder names .ssh


```
$ ls -a
```

If you don't you have to create one:


```
$ mkdir .ssh
```
Now you need to create a file named config. Use Nano or Vim or any other editor you are comfortable with:


```
$ vim ~/.ssh/config
```
If, for example, you want to create a shortcut to ssh on Talon3, your config file should look like:


```
Host t3                                             
  HostName talon3.hpc.unt.edu                      
  User euid123
  Port 22
```
Where t3 (it can be any word you want) is the shortcut you will use instead of typing: 

```
$ ssh euid123@talon3.hpc.unt.edu
```
You will type:


```
$ ssh t3
```
### Save SSH password:
Now you have a shortcut, but you will still need to enter your password everytime.
In order to save your passwords you will have to create a keygen file:


```
$  ssh-keygen 
```
When prompted with this:


```
Enter file in which to save the key (/home/your_user/.ssh/id_rsa): 
```
Just press Enter to save the id_ras in the path. Then you will be prompted with:


```
Enter passphrase (empty for no passphrase):
```
Type Enter again if you don't want to type any password when ssh


```
Enter same passphrase again: 
```
Hit Enter again!
You should see:


```
Your identification has been saved in /home/your_user/.ssh/id_rsa.
Your public key has been saved in /home/you_user/.ssh/id_rsa.pub.
```
Now you can start saving passwords on you SSH:


```
 $ ssh-copy-id euid123@talon3.hpc.unt.edu
```
or if you have your shortcut 
```
$ ssh-copy-id t3
```
You will be prompted to enter password. It will logout, and you should see:


```
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 't3'"
and check to make sure that only the key(s) you wanted were added.
```

Congratiulations! Now everytime you need to login to Talon you just need to type **ssh t3** and your good to go!

## When you want to copy files using SCP:
Now since you setup your ssh shourtcut to be t3 and the password saved, when you use SCP it will be a lot easier!
Just type 


```
scp path/to/file/my_file t3:.
```
It will automatically enter the whole euid123@talon3.hpc.unt.edu and password for you!



















