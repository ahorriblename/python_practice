def rgb_to_hex(r, g, b):
    # Pre-cond: ints are >= 0 and <= 255
    if (
        r > 255 or r < 0
    ) or (
        g > 255 or g < 0
    ) or (
        b > 255 or b < 0
    ):
        return ""
    
    return "{:02x}{:02x}{:02x}".format(r,g,b)

print(rgb_to_hex(145,0,255))
