import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
# portvar = ""
for onePort in ports:
    portsList.append(str(onePort))
    print (str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portvar = "COM" + str(val)
        print (portvar)

serialInst.baudrate = 9600
serialInst.port = portvar
serialInst.open()

while True:
    cmd = input("ON/OFF")
    serialInst.write(cmd.encode('utf-8'))