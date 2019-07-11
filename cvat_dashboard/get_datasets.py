import subprocess
import pandas as pd
from io import StringIO

output = subprocess.run('onepanel datasets list', shell=True, stdout=subprocess.PIPE,
                        universal_newlines=True)
data = output.stdout
data = data.split("  ")
text = []
for i in data:
    if i == '':
        continue
    else:
        text.append(i)
text = ";".join(text)
text = text.replace(";\n;", " \n ")

s = StringIO(text)
with open('fileName.csv', 'w') as f:
    for line in s:
        f.write(line)
df = pd.read_csv('fileName.csv', sep=';');
df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)

print(df.to_html())
