import re
import subprocess
import sys

_proc = subprocess.Popen('ipconfig', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = _proc.communicate()

if _proc.returncode !=0:
    print('Something is Wrong')
    sys.exit(1)
print(stdout.decode())
pattern = "[a-zA-Z0-9-. ]+:[a-z0-9%]{0,4}?:[a-z0-9%]{0,4}?:[a-z0-9%]{0,4}?:[a-z0-9%]{0,4}?:[a-z0-9%]{0,4}?:[a-z0-9%]{0,7}?"

matches = re.findall(pattern, stdout.decode())

print(matches)