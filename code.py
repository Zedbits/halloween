import board
import neopixel
import time
import random


BRIGHTNESS = 1.0
num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)


"""
Function: sparkle
Description: a chosen foreground color flashes randomly on a chosen background color.
Parameters: color1(tuple) - color1 is background, color2(tuple)is foreground. delay(floating
point) - time between flashes. loop (int) is the time the light flashes
Return: none
"""
def sparkle(color1, color2, loop = 10, delay=0.1):
  for outer in range(loop):
    np.fill(color1)
    for i in range(np.n / 4):
      np[random.randint(0, np.n-1)] = color2
    np.show()
    time.sleep(delay)

'''
Function: chase
Description: The foreground color chases other instances of the foreground color on a
backdrop of
the background color
Parameters: color1(tuple) is background, color2(tuple) is foreground. loop(int) is how much
the color moves around. count(int) is the space between chasing pixels. delay(floating
point)
is the time it takes to move color
Return value: none
'''
def chase(color1, color2, loop=10, delay=0.1):
  result = 0
  for outer in range(loop):
    np.fill(color1)
    for i in range(np.n):
      if i % 3 == result:
        np[i] = color2
    np.show()
    time.sleep(delay)
    result = (result + 1) % 3

'''
Function: fade_in
Description: This function fades a color in from black.
Parameters: color(tuple) - the color that is being faded in, delay(floating point)
is the time it takes to start fading in
Return value: none
'''
def fade_in(color, delay=0.01):
    pix = color
    start = (0, 0, 0)
    mx = max(pix[0], max(pix[1], pix[2]))
    r_inc = pix[0]/mx
    g_inc = pix[1]/mx
    b_inc = pix[2]/mx
    r, g, b = start
    while r < pix[0] and g < pix[1] and b < pix[2]:
        r += r_inc
        g += g_inc
        b += b_inc
        np.fill((int(r), int(g), int(b)))
        print('r - {}, g - {}, b - {}'.format(int(r), int(g), int(b)))
        np.show()
        time.sleep(delay)

'''
Function: fade_out
Description: This function fades a color to black
Parameters: color(tuple) - the starting color that is being faded to black,
delay(floating point)
is the time needed to fade out
Return value: none
'''
def fade_out(color, delay=0.01):
    end = (0, 0, 0)
    pix = color
    mx = max(color[0], max(color[1], color[2]))
    r_inc = pix[0] / mx
    g_inc = pix[1] / mx
    b_inc = pix[2] / mx
    r, g, b = pix
    while r >= end[0] and g >= end[1] and b >= end[2]:
        r -= r_inc
        g -= g_inc
        b -= b_inc
        np.fill((int(r), int(g), int(b)))
        print('r - {}, g - {}, b - {}'.format(int(r), int(g), int(b)))
        np.show()
        time.sleep(delay)

'''
Function: Fire
Description: Creates a flame effect on a strip of neopixels
Parameters: background(tuple): base color for flame, foreground(tuple): color used to flash
return value: none
'''
def fire(background, foreground):
    why = random.random()/5
    for j in range(20):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(why)

'''
Function: lightning
Description: Creates a lightning effect
Parameters: background(tuple): base color for the lightning, foreground(tuple): color used
to flash
return value: none
'''
def light(background, foreground):
    why = random.random()/20
    for j in range(20):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(why)


while True:
    # fades into orange
    fade_in((179, 98, 1))
    # lightning effect with orange background and green lightning
    for i in range(3):
        fire((179, 98, 1), (179, 98, 1))
        light((1, 255, 1), (1, 255, 1))
        fire((179, 98, 1), (179, 98, 1))
    # fades out from orange
    fade_out((179, 98, 1))
    # fades into purple
    fade_in((144, 46, 187))
    # chase
    chase((144, 46, 187), (1, 1, 1), 50, .07)
    # fades out
    fade_out((144, 46, 187))
    # fades into red
    fade_in((255, 1, 1))
    # sparkles purple on a red background
    sparkle((255, 1, 1), (98, 1, 179), 50)
    # fades out
    fade_out((176, 1, 90))
    # pulses red color
    for i in range(5):
        fade_in((120, 1, 1), .001)
        fade_out((120, 1, 1), .001)
