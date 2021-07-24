from device import Device

dev1 = Device('dev1')
dev2 = Device('dev2')
dev2.motd = 'Welcome!'
print(dev1.show())
print(dev2.show())
print(dev2.show('motd'))
print(dev2.show('interface'))
