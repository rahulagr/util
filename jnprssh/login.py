import pexpect
import sys
import argparse
import os

"""
parser = argparse.ArgumentParser(description='Logs into a Jnpr device')
parser.add_argument('-u', action='store', dest='s_user', default='root', help='Username')
parser.add_argument('-p', action='store', dest='s_pass', default='Embe1mpls', help='Password')
parser.add_argument('-F', action='store', dest='ssh_options', default='contrail-config', help='SSH options')
parser.add_argument(action='store', dest='ip', help='device_name')
args = parser.parse_args()  
"""                  
verbose = 1


class JnprConn():
    """ Simple ssh login class """
    def __init__ (self):
        pass
    def login(self, s_user, s_pass, ssh_options, ip):
        try:
            try:
                homedir = os.path.expanduser('~') + '/.ssh/'
                ssh_options = homedir + ssh_options
                ssh_cmd="ssh -F %s %s@%s" %(ssh_options,s_user,ip)
                child = pexpect.spawn(ssh_cmd)
                if verbose:
                    child.logfile = sys.stdout
                child.timeout = 10
                child.expect('Password:')
            except pexpect.TIMEOUT:
                raise Exception("Couldn't log on to the switch")
            """ adding a comment """                               
            child.sendline(s_pass)
            child.expect('%')
            return child
        except (pexpect.EOF, pexpect.TIMEOUT), e:
            raise Exception("Error while trying to move the vlan on the switch.")   
    def logout(self, child):
            child.sendline('exit')
            