from pathlib import Path
import os 


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

def readfile():
    try:
     readfileandfolder()
     name =  input("please enter the file name :")
     p = Path(name)
     if  p.exists() and p.is_file():
        with open(p,"r") as fs:
         data =  fs.read()
         print(data)
         print("file is read successfully")
     else:
       print("this file does not  exists")
    except Exception as err:
         print(f"error occured at : {err}")

def updatefile():
    try: 
        readfileandfolder()
        name  = input("enter the name of the file you want to update")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing your file name :")
            print("press 2 for overwriting  your file name :")
            print("press 3 for appending content to your  file name :")

            res = int(input("enter your response :  "))
            if res ==1:
                name2 = input("enter the new name of the file: ")
                p2 = Path(name2)
                p.rename(p2)
                print("the file is renamed")

            if res ==2:
                with open(p,"w") as fs:
                    content = input("enter the new content: ")
                    fs.write(content)
                    print("the file is overwritten successfully ")

            if res ==3:
                with open(p,"a") as fs:
                    appcontent = input("enter the content to be appended :")
                    fs.write(" " +appcontent)
                    print("the data is appended successfully")
    except Exception as err:
       print(f" an error as : {err}")


def deletefile():
   try:
    readfileandfolder()
    name = input("enter the name of the file you want to delete")
    p = Path(name)
    if p.exists and p.is_file():
        os.remove(p)
        print("the file is deleted successfully")
    else:
        print("no such file exists")
    
   except Exception as err:
      print(f"error occurred as {err}")   
   
      

print("1 for creating a file ")
print("2 for reading a file ")
print("3 for updating a file ")
print("4 for deleting  a file ")
check =  int(input("enter your response: "))

if check ==1:
    createfile()

if check ==2:
    readfile()

if check ==3:
   updatefile()
   
if check ==4:
   deletefile()