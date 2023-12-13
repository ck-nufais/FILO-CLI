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
# file check
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
parser.add_argument("-i","--ignore",help="give ignore files list \n['main.py']",default=[],type=str,nargs="*")

args = parser.parse_args()

src = args.src.resolve()
dest = args.dest.resolve()
ext = args.list
ignore = args.ignore
decode = {}

#check if list argument are none
if ext != None:
    with ext.open("r") as file:
        try:
            decode = json.load(file)
        except json.decoder.JSONDecodeError:
            print("The Passed File is not correctly formatted for python dictionary or json\nfor More info refers to github")
            raise SystemExit(1)
    organise = Filo(src,dest,data=decode,ignore=ignore)
    organise.OrganiseDir()
else:
    organise = Filo(src,dest,ignore=ignore)
    organise.OrganiseDir()
# print(json.loads(ignore))

