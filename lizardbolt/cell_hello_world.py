"""Tests communication with the SIM800C USB to GSM Module."""
# TODO ChatGPT wrote much of this--rewrite when we have a better understanding of the protocol
# TODO unit tests, pylint, Black, docstrings
# TODO rename this module as like "stat" or something and have that as one of three basic command line tools: stat, text, call

import serial
import time

SERIAL_PORT = "/dev/ttyUSB3"
BAUD_RATE = 115200
TIMEOUT = 1


def send_command(ser, command, wait_time=1):
    ser.write((command + '\r\n').encode())
    time.sleep(wait_time)
    while ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(response)


def main():
    try:
        # Open serial port
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")

        # Test AT command communication
        print("Sending AT command to test communication...")
        send_command(ser, 'AT')  # Basic AT command to check communication

        # Check GSM network registration
        print("Checking network registration...")
        send_command(ser, 'AT+CREG?')

        # Check signal quality
        print("Checking signal quality...")
        send_command(ser, 'AT+CSQ')

        # Optional: send an SMS (uncomment and modify phone number and message)
        # print("Sending an SMS...")
        # phone_number = "+1234567890"
        # message = "Hello from Raspberry Pi!"
        # send_command(ser, f'AT+CMGF=1')  # Set SMS text mode
        # send_command(ser, f'AT+CMGS="{phone_number}"')
        # send_command(ser, message + chr(26))  # Ctrl+Z to send the message

        # Close the serial port
        ser.close()
        print("Serial port closed.")

    except serial.SerialException as e:
        print(f"Error opening or using the serial port: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
