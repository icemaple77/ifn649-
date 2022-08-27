import serial

ser = serial.Serial("/dev/rfcomm2", 9600)
# Alarm.write(bytes("1", 'utf-8'))
# Alarm.write(bytes("1", 'utf-8'))
# Alarm.write(bytes("3", 'utf-8'))
result = ser.write(bytes("11111222233", 'utf-8'))
print(result)
