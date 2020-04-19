import sys
import signal

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
