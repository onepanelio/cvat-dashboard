import subprocess
import sys

data = sys.argv[1]
output = subprocess.run('cd ../input && mkdir '+data+' && cd '+data+' && onepanel download onepanel-demo/datasets/' + data, shell=True,
                        stdout=subprocess.PIPE,
                        universal_newlines=True)
print(output)
