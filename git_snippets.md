# Git Tutorial 


### Checkout if you have git:
```
$ git --version
```

### Staging

* **Add 1 file:**
  ```
  $ git add file
  ```
  
* **Add multiple files:**
  ```
  $ git add file1 file 2
  ```

* **Add all the files inside your project folder:**
  ```
  $ git add .
  ```


### Commit the file/files:
  ```
  $ git commit -m "your message"
  ```


### Find out information regarding what files are modified and what files are in the staging area:
  ```
  $ git status
  ```
  
### Print out all the commits which have been done up until now:
  ```
  $ git log
  ```


### Create a new branch called testing:
  ```
  $ git branch testing
  ```

### Switch to an existing branch:
  ```
  $ git checkout testing
  ```
  
### List out all the branches in local using the following command:
  ```
  $ git branch
  ```
  
### See all branches local and remote:
```
$ git branch -a
```

### To merge branches:

* **First go back to the master branch:**
  ```
  $ git checkout master
  ```
  
* **Then run the merge command:**
  ```
  $ git merge test
  ```
  
### Delete branch on remote server:
```
$ git push origin --delete test
```

### Delete test branch from local:
```
$ git branch -d test
```


### Clone to your location:
```
$ git clone [repository url]
```

### Make sure your folder project is updated:
```
$ git pull origin master
```
  
### Solve *Peer's Certificate has expired.* error:
```
$ git config --global http.sslVerify false
```



