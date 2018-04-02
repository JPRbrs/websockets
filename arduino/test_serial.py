import serial

try:
    while True:
        ser = serial.Serial('/dev/ttyACM0', 9600)
        value_sent = raw_input('what to send?: ')
        write_serial = ser.write(value_sent.encode('utf-8'))
        print("bytes sent {}".format(write_serial))
        ser.close()
except KeyboardInterrupt:
    print("Exiting...")
