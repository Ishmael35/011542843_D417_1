import paramiko

def ssh_to_switch(host, user, password=""):

	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		client.connect(hostname=host, username=user, password=password)
		stdin, stdout, stderr = client.exec_command('create vlan data_100')
		stdin, stdout, stderr = client.exec_command('configure vlan data_100 tag 100')

		output = stdout.read().decode()
		error = stderr.read().decode()

		if output: 
			print(f"Command Output:\n", output)
		if error:
			print(f"Error Output:\n", error)

	except paramiko.SSHException as e:
		print(f"SSH connection failed: {e}")
	finally:
		client.close()

if __name__ == "__main__":
    	switches = [
        	{"host": "10.10.1.5", "user": "admin"}, 
        	{"host": "10.10.1.6", "user": "admin"},
        	{"host": "10.10.1.7", "user": "admin"}, 
        	{"host": "10.10.1.8", "user": "admin"},

    ]

    	for switch in switches:
        	ssh_to_switch(switch["host"], switch["user"])
