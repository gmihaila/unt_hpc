# Talon Jupyter Notebook on Google Chrome  (interactive session)

## Open new tab on Google Chrome browser

There are 2 way (that I know of) to launch it:

* From the apps page: chrome://apps/

* Type ssh in the browser and hit **Tab** to select the  Secure Shell App.To launch it hit **Enter**.

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_url.png)



You should see a window like this:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh.png)



To ssh in Talon Viz Node, type your ** YOUR_EUID@vis-01.acs.unt.edu ** where it says *username@hostname or free from text* This will automatically fill in username and hostname fields.

Then enter 22 for the *port* field.

Then simply hit **Enter** or click **[ENTER] Connect**

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/viz_node_login_chrome.png)


Allow **Open ssh links**:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_allow.png)


You should see a window like this on your first login. Type *yes* and hit **Enter**:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_login.png)


Then you should be prompted to enter your Talon account password:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_login_yes.png)



### Load any modules you plan to use in Jupyter Notebook

For example:



```
$ module load keras/2.2.0
```


### Launch Jupyter Notebook:

  Enter the following command in your terminal:

  ```
  $ jupyter notebook
  ```

  This will spawn a Jupyter Notebook terminal window that looks like this: ![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/screenshoot_jupyter.png)

  As long as you want to use Jupyter Notebook you need to keep this terminal open.

  ### If you close this terminal or tab you will lose your Jupyter Notebook session and any unsaved information!

  Keep track of the port that the notebook is running on. in the window you see



  ```
  $ REFRESH(1 sec): http://localhost:8891/tree
  ```

### 8891 is the port number in this case. In your case it can be a different number! That will be YOUR_PORT_NUMBER



## Forward Jupyter Notebook to your local machine

Open new tab in Google Chrome.

Open the ssh app.

This time when you login, you will use the port number in the SSh Arguments:



```
$ SSH Arguments: -L 8891:localhost:8891
```

So your window should look like this:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/viz_node_chrome_forward.png)


### Now you should have 2 tabs open with terminals. First one was used to launch Jupyter Notebook and get the port number. Second is used to forward the port number so you can see it on your local machine.

### Access your Jupyter Notebook:

   Now to access the Jupyter Notebook, open any browser (Chrome,Mozilla etc) and type:

   ```
   http://localhost:YOUR_PORT_NUMBER
   ```

   In my case, my port number is 8891 so I will have to use:

   ```
   http://localhost:8891
   ```
   You will see a webpage like this:

   ![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/screenshot_loginwindow_jupyter.png)

   This is where you will enter your password that you created when you used

   ```
   $ jupyter notebook password
   ```

   Now you are inside your Jupyer Notebook on your local machine browser that runs on Talon! Cool!

   This is how mine looks like after login:

   ![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/screenshot_logged_jupyter.png)

   I only have bin folder in this image. Yours will be different, you will see all your directories from Talon.

</br>

### [< Jupyter Tutorial](https://github.com/gmihaila/unt_hpc/tree/master/jupyter_notebook)

### [< Main Page](https://github.com/gmihaila/unt_hpc)






