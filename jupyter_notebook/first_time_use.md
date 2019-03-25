## First time ONLY Setup:

### When you use Jupyter Notebook execute this step to setup password for your Jupyter Notebook

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


  Type this in your terminal:

  ```
  $ jupyter notebook password
  ```

  Then enter a password. This will be the password necessary to access Jupyter Notebook. THIS IS NOT YOUR EUID PASSWORD.

  You will have to type twice, for:

  ```
  $ Enter password:
  ```
  And

  ```
  $ Verify password:
  ```

  After you entered the password twice you should see a message:

  ```
  [NotebookPasswordApp] Wrote hashed password to /home/YOUR_EUID/.jupyter/jupyter_notebook_config.json
  ```

  This creates a configuration file jupyter_notebook_config.json related to your password.
  
  
  </br>

### [< Jupyter Tutorial](https://github.com/gmihaila/unt_hpc)

### [< Main Page](https://github.com/gmihaila/unt_hpc)
