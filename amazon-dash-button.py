#!/usr/bin/python

from scapy.all import *

TIME_MARGIN = os.getenv('TIME_MARGIN', 5)

if len(sys.argv) < 3:
    print('Usage: %s BUTTON_IP COMMAND [ARGS...]' % sys.argv[0])
    exit(1)

BUTTON_IP = sys.argv[1]
COMMAND   = sys.argv[2:]

last = datetime.min

def prn(x):
    global last

    now   = datetime.utcnow()
    delta = now - last

    if delta.total_seconds() > TIME_MARGIN:
        last = now
        subprocess.Popen(COMMAND)

sniff(prn=prn, filter='src host %s' % BUTTON_IP, store=0)
