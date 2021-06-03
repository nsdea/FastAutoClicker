import time
import mouse

globals()['clicks'] = 0

def clicked():
    globals()['clicks'] += 1

mouse.on_click(clicked)

while True:
    time.sleep(1)
    print(globals()['clicks'])
    globals()['clicks'] = 0