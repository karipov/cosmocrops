import serial

SERIAL_DEVICE = '/dev/ttyACM0'
BAUD_RATE = 9600

# helper functions
def mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def mode(data: list):
    return max(set(data), key=data.count)


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
        'water_level': float(parts[0]),
        'moisture': float(parts[1]),
        'temperature': float(parts[2]),
        'light': float(parts[3]),
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
    ser = serial.Serial(SERIAL_DEVICE, BAUD_RATE)
    output = []

    # read some lines of the serial output line
    for _ in range(10):
        output.append(ser.readline().decode().strip())

    # close the serial port
    ser.close()

    return output


def get_data():
    """
    Get the data from the Arduino and process it
    """
    lines = get_lines()
    data = process_lines(lines)
    return data


