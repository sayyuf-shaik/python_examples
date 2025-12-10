import re
import subprocess


_proc = subprocess.Popen("ipconfig", stdout=subprocess.PIPE, stdin=subprocess.PIPE)

output, err = _proc.communicate()

print(output.decode(), err)
# get the adapters first

adapters = re.findall(r"^([^\n].*):$", output.decode())
print(adapters)