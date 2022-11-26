import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        try:
            self.rgb = COLOR_NAMES[self.color.upper()]
        except:
            self.rgb = None

    def hex2rgb(hex_value):
        hex_rgb = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9":9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
        i = 0
        rgb_value = []
        if len(hex_value) != 7 or hex_value[0] != "#":
            raise ValueError("Not proper Hex!")
        for v in hex_value[1:]:
            if v not in hex_rgb:
                raise ValueError("Not proper Hex!")
            if i % 2 == 0:
                rgb = 0
                rgb = int(hex_rgb[v]) * 16
            else:
                rgb = rgb + int(hex_rgb[v])
                rgb_value.append(rgb)
            i += 1
        """Class method that converts a hex value into an rgb one"""
        return tuple(rgb_value)

    def rgb2hex(rgb_value):
        rgb_hex = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        """Class method that converts an rgb value into a hex one"""
        hex_value = "#"
        if len(rgb_value) != 3:
            raise ValueError("Need R, G and B values!")
        for v in rgb_value:
            if v not in range(0, 256):
                raise ValueError("Not in range 0-255")
            d = v//16
            if v % 16 == 0:
                m = 0
            else:
                m = (v/16) % 1
            if d > 9:
                hex_value = hex_value + str(rgb_hex[d])
            else:
                hex_value = hex_value + str(d)
            if m * 16 > 9:
                hex_value = hex_value + str(rgb_hex[m * 16])
            else:
                hex_value = hex_value + str(int(m * 16))
        return hex_value


    def __repr__(self):
        """Returns the repl of the object"""
        rep = "Color('" + self.color + "')"
        return rep

    def __str__(self):
        """Returns the string value of the color object"""
        try:
            self.rgb = COLOR_NAMES[self.color.upper()]
        except:
            self.rgb = "Unknown"
        return str(self.rgb)
