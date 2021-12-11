import RPi.GPIO as GPIO
import time

MOTOR_PIN = 18
MOISTURE_SENSOR_PIN = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)
GPIO.setup(MOTOR_PIN, GPIO.OUT, initial=GPIO.LOW)


def get_moisture_value():
    return GPIO.input(MOISTURE_SENSOR_PIN)


def start_water_motor():
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    print(f'Started Motor - {GPIO.input(MOTOR_PIN)}')
    return GPIO.input(MOTOR_PIN)


def stop_water_motor():
    GPIO.output(MOTOR_PIN, GPIO.LOW)
    print(f'Stopped Motor - {GPIO.input(MOTOR_PIN)}')
    return GPIO.input(MOTOR_PIN)


def water_plant():
    counter = 0

    start_water_motor()

    while counter < 100 and not get_moisture_value():
        counter += 1
        time.sleep(.25)
        if get_moisture_value():
            break

    stop_water_motor()

def cleanup():
    GPIO.cleanup()