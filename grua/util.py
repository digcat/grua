
import subprocess, re, os



def announce(msg, ignore_quiet=False):
    global G
    if G.get('modeNoisy') == 'noisy' or ignore_quiet:
        print "\n>>> " + msg + "\n"

def mention(msg, ignore_quiet=False):
    global G
    if G.get('modeNoisy') == 'noisy' or ignore_quiet:
        print ">> " + msg

def note(msg, ignore_quiet=False):
    global G
    if G.get('modeNoisy') == 'noisy' or ignore_quiet:
        print "> " + msg

def find_bridge_ip():
    command = ["ip", "addr", "show", "dev", "docker0"]
    sp = subprocess.Popen((command), stdout=subprocess.PIPE)

    output = subprocess.check_output(('grep', 'inet'), stdin=sp.stdout).strip().split()[1].split('/')[0]

    sp.wait()

    # ensure we have a valid ip
    p = re.compile(
        '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
    if not p.match(output):
        raise Exception(output + " is not a valid IP address for BridgeIP")

    return output


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
