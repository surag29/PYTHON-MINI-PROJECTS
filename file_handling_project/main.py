from pathlib import Path


def readfileandfolder():
    path = Path("")
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
     print(f"{i+1} : {items}")





def createfile():
   try:
    readfileandfolder()
    name =  input("please enter the file name :")
    p = Path(name)
    if not p.exists():
        with open(p,"w") as fs:
         data =  input("what you want to write in this file")
         fs.write(data)
         print("file created successfully")
    else:
       print("this file already exists")
   except Exception as err:
         print(f"error occured at : {err}")
   
      

print("1 for creating a file ")
print("2 for reading a file ")
print("3 for updating a file ")
print("4 for deleting  a file ")
check =  int(input("enter your response: "))
if check ==1:
    createfile()