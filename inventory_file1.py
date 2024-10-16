inventory = (
 """User_Network: 
     General_Settings: 
     Name: User_Network 
     RAM: 512 GB 
     vCPUs: 1 
     QEMU_binary: /usr/bin/qemu-system-x86_64(v4.2.1) 
     Boot_Priority: CD/DVD-ROM or HDD 
     On_close: Power off the VM 
     Console_type: telnet 
     Network_Settings: 
     Adapters: 13 
     Base_MAC: 0c:e0:f2:0b:00:00 
     Type: Realtek 8139 Ethernet (rtl8139) 
     Replicate_network_connection_states_in_QEMU: True
     -
 """
    
 """ACCT_Network: 
     General_Settings: 
     Name: ACCT_Network 
     RAM: 512 GB 
     vCPUs: 1 
     QEMU_binary: /usr/bin/qemu-system-x86_64(v4.2.1) 
     Boot_Priority: CD/DVD-ROM or HDD 
     On_close: Power off the VM 
     Console_type: telnet 
     Network_Settings: 
     Adapters: 13 
     Base_MAC: 0c:40:34:07:00:00 
     Type: Realtek 8139 Ethernet (rtl8139) 
     Replicate_network_connection_states_in_QEMU: True
     -
""" 
"""MGMT_Network: 
     General_Settings: 
     Name: MGMT_Network 
     RAM: 512 GB 
     vCPUs: 1 
     QEMU_binary: /usr/bin/qemu-system-x86_64(v4.2.1) 
     Boot_Priority: CD/DVD-ROM or HDD 
     On_close: Power off the VM 
     Console_type: telnet 
     Network_Settings: 
     Adapters: 13 
     Base_MAC: 0c:cc:78:5d:00:00 
     Type: Realtek 8139 Ethernet (rtl8139) 
     Replicate_network_connection_states_in_QEMU: True 
     -    
 """
    
"""IT_Network: 
     General_Settings: 
     Name: IT_Network 
     RAM: 512 GB 
     vCPUs: 1 
     QEMU_binary: /usr/bin/qemu-system-x86_64(v4.2.1) 
     Boot_Priority: CD/DVD-ROM or HDD 
     On_close: Power off the VM 
     Console_type: telnet 
     Network_Settings: 
     Adapters: 13 
     Base_MAC: 0c:1c:b2:85:00:00 
     Type: Realtek 8139 Ethernet (rtl8139) 
     Replicate_network_connection_states_in_QEMU: True 
     -
"""
    
"""Local_Switch: 
     General_Settings: 
     Name: Local_Switch 
     RAM: 512 GB 
     vCPUs: 1 
     QEMU_binary: /usr/bin/qemu-system-x86_64(v4.2.1) 
     Boot_Priority: CD/DVD-ROM or HDD 
     On_close: Power off the VM 
     Console_type: telnet 
     Network_Settings: 
     Adapters: 13 
     Base_MAC: 0c:c0:5e:66:00:00 
     Type: Realtek 8139 Ethernet (rtl8139) 
     Replicate_network_connection_states_in_QEMU: True """
)

print(inventory)
