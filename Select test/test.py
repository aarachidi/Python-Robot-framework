import os, glob
print(os.getcwd())
os.chdir('../')
path = os.getcwd()
files = glob.glob(path)
print(files)