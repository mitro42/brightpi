from smbus import SMBus
import time

bus = SMBus(1)

LED_WHITE_1 = 0x02
LED_WHITE_2 = 0x08
LED_WHITE_3 = 0x10
LED_WHITE_4 = 0x40
LED_WHITE_ALL = [LED_WHITE_1, LED_WHITE_2, LED_WHITE_3, LED_WHITE_4]

LED_IR_1 = 0x04
LED_IR_2 = 0x01
LED_IR_3 = 0x80
LED_IR_4 = 0x20
LED_IR_ALL = [LED_IR_1, LED_IR_2, LED_IR_3, LED_IR_4]
LED_ALL = LED_WHITE_ALL + LED_IR_ALL

_ADDRESS = 0x70
_COMMAND_GETSET_LED = 0x00
_COMMAND_GETSET_GAIN = 0x09

_BRIGHTNESS_COMMANDS = {
	LED_WHITE_1: 0x02,
	LED_WHITE_2: 0x04,
	LED_WHITE_3: 0x05,
	LED_WHITE_4: 0x07,
	LED_IR_1: 0x01,
	LED_IR_2: 0x03,
	LED_IR_3: 0x06,
	LED_IR_4: 0x08
}

def _get_led_bits(leds):
	if isinstance(leds, list):
		bits = 0x0
		for l in leds:
			bits |= l
		return bits
	else:
		return leds

def led_on(leds):
	bus.write_byte_data(_ADDRESS,  _COMMAND_GETSET_LED,  _get_led_bits(leds))

def led_off(leds):
	currentBits = bus.read_byte_data(_ADDRESS, _COMMAND_GETSET_LED)
	offBits = _get_led_bits(leds)
	currentBits &= ~offBits
	bus.write_byte_data(_ADDRESS, _COMMAND_GETSET_LED,  currentBits)


def set_gain(value):
	value  = max(0, min(value, 15))
	bus.write_byte_data(_ADDRESS, _COMMAND_GETSET_GAIN, value)

def get_gain()	:
	return bus.read_byte_data(_ADDRESS, _COMMAND_GETSET_GAIN)

def set_brightness(leds, brightness):
	brightness  = max(0, min(brightness, 63))
	if isinstance(leds, list):
		for l in leds:
			bus.write_byte_data(_ADDRESS, _BRIGHTNESS_COMMANDS[l], brightness)
	else:
			bus.write_byte_data(_ADDRESS, _BRIGHTNESS_COMMANDS[leds], brightness)

def get_brightness(leds):
	if isinstance(leds, list):
		return [bus.read_byte_data(_ADDRESS, _BRIGHTNESS_COMMANDS[l]) for l in leds]
	else:
			return bus.read_byte_data(_ADDRESS, _BRIGHTNESS_COMMANDS[leds])
	return None

