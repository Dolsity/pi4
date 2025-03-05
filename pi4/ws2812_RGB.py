import time

from utils import log
from rpi_ws281x import PixelStrip, Color  # https://github.com/jgarff/rpi_ws281x


RGB_styles = [
    'breath',
    'static',
    'leap',
    'flow',
    'raise_up',
    'colorful',
    'colorful_static',
    'colorful_leap',
]

colorful_leds = [
    "#ff0000",
    "#e71164",
    "#ffa500",
    "#0000ff",
    "#ffC800",
    "#00ff00",
    "#0000ff",
    "#00ffb4",
    "#ff0000",
    "#00ff00",
    "#00ff00",
    "#8b00ff",
    "#8b00ff",
    "#8b00ff",
    "#0000ff",
    "#0000ff",
]


class WS2812():

    lights_order = [i for i in range(16)]

    def __init__(
        self,
        LED_COUNT,
        LED_PIN,
        LED_BRIGHTNESS,
        LED_FREQ_HZ=1000000,
        LED_DMA=10,
        LED_INVERT=False,
    ):
        self.led_count = LED_COUNT
        self.led_pin = LED_PIN
        self.led_brightness = int(LED_BRIGHTNESS * 225 / 100)
        self.led_freq_hz = LED_FREQ_HZ
        self.led_dma = LED_DMA
        self.led_invert = LED_INVERT
        self.strip = None
        self.init()

    def init(self):
        self.strip = PixelStrip(self.led_count, self.led_pin, self.led_freq_hz,
                                self.led_dma, self.led_invert, self.led_brightness)
        time.sleep(0.01)
        self.strip.begin()

    def reinit(self):
        if self.strip is None:
            self.init()

    # str or hex, eg: 'ee55ee', '#ee55ee', '#EE55EE'
    def hex_to_rgb(self, hex):
        try:
            hex = hex.strip().replace('#', '')
            return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
        except Exception as e:
            log('color parameter error: \n%s' % e)

    def clear(self, color: str = '#000000'):
        r, g, b = self.hex_to_rgb(color)
        self.reinit()
        self.strip.begin()
        for i in range(self.led_count):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()

    def display(self, style: str, color: str = '#ee55ee', speed=50):
        color = list(self.hex_to_rgb(color))
        self.clear()

        try:
            fuc = getattr(self, style)
            fuc(color, speed)
        except KeyError as e:
            log(f'LED strip parameter error: {e}')
        except Exception as e:
            log(f'LED display error: {e}')


    def breath(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        while True:
            self.reinit()
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            for i in range(100, 1, -1):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

    def static(self, color: list = [255, 255, 255], speed=50):
        while True:
            self.reinit()
            # No breath
            r, g, b =  color
            for index in self.lights_order:
                self.strip.setPixelColor(index, Color(r,g,b))
            self.strip.show()
            time.sleep(2)

    def leap(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            self.reinit()
            for i in range(self.led_count):
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(0, 0, 0))
                self.strip.setPixelColor(i, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

    def flow(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            self.reinit()
            for index in self.lights_order:
                self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            for j in range(self.led_count):
                self.strip.setPixelColor(j, Color(0, 0, 0))
            self.strip.show()
            time.sleep(0.005 * speed)

    def raise_up(self, color: list = [255, 255, 255], speed=50):
        speed = 101 - speed
        r, g, b = color
        while True:
            self.reinit()
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in range(0, 4, 1):
                    self.strip.setPixelColor(self.lights_order[index], Color(r, g, b))
                self.strip.show()
                time.sleep(0.0002 * speed)
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in range(4, 8, 1):
                    self.strip.setPixelColor(self.lights_order[index], Color(r, g, b))
                self.strip.show()
                time.sleep(0.0002 * speed)
            for i in range(2, 101):
                r, g, b = [int(x * i * 0.01) for x in color]
                for index in range(8, 16, 1):
                    self.strip.setPixelColor(self.lights_order[index], Color(r, g, b))
                self.strip.show()
                time.sleep(0.0002 * speed)
            # Turn off
            time.sleep(10 * 0.0005 * speed)
            for index in self.lights_order:
                self.strip.setPixelColor(self.lights_order[index], Color(0, 0, 0))
                self.strip.show()
                time.sleep(0.001 * speed)

    def colorful(self, color: list = None, speed=50):
        speed = 101 - speed
        _color = list(
            self.hex_to_rgb(colorful_leds[i]) for i in range(self.led_count))
        while True:
            self.reinit()
            for i in range(2, 101):
                for index in self.lights_order:
                    r, g, b = [int(x * i * 0.01) for x in _color[index]]
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)
            for i in range(100, 1, -1):
                for index in self.lights_order:
                    r, g, b = [int(x * i * 0.01) for x in _color[index]]
                    self.strip.setPixelColor(index, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

    def colorful_static(self, color: list = None, speed=50):
        _color = list(
            self.hex_to_rgb(colorful_leds[i]) for i in range(self.led_count))
        while True:
            self.reinit()
            # No breath
            for index in self.lights_order:
                r, g, b =  _color[index]
                self.strip.setPixelColor(index, Color(r, g, b))
            self.strip.show()
            time.sleep(2)

    def colorful_leap(self, color: list = None, speed=50):
        speed = 101 - speed
        while True:
            self.reinit()
            for i in range(self.led_count):
                r, g, b = self.hex_to_rgb(colorful_leds[i])
                for index in self.lights_order:
                    self.strip.setPixelColor(index, Color(0, 0, 0))
                self.strip.setPixelColor(i, Color(r, g, b))
                self.strip.show()
                time.sleep(0.001 * speed)

if __name__ == "__main__":
    speed = 80
    strip = WS2812(16, 10, 10)  # LED_COUNT, LED_PIN, LED_BRIGHTNESS

    strip.display('breath', 'ee00ee', speed=speed)
