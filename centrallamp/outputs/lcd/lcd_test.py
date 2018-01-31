from display_message import LCDDisplay
import time

lcd = LCDDisplay()

lcd.com.CURSOR_BLINK_OFF(lcd.ser);

#write message to screen with default offset
lcd.write_msg_to_screen("Hello")
time.sleep(5)

#write message with offset
lcd.write_msg_to_screen("hello", 6)
time.sleep(5)

#write two line message
lcd.write_two_line_msg("First Line", "Second Line")
time.sleep(5)

#write to second line
lcd.write_msg_to_second_line("New message")
time.sleep(5)

#clear only first line
lcd.com.CLEAR_FIRST_LINE(lcd.ser)
time.sleep(5)

#write to second line with offset
lcd.write_msg_to_second_line("Hej", 7)
time.sleep(5)

#write to first line with offset
lcd.write_msg_to_first_line("Hello", 3)
time.sleep(5)

#clear only second line
lcd.com.CLEAR_SECOND_LINE(lcd.ser)
time.sleep(5)

#write time to screen
lcd.write_time_to_screen()



