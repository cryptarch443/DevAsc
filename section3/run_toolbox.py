import toolbox

name = toolbox.generate_device_name('firewall','test')
print(name)

test1 = toolbox.is_ipv4_address('192.168.100.1')
test2 = toolbox.is_ipv4_address('255.255.255.0')
test3 = toolbox.is_ipv4_address('fd00:aa:bb::1')
print(test1, test2, test3)