class Ec2:
    def __init__(self,ami:str,instance_type:str,network:str,subnet:str,auto_assign_ip:bool,storage_size:int,volume_type:str,delete_on_termination:bool):
        self.ami = ami
        self.instance_type = instance_type
        self.network = network
        self.subnet= subnet
        self.auto_assign_ip = auto_assign_ip
        self.storage_size = storage_size
        self.volume_type = volume_type
        self.delete_on_termination = delete_on_termination
        def show_info(self):
            print(f' n An instance has been created with this configuration\n -AMI: {self.ami}\n -Instance Type: {self.instance_type}\n -Network: {self.network}\n -Subnet: {self.subnet}\n -Auto Assign Ip: {self.auto_assign_ip}\n -Storage Size: {self.storage_size}\n -Volume Type: {self.volume_type}\n -Delete On Termination: {self.delete_on_termination}\n')
        show_info(self)
   
ec2 = Ec2("linux", "t2.micro", "vpc-atlas", "SPB-1",True,30,"GPT2",True)