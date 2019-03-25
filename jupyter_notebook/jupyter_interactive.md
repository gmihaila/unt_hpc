## Run on an interactive node


### Login to a Viz Node. Use ONE of the following:

```
$ ssh YOUR_EUID@vis-01.acs.unt.edu
```

```
$ ssh YOUR_EUID@vis-02.acs.unt.edu
```

```
$ ssh YOUR_EUID@vis-03.acs.unt.edu
```

### Load the appropriate module:

  ```
  $ module load python/3.6.5
  ```


### Launch Jupyter Notebook:

  Enter the following command in your terminal:

  ```
  $ jupyter notebook
  ```

  This will spawn a Jupyter Notebook terminal window that looks like this:

  ![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/screenshoot_jupyter.png)

  As long as you want to use Jupyter Notebook you need to keep this terminal open.

  ### If you close this terminal you will lose your Jupyter Notebook session and any unsaved information!

  Keep track of the port that the notebook is running on. in the window you see



  ```
  $ REFRESH(1 sec): http://localhost:8891/tree
  ```

### 8891 is the port number in this case. In your case it can be a different number! That will be YOUR_PORT_NUMBER



  ### Forward Jupyter Notebook to your local machine browser

  Now you need to open a new terminal window and use the following command:

  ```
  $ ssh -L YOUR_PORT_NUMBER:localhost:YOUR_PORT_NUMBER YOUR_EUDI@vis-01.acs.unt.edu
  ```

  In this example the port number is 8891, so I will use:

  ```
  ssh -L 8891:localhost:8891 EUID@vis-01.acs.unt.edu
  ```

  You will replace this number with the one generated in your Jupyter Notebook terminal window.

  This will forward the port of the Jupyter Notebook running on talon to your local machine.


### Double check...

  Now you should have 2 terminals running:

  * One terminal with the Jupyter Notebook terminal window like in **1.3. Launch Jupyter Notebook**
    ![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/screenshoot_jupyter.png)

  * Another terminal that you used to login with like in **1.4 Forward Jupyter Notebook to your local machine browser**:

  ```
  $ ssh -L YOUR_PORT_NUMBER:localhost:YOUR_PORT_NUMBER YOUR_EUDI@vis-01.acs.unt.edu
  ```

  These 2 terminal are the ones keeping your Jupyter Notebook alive and running on your local machine!


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

### [< Jupyter Tutorial](https://github.com/gmihaila/unt_hpc)

### [< Main Page](https://github.com/gmihaila/unt_hpc)
