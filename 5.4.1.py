from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.101',  #Your Server IP
    'username': 'sara', #your Server Username
    'password': '#Sara8979', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('apt-get update')
print(output)
