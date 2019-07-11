import sys, os, subprocess
import glob


def find_latest():
    list_of_files = glob.glob('/onepanel/output/cvat/data/*/*.xml')
    print
    latest_file = max(list_of_files, key=os.path.getctime)
    flags = latest_file.split('/')
    print(flags)
    task = flags[-2]
    name = flags[-1].split('.')[0] + '-dump'
    return task, name.lower()


def process():
    dataset, pushd = find_latest()
    dev_null = open(os.devnull, 'w')
    print(subprocess.check_output(
        'cd /onepanel/output/cvat/data/' + dataset + ' && onepanel datasets init -n ' + pushd + ' && onepanel push -y',
        shell=True))


process()
