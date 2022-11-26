def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if rgb[0] in range(0,256) and rgb[1] in range(0,256) and rgb[2] in range(0,256):
        a = "#"
        for color in rgb:
            #print(color)
            if len(hex(color)) == 3:
                a += "0"+str(hex(color).replace("0x", ""))
            else:
                a += str(hex(color).replace("0x", ""))
        return a.upper()
    else:
        raise ValueError
    pass
