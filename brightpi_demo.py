from brightpi import *

DELAY = 0.5

# ##################
def white_led_demo():
	led_on(LED_WHITE_1)
	time.sleep(DELAY)
	led_on(LED_WHITE_2)
	time.sleep(DELAY)
	led_on(LED_WHITE_3)
	time.sleep(DELAY)
	led_on(LED_WHITE_4)
	time.sleep(DELAY)

	led_on([LED_WHITE_1])
	time.sleep(DELAY)
	led_on([LED_WHITE_1, LED_WHITE_2])
	time.sleep(DELAY)
	led_on([LED_WHITE_1, LED_WHITE_2, LED_WHITE_3])
	time.sleep(DELAY)
	led_on([LED_WHITE_1, LED_WHITE_2, LED_WHITE_3, LED_WHITE_4])
	time.sleep(DELAY)

	led_off([LED_WHITE_1])
	time.sleep(DELAY)
	led_off([LED_WHITE_1, LED_WHITE_2])
	time.sleep(DELAY)
	led_off([LED_WHITE_1, LED_WHITE_2, LED_WHITE_3])
	time.sleep(DELAY)
	led_off([LED_WHITE_1, LED_WHITE_2, LED_WHITE_3, LED_WHITE_4])
	time.sleep(DELAY)

	led_on(LED_WHITE_ALL)
	time.sleep(DELAY)
	led_off(LED_WHITE_ALL	)
	time.sleep(DELAY)
	led_on(LED_WHITE_ALL)
	time.sleep(DELAY)
	led_off(LED_WHITE_ALL)
	time.sleep(DELAY)


def ir_led_demo():
	led_on(LED_IR_1)
	time.sleep(DELAY)
	led_on(LED_IR_2)
	time.sleep(DELAY)
	led_on(LED_IR_3)
	time.sleep(DELAY)
	led_on(LED_IR_4)
	time.sleep(DELAY)

	led_on([LED_IR_1])
	time.sleep(DELAY)
	led_on([LED_IR_1, LED_IR_2])
	time.sleep(DELAY)
	led_on([LED_IR_1, LED_IR_2, LED_IR_3])
	time.sleep(DELAY)
	led_on([LED_IR_1, LED_IR_2, LED_IR_3, LED_IR_4])
	time.sleep(DELAY)

	led_off([LED_IR_1])
	time.sleep(DELAY)
	led_off([LED_IR_1, LED_IR_2])
	time.sleep(DELAY)
	led_off([LED_IR_1, LED_IR_2, LED_IR_3])
	time.sleep(DELAY)
	led_off([LED_IR_1, LED_IR_2, LED_IR_3, LED_IR_4])
	time.sleep(DELAY)

	led_on(LED_IR_ALL)
	time.sleep(DELAY)
	led_off(LED_IR_ALL	)
	time.sleep(DELAY)
	led_on(LED_IR_ALL)
	time.sleep(DELAY)
	led_off(LED_IR_ALL)
	time.sleep(DELAY)

def white_led_brightness_demo():
	led_on(LED_WHITE_ALL)
	for i  in range(0, 64):
		set_brightness(LED_WHITE_1, i)
		set_brightness(LED_WHITE_2, i)
		set_brightness(LED_WHITE_3, i)
		set_brightness(LED_WHITE_4, i)
		time.sleep(DELAY/10)
	for i  in range(63, -1, -1):
		set_brightness([LED_WHITE_1, LED_WHITE_2, LED_WHITE_3, LED_WHITE_4], i)
		time.sleep(DELAY/10)
	led_off(LED_WHITE_ALL)

def ir_led_brightness_demo():
	led_on(LED_IR_ALL)
	for i  in range(0, 64):
		set_brightness(LED_IR_1, i)
		set_brightness(LED_IR_2, i)
		set_brightness(LED_IR_3, i)
		set_brightness(LED_IR_4, i)
		time.sleep(DELAY/10)
	for i  in range(63, -1, -1):
		set_brightness([LED_IR_1, LED_IR_2, LED_IR_3, LED_IR_4], i)
		time.sleep(DELAY/10)
	led_off(LED_IR_ALL)

def gain_demo():
	led_on(LED_WHITE_ALL)
	for i  in range(-20, 32):
		print(i)
		set_gain(i)
		print(get_gain())
		time.sleep(DELAY)

led_on(LED_ALL)
set_brightness(LED_ALL, 16)
set_gain(8)
white_led_demo()
ir_led_demo()
white_led_brightness_demo()
ir_led_brightness_demo()
led_off(LED_ALL)
