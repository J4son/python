import usb
#dev = usb.core.find(find_all=True)
dev = usb.core.find()
dev.set_configuration()
