from test_class import generate_device_name, Router, Interface

dev_name = generate_device_name("router", "test_env")
router1 = Router(dev_name)
router1.interface = Interface("eth0", "1.1.1.1")
print(router1.show())