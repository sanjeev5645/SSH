 
from ssh_connect_handler import SSHConnectHandler
 
def execute_commands():
    ssh_connect_handler = None
    ssh_connect_handler = SSHConnectHandler(ip='192.168.0.200',
                                                    username='san',
                                                    password='san',
                                                    device_type='ARISTA_EOS'
                                                    )
    command_output_dict = {}
    #workload = {'switch':'show system','routes':'show ip routes','showSwitchPorts':'show interfaces','showRouterInterfaces':'show ip interface','vrfs':'show vrf'}
    workload = {'switch':'show ip int brief','vrf':'show vrf','routes':'show ip route'}
    vrf_list = ['AMMU1','ANKU']
    for COMMAND_KEY in workload:
        if (COMMAND_KEY == 'routes'):
            command_result = ''
            command_result = ssh_connect_handler.execute_command(workload[COMMAND_KEY])
            for item in vrf_list:
                command_result = command_result + ssh_connect_handler.execute_command(workload[COMMAND_KEY]+' '+'vrf'+' '+item)
            command_output_dict[workload[COMMAND_KEY]] = command_result
        else:
            command_result = ssh_connect_handler.execute_command(workload[COMMAND_KEY])
            command_output_dict[workload[COMMAND_KEY]] = command_result




    ssh_connect_handler.close_connection()
    print(command_output_dict['show ip route'])

if __name__ == "__main__":
    execute_commands()