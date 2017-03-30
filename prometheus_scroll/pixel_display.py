import scrollphat
import time

class output_display:
    def __init__(self):
        MID_LEVEL = 10
        scrollphat.clear()
        scrollphat.update()
        scrollphat.set_brightness(MID_LEVEL)

        self.last = 0
        self.HEIGHT = 5
        self.WIDTH = 11
        self.MAX = (self.WIDTH) * (self.HEIGHT)

    def flash(self,val):
        scrollphat.clear()
        self.slow_fill(val,0.01)

    def slow_fill(self, val, pause):
        y = 0
        x = 0
        while(val > 0):
            scrollphat.set_pixel(x, y, True)
            time.sleep(pause)
            scrollphat.update()
            x = x + 1
            if(x == 10):
                y = y + 1
                x = 0
            val = val -1

    def display(self, amt):
        val = 0
        if(amt != None):
            val = int(amt)
            if(val > self.MAX):
                val = self.MAX
                self.flash(val)
                return

        if(val == self.last):
            return

        if(self.last > val):
            scrollphat.clear()

        self.last = val

        y = 0
        x = 0
        while(val > 0):
            scrollphat.set_pixel(x, y, True)
            scrollphat.update()
            x = x + 1
            if(x == 10):
                y = y + 1
                x = 0
            val = val -1
