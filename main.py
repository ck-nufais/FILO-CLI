import argparse
from filo import Filo
import pathlib
import json

##Type Checks

#function for Path type checking
def Pathcheck(msg,x):
    x = pathlib.Path(x)
    if not x.exists():
        print(msg)
        raise SystemExit(1)
    else:
        return x

def Filecheck(x):
    x = pathlib.Path(x)
    if not x.is_file() or not x.exists():
        print("The file path not found or is invalid file")
        raise SystemExit(1)
    return x

#base bone 
parser = argparse.ArgumentParser(description="CLI tool for organizing files",prog="FILO-CLI")
parser.add_argument("src" ,help="Source Path which needs to be Organized",type=lambda x:Pathcheck("Incorrect Source Path",x))
parser.add_argument("dest",help="Destination Path for Organized files",type=lambda x:Pathcheck("Incorrect Destination Path",x))
parser.add_argument("-l","--list",help="Pass the file that containes mapped folders with extensions",default=None,type=Filecheck)
args = parser.parse_args()
src = args.src
dest = args.dest
ext = args.list
decode = None
if ext != None:
    with ext.open("r") as file:
        try:
            decode = json.load(file)
        except json.decoder.JSONDecodeError:
            print("The Passed File is not correctly formatted for python dictionary or json\nfor more info refers to github")
            raise SystemExit(1)
print(decode)

