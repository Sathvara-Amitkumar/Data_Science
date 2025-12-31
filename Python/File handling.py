from pathlib import Path

def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}", end="\n")
        
        
def createFile():
    try:
        readfileandfolder()
        fname = input("\nEnter file name to create: ")
        p = Path(fname)
        
        if not p.exists() and p.is_file():
            with open(p, "w") as f:
                data = input("Enter data to write in file: ")
                f.write(data)

            print((f"FILE {fname} CREATED SUCCESSFULLY"))
        else:
            print(f"File {fname} already exists!")
    
    except Exception as err:
        print(f"An error occured as {err}")

def readFile():
    try:
        readfileandfolder()
        fname = input("\nEnter file name to read: ")
        p = Path(fname)
        
        if p.exists() and p.is_file():
            with open(p, "r") as f:
                data = f.read()
                print(f"Data in file {fname} : \n{data}")

        else:
            print(f"File {fname} does not exist!")
    
    except Exception as err:
        print(f"An error occured as {err}")


def updateFile():
    readfileandfolder()
    fname = input("\nEnter file name to update: ")
    p = Path(fname)
    
    if p.exists() and p.is_file():
        print("\nPress 1 to append data")
        print("Press 2 to overwrite data")
        print("Press 3 to Change file name")
        print("Press 4 to exit")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            with open(p, "a") as f:
                data = input("Enter data to append in file: ")
                f.write(data)
            print(f"Data appended successfully to file {fname}")
        
        elif choice == 2:
            with open(p, "w") as f:
                data = input("Enter data to overwrite in file: ")
                f.write(data)
            print(f"Data overwritten successfully to file {fname}")
        
        elif choice == 3:
            new_name = input(("enter new file name : "))
            p.rename(new_name)
            print(f"File {fname} renamed successfully to {new_name}")
        
        elif choice == 4:
            pass
        
        else:
            print("Invalid choice!")
    
    else:
        print(f"File {fname} does not exist!")


def deleteFile():
    readfileandfolder()
    fname = input(("\nEnter file name to delete: "))
    p = Path(fname)
    
    if p.exists() and p.is_file():
        p.unlink()
        print(f"File {fname} deleted successfully")
    
    else:
        print(f"File {fname} does not exist!")
            
            
print("\nPress 1 to create a new file")
print("Press 2 to reading a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    createFile()
elif choice == 2:
    readFile()
elif choice == 3:
    updateFile()
elif choice == 4:
    deleteFile()
else:
    print("Invalid choice")