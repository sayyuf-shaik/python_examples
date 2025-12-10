import serial

ports = serial.tools.ports.comports()


print(ports)


ser = serial.Serial(ports, baudrate, timeout)


ser.write("Hello device")

response = ser.readline().decode()
print(response)




