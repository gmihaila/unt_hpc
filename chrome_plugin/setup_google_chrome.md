# UNT Talon from your Google Chrome browser

## Install SSH plug-in

This is a plugin made by Google itself (reliable and secure).
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_desc.png)

Make sure you have **Google Chrome** browser installed and opened.


Go to google extension page and search for Secure Shell [here](https://chrome.google.com/webstore/detail/secure-shell-app/pnhechapfaindjhompbnflcldabbghjo?hl=en) or just google *'chrome secure shell app*'

Click **Add to Chrome** to install this extension.

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_secure_shell.png)


You will see a pop-up window where you need to click **Add app**.

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/add_chrome_extension_window.png)



Once extension is installed you will see a new tab open with an **icon to the Secure Shell App**:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_icon.png)

## Start SSH-ing

There are 2 way (that I know of) to launch it:

* From the apps page: [chrome://apps/](chrome://apps/)

* Type ssh in the browser and hit **Tab** to select the  Secure Shell App.To launch it hit **Enter**.

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_url.png)



You should see a window like this:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh.png)

To ssh in Talon, type your **EUID@talon3.hpc.unt.edu** where it says *username@hostname or free from text* This will automatically fill in username and hostname fields.

Then enter 22 for the *port* field.

Then simply hit **Enter** or click **[ENTER] Connect**

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_enter_info.png)


Allow **Open ssh links**:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_allow.png)


You should see a window like this on your first login. Type *yes* and hit **Enter**:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_login.png)


Then you should be prompted to enter your Talon account password:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_login_yes.png)


### Cool! Now you can SSH to Talon from your Chrome browser! No software installation or terminal needed!

## To exit

Simply type *exit* and hit **Enter**. For this window type **E** to exit tab:

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_exit.png)




## By The Way....

If you have your SSH public key:

Use the** Import...** button to upload the id_rsa.pub file.

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/chrome_ssh_identity.png)

You ca copy the SHH public key somewhere to have easy access to it:

For example if you want to copy the SSH public Key to your Downloads folder [LINUX/MAC users]:

```
$ cp ~/.ssh/id_rsa.pub ~/Downloads/.
```

This way you can easily ssh without typing your password every time!

## Enjoy!
