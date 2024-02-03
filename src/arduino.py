import serial

def get_lines():
    # Open the serial port
    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with the appropriate port
    output = []

    # Read 10 lines of the serial output line
    for _ in range(10):
        output.append(ser.readline().decode().strip())

    # Close the serial port
    ser.close()

    return output


