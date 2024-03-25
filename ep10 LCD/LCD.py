import lcdlib
import time

lcd = lcdlib.lcd()
lcd.lcd_display_string("Hello World", 1)
time.sleep(1)
lcd.lcd_display_string("I love coding.",2)
time.sleep(2)
lcd.lcd_clear()
lcd.lcd_display_string("Bye...",1)
time.sleep(2)
