from paramiko import client

def func():
    ssh_client = client.SSHClient()
    policy = client.AutoAddPolicy
    ssh_client.set_missing_host_key_policy(policy())