# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import pexpect
import sys
from io import StringIO
from multiprocessing import Process, Pipe
import os
import time
import datetime


def check_pid(user, file):
    """ Check For the existence of a unix pid. """
    ## file format user\t...\tpid
    if not os.path.exists(file):
        return False
    lines = open(file, "r").read().splitlines()
    lines = [line for line in lines if line.split("\t")[1] == user]
    if len(lines) == 0:
        return False
    else:
        pid = lines[-1].split("\t")[-1]
        try:
            os.kill(int(pid), 0)
        except OSError:
            return False
        else:
            return lines[-1]


def ssh_code(conn, euid, pass_, addrs, timeout=300):
    user_status = check_pid(user=euid,
                            file="tmp_database")

    if user_status:
        ## user laready logged in, can close connection
        _, _, ide_password, ide_port, ssh_pid = user_status.split("\t")
        line = "success %s %s %s %s" % (euid, ide_password, ide_port, ssh_pid)
        conn.send(line)
        conn.close()
        print("User already logged in: ",user_status)
        return
    else:
        print("User not logged in. Trying to connect...")


    ssh_pid = os.getpid()

    print('process id:', ssh_pid)
    child = pexpect.spawn('./sshcode %s@%s --bind=0.0.0.0 --skipsync' % (euid, addrs), encoding='utf-8', timeout=timeout, logfile=None)
    # child.expect(['password: '])
    # child.sendline(pass_)

    ide_password = None
    ide_port = None
    failed_connections = 0

    while True:
        try:
            child.expect('\n')
            out_line = child.before
            # print("out_line: ", out_line)
            if "Tunneling remote port" in out_line:
                ide_port = out_line.split()[-1].split(":")[1]
                print("Port: ", ide_port)

            if "Password is" in out_line:
                ide_password = out_line.split()[-1][:-4]
                print("Password: ",ide_password)

            if "failed to start SSH master connection" in out_line:
                failed_connections += 1
                print("failed_connections: ", failed_connections)

                if failed_connections == 3:
                    ## after 3 failed connections
                    conn.send("error ")
                    conn.close()
                    ## failed to connect
                    print("FAILED TO CONNECT")
                    child.close(force=True)
                    return

            if ide_password and ide_port:
                time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                line = "success %s %s %s %s" % (euid, ide_password, ide_port, ssh_pid)
                conn.send(line)
                conn.close()
                ## add to database
                with open("tmp_database", "a") as f:
                    line = "%s\t%s\t%s\t%s\t%s\n" % (time_stamp, euid, ide_password, ide_port, ssh_pid)
                    f.write(line)
                break
            # print("line_output: ",out_line)
        except pexpect.EOF:
            break
    child.expect(pexpect.EOF)
    child.close(force=True)
    return


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        use = request.form['username']
        pas = request.form['password']

        # creating a pipe
        parent_conn, child_conn = Pipe()

        p = Process(target=ssh_code, args=(parent_conn, use, pas, "talon3.hpc.unt.edu"))
        p.start()

        # print(u,p)
        msg = child_conn.recv()
        status = msg.split(" ")[0]
        if status == 'error':
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            euid, ide_password, ide_port, pid = msg.split(" ")[1:]
            ide_link = "http://0.0.0.0:%s" %(ide_port)
            return render_template('login.html', ide_link=ide_link, ide_password=ide_password)
    return render_template('login.html', login='login')



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
