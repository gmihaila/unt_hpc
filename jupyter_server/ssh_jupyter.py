# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import pexpect
import sys
from io import StringIO
from multiprocessing import Process, Pipe
import os
import time
import datetime



# child = pexpect.spawn('./sshcode %s@%s --bind=0.0.0.0 --skipsync' % (euid, addrs), encoding='utf-8', timeout=timeout, logfile=None)
