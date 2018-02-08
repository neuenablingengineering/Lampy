from display_message import LCDDisplay
import time

lcd = LCDDisplay()

#write message to screen with default offset
lcd.write_msg_to_screen("Hello")
time.sleep(5)

#write message with offset
lcd.write_msg_to_screen("hello", 6)
time.sleep(5)

#write two line message
lcd.write_two_line_msg("line 1", "line 2")
time.sleep(5)

#clear only second line
lcd.clear_second_line()
time.sleep(5)

#write to second line
lcd.write_to_second_line("second line")
time.sleep(5)

#write to second line with offset
lcd.write_to_second_line("hello", 5)
time.sleep(5)

#clear only first line
lcd.clear_first_line()
time.sleep(5)

#write time
lcd.write_time_to_screen()


