import time
import usb.core
import usb.util
# use lsusb
VID = 0x80ee
PID = 0x0021


dev = usb.core.find(idVender=VID, idProduct=PID)
if not dev:
    print("could not found")
    exit(1)
print("Yeeha!!!! found it!!")
exit(0)
