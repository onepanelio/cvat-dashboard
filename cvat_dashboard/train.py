import sys,os
def process(dataset,pushd):
    #print(' onepanel jobs create "python cat_dog.py '+dataset+' /onepanel/input && pip install onepanel==2.13.2b0 && cd /onepanel/output && onepanel datasets init -n '+pushd+'  && onepanel push" --machine-type gpu-8-52-1v100 --environment jupyter-py3-tensorflow1.11.0 --storage default-storage-10 ')
    os.system(' onepanel jobs create "python /onepanel/code/nodered/model.py '+dataset+' /onepanel/input && pip install onepanel==2.13.2b0 && cd /onepanel/cnn && onepanel datasets init -n '+pushd+'  && onepanel push -y" --machine-type gpu-8-52-1v100 --environment jupyter-py3-tensorflow1.11.0 --storage default-storage-10 ')

if __name__ == "__main__":
    print(sys.argv)
    var=sys.argv[1].split(' ')
    #process(var[0],var[1])
    process('onepanel-demo/datasets/cat-dog','tets')
