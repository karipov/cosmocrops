import serial

SERIAL_DEVICE = '/dev/ttyACM0'
BAUD_RATE = 9600
NUM_TRIES = 3
NUM_LINES = 1

serial_device = serial.Serial(SERIAL_DEVICE, BAUD_RATE)

# helper functions
def mean(numbers: list) -> float:
    numbers = list(numbers)
    return sum(numbers) / len(numbers)

def get_line():
    line = ''
    while serial_device.inWaiting() > 0:
        line = serial_device.readline().decode().strip()

    return line

# data transofrmation functions
def process_line(line: str) -> dict:
    """
    Process a single line from the serial port
    """
    # split the line into a list of strings
    parts = line.strip().split(',')
    parts = [part.strip() for part in parts]

    # convert the strings to the correct data type
    data = {
        'water_level': round(float(parts[0]), 2),
        'moisture': round(float(parts[1]), 2),
        'temperature': round(float(parts[2]), 2),
        'light': round(float(parts[3]), 2),
    }

    return data

def process_lines(lines: list) -> dict:
    """
    Average the data from the lines from the serial port
    """
    # process each line
    dict_data = [process_line(line) for line in lines]

    # average the data
    averaged = {
        'water_level': mean(d['water_level'] for d in dict_data),
        'moisture': mean(d['moisture'] for d in dict_data),
        'temperature': mean(d['temperature'] for d in dict_data),
        'light': mean(d['light'] for d in dict_data),
    }

    return averaged
    
def get_lines():
    """
    Get the lines from the serial port (raw data)
    """
    # open the serial port
    output = []

    # read some lines of the serial output line
    for _ in range(NUM_TRIES):
        try:
            for _ in range(NUM_LINES):
                serial_device.reset_input_buffer()
                serial_device.reset_output_buffer()
                output.append(serial_device.readline().decode().strip())
        except UnicodeDecodeError:
            continue
        break

    return output


def get_data_from_arduino():
    """
    Get the data from the Arduino and process it
    """
    for _ in range(NUM_TRIES):
        try:
            line = get_line()
            data = process_line(line)
            return data
        except Exception:
            continue

    # default data
    return {
        'water_level': 0,
        'moisture': 0,
        'temperature': 0,
        'light': 0,
    }


