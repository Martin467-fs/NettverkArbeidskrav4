import serial
import time

def serial_connect_router(port, baudrate, username, password):
    try:
        # Establish a serial connection
        print(f"Connecting to the router via serial port {port}...")
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Wait for the connection to stabilize
        
        # Example configuration commands
        commands = [
            "enable\n",  # Enter enable mode
            "configure terminal\n",  # Enter global config mode
            f"hostname {hostname}\n",  # Set hostname
            "ip domain name cisco\n", # Set ip domain name
            "crypto key generate rsa general-keys modulus 1024\n", # Generate ssh keys
            f"enable password {password}\n", #set the enable password
            f"username {username} password {password}\n", # Create a user and password
            "ip ssh version 2\n", # Specify which version of ssh to use
            "line vty 0 4\n", # Set amount of ssh sessions
            "transport input ssh\n", # Set that only ssh connections are allowed
            "login local\n", # Tell the device to authenticate using local login credentials
            "exit\n", # Exit config-line
            f"interface {interface}\n", # enter the interface to set an IP address
            f"ip address {ipaddress} {subnetmask}\n", # Set the IP address and subnetmask
			"no shutdown\n",
            "exit\n" # Exit interface configuration
            
        ]
        if AskDevice == "switch":
            commands.append(f"interface {SwitchInterface}\n")
            commands.append(f"switchport mode {Switchportmode}\n")
            commands.append(f"switchport access vlan {VLANID}\n")
        elif AskDevice == "ruter" or AskDevice == "router":
            commands.append(f"ip route {StatiskRoutingDestinasjon} {StatiskRoutingDestinasjonSubnetMaske} {StatiskRoutingNextHop}\n")
        commands.append("exit\n")  # Exit config mode
        commands.append("exit\n")  # Exit session
        for command in commands:
            ser.write(command.encode())
            time.sleep(1)  # Allow time for the command to process
        
        print("Configuration applied to the router.")
        
        # Close the connection
        ser.close()
        print(f"Connection to the router on {port} closed.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input variables
    serial_port = input("Enter the serial port (e.g., COM3 or /dev/ttyUSB0): ")
    baud_rate = int(input("Enter the baud rate (e.g., 9600 or 115200): "))
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    interface = input("Enter the interface name: ")
    hostname = input("Enter the hostname: ")
    ipaddress = input("Enter the IP address for the interface: ")
    subnetmask = input("Enter the subnet mask for the IP: ")
    AskDevice = input("What type of device are you configuring? ")
    AskDevice = AskDevice.lower()
    if AskDevice == "switch":
        SwitchInterface = input("Enter a switchport for VLAN: ")
        VLANID = input("Enter a VLAN ID: ")
        Switchportmode = input("Enter the mode for the Switchport: ")
    elif AskDevice == "ruter" or AskDevice == "router":
        StatiskRoutingDestinasjon = input("Enter the IP of where you are routing to: ")
        StatiskRoutingDestinasjonSubnetMaske = input("Enter the subnetmask of where you routing to: ")
        StatiskRoutingNextHop = input("Enter the IP address of the next hop you are going to: ")
    # Connect to the router
    serial_connect_router(serial_port, baud_rate, username, password)
