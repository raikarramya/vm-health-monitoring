import subprocess

def recover_service(service_name):
    command = ["powershell","-ExecutionPolicy","Bypass",
               f"Restart-Service -Name {service_name}"]
    subprocess.run(command)
