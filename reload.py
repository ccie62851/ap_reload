from netmiko import ConnectHandler

def resetAP(host, userName, passWord):
	verification_cmd = "show ap summary"
	net_connect = ConnectHandler(device_type="cisco_ios",ip=host,username=userName,password=passWord)
	print("Connected to",host)
	output = net_connect.send_command(verification_cmd)
	stripped_op = []
	stripped_op.append(output.split("\n")[9:])
	ap_list = []
	for ap in stripped_op[0]:
		try:
			ap_list.append(ap.split()[0])
		except:
			pass
	for ap in ap_list:
		reset_command = "config AP reset {} \n".format(ap)
		commands = net_connect.send_command_timing(reset_command, strip_command=False, strip_prompt=False)
		if "Would" in commands:
			commands += net_connect.send_command_timing("y\n", strip_command=False, strip_prompt=False)
			print("Reseting " + ap)

host = "10.1.1.1"
userName = "admin"
passWord = "password"

resetAP(host, userName, passWord)
