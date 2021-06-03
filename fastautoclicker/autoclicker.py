'''The main autoclicker program

IMPORTANT: Windows capped the CPS for me to 63-66, just so you know.
Also, most of the games, like Minecraft 1.8.9+ have cooldowns or something
like that, so you may mess around with the parameters a bit and do some
testing before actually using it.
'''


import time
import mouse
import random
import keyboard 

class Clicker:
    def __init__(self, key='tab', mode: bool=True, button: str='left', cps: int=10, optimize_cps=True, randomize=0):
        '''
        key (str): key to enable/disable the autoclicker, examples: 'tab' or 'space' or 'x' or 'shift' or 'ctrl'
        mode (bool): True: press <key> to activate, press again to deactivate. False: Autoclick only when <key> is pressed. 
        button (str): 'left' or 'right' mouse button, example: 'left' - can also be a key, like 'a' or 'space'.
        cps (int): the approx. amount of **clicks done per second** - higher values may not work as high as expected, example: 10 - Set CPS to 0 to make it hold <button>
        optimize_cps (bool): if CPS optimization should be used to get more accurate/higher CPS - this should be used on lower CPS values
        randomize (int): How much the CPS should be randomized.
        '''

        self.key = key
        self.mode = mode
        self.button = button
        self.randomize = randomize

        if optimize_cps:
            if cps > 85:
                cps *= 6
            elif cps > 50:
                cps *= 4
            elif cps > 30:
                cps *= 2
            elif cps > 15:
                cps *= 1.5
            elif cps > 5:
                cps *= 1.25
            elif cps > 1:
                cps *= 1.1
            else:
                cps = 0

        self.cps = cps

        self.cooldown = True
        if cps >= 999: # remove cooldown completely if clicks per seconds are over 999
            self.cooldown = False

        globals()['ac_active'] = False

    def toggle(self, event):
        '''Toggles the AutoClicker status'''

        if globals()['ac_active']:
            globals()['ac_active'] = False
        else:
            globals()['ac_active'] = True

    def hold(self, event):
        '''Keeps clicking the key pressed until <self.key> is released'''

        time.sleep(0.05)

        globals()['ac_active'] = True

        while keyboard.is_pressed(self.key):
            pass

        globals()['ac_active'] = False

    def run(self):
        '''Clicks if <globals()['ac_active']> is True'''

        while True:
            if globals()['ac_active']:
                if self.cps == 0:
                    keyboard.press(self.button)
                else:   
                    mouse.click(button=self.button)
                    if self.cooldown:
                        actual_cps = self.cps
                        actual_cps =  actual_cps + random.randint((self.randomize//2)*-1, (self.randomize//2))

                        print(actual_cps)

                        time.sleep(1/actual_cps)
            elif (not globals()['ac_active']) and self.cps == 0:
                keyboard.release(self.button)

    def start(self):
        '''Starts the Auto Clicker events, is being used in the actual code'''

        time.sleep(0.1)

        if self.mode:
            keyboard.on_press_key(self.key, self.toggle)
        else:
            keyboard.on_press_key(self.key, self.hold)

        self.run()

if __name__ == '__main__':
    c = Clicker(key='tab', mode=True, button='left', cps=100, optimize_cps=True, randomize=0)
    c.start()