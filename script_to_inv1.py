import configparser

config = configparser.ConfigParser()

networks= {
	'User_Network':{ 
		'Name':'User_Network',
		'RAM': '512 MB',
		'vCPUs': '1',
		'Qemu binary': '/usr/bin/qemu-system-x86_64(v4.2.1)',
		'Boot priority': 'CD/DVD-ROM or HDD',
		'On close': 'Power off the VM',
		'Console type': 'telnet',
		'Adapters': '13',
		'Base MAC': '0c:e0:f2:0b:00:00',
		'Type': 'Realtek 8139 Ethernet (rtl8139)',
		'Replicate network connection states in Qemu': 'check'
	},
	'ACCT_Network':{ 
                'Name':'User_Network',
                'RAM': '512 MB',
                'vCPUs': '1',
                'Qemu binary': '/usr/bin/qemu-system-x86_64(v4.2.1)',
                'Boot priority': 'CD/DVD-ROM or HDD',
                'On close': 'Power off the VM',
                'Console type': 'telnet',
                'Adapters': '13',
                'Base MAC': '0c:40:34:07:00:00',
                'Type': 'Realtek 8139 Ethernet (rtl8139)',
                'Replicate network connection states in Qemu': 'Yes'
                        },
	'MGMT_Network':{ 
                'Name':'User_Network',
                'RAM': '512 MB',
                'vCPUs': '1',
                'Qemu binary': '/usr/bin/qemu-system-x86_64(v4.2.1)',
                'Boot priority': 'CD/DVD-ROM or HDD',
                'On close': 'Power off the VM',
                'Console type': 'telnet',
                'Adapters': '13',
                'Base MAC': '0c:cc:78:5d:00:00',
                'Type': 'Realtek 8139 Ethernet (rtl8139)',
                'Replicate network connection states in Qemu': 'Yes'
                        },
	'IT_Network':{ 
                'Name':'User_Network',
                'RAM': '512 MB',
                'vCPUs': '1',
                'Qemu binary': '/usr/bin/qemu-system-x86_64(v4.2.1)',
                'Boot priority': 'CD/DVD-ROM or HDD',
                'On close': 'Power off the VM',
                'Console type': 'telnet',
                'Adapters': '13',
                'Base MAC': '0c:1c:b2:85:00:00',
                'Type': 'Realtek 8139 Ethernet (rtl8139)',
                'Replicate network connection states in Qemu': 'Yes'
                        }
	}
for network, switch in networks.items():
	config[network] = switch

with open('inventory_step_b.ini', 'w') as configfile:
	config.write(configfile)









