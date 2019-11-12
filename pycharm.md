## How to setup PyCharm for Talon

### Apply for professional account:
In order to register for a professional account use please go to: https://www.jetbrains.com/student/

Apply:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/apply_student_account.png)

### Download PyCharm Professional:
Go to: https://www.jetbrains.com/pycharm/ 

Press Download:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/website_download.png)


Choose Professional version [in this example I have use Linux. For Windows or Mac will be slightly different]:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/choose%20professional.png)

### Install PyCharm:
Follow normal installation instruction

### Fisrt time setup:

Skip Remaining and Set Defaults

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/skip_remaining_set_default.png)


Welcome to PyCharm

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/welcome_pycharm.png)


Go to Settings

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/welcome_settings.png)


Now click on Project Interpreter

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/setting_interpretter.png)


Click on right wheel

![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/settings_interpretter_add.png)



Add...
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/add_interpretter.png)


SSH Interpreter
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/ssh_interpretter.png)



New server configuration: enter Talon Vis node address: vis-01.acs.unt.edu
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/ssh_interpretter_username.png)



Asks for Connecting To Remote Host: Accept **[It might ask for your password instead]**
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/connection_remote_confirm_yes.png)


It mgiht also ask you to enter password of your JetBrain account.
You created this account earlier. 
[Make sure to enter password for that account]
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/login_unt_for_professional_verison.png)


Default remote interpreter:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/current_interpretter.png)

Brows to add a new interpreter:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/browse_interpretter.png)

Enter path of Talon Python interpreter:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/enter_path_interpretter.png)

Set path interpreter:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/set_path_interpretter.png.png)

Path Interpreter should look like this now:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/finish_adding_interpretter.png)

Project Interpreter should look like this now:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/inter-pretter_set.png)

Need to wait for a while to finish:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/wait_to_finish_setup.png)


## Test with creating a new project

Create New Project
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_create_new_project.png)


Select Pure Python
Choose preffered name of project. In this case is **test**
Now we need to set interpreter:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_new_test_file.png)


Click Project Interpreter > Existing Interpreter:
In **Remote project location** make sure add the path on Talon where you want your project to be!
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_path_to_remote_server.png)


Wait for some time:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_wait_before_workspace.png)


Workspace shold look like this:
If no folder is created wiht project name in Talon, PyCharm will create it for you.
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/.png)


Create Python file:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_create_python_file.png)

Name your python test file:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_create_file.png)


File uploaded to Talon when it's created:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_file_uploaded.png)


Write a print("Hello world!") in python file.
When save the file it will automatichally save it to Talon:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_hit_save_automatic_upload.png)


To run the Python file:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_run_python_file.png)


Python file will run on Talon and show results just like it's locally:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_python_file_is_running.png)


To see files on Talon in PyCharm click **Remote Host** on right side:
![alt text](https://raw.githubusercontent.com/gmihaila/unt_hpc/master/misc/pycharm_screenshot/test_sroll_through_your_path.png)


