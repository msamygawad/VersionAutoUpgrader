import os
import sys
import glob
import shutil
import time

def check_server_and_run_last():
    
    # Define the name of the project file
    running_version = os.path.basename(__file__)

    server_files = glob.glob(".\..\Server\Proj_Version*.py")
    server_files.sort()
    if not server_files:
        print("No files found in the Server directory.")
        return None
    latest_version = os.path.basename(server_files[-1])

    if latest_version != running_version:
        shutil.copy2(server_files[-1], os.getcwd())        
        print("Moving control to the latest version")
        path = os.path.join(os.getcwd(),latest_version)
        path_arg = ["python",path]
        os.execvp("python",path_arg)
        sys.exit()
    
    preLast_version = ""
    local_files =  glob.glob("Proj_Version*.py")
    if len(local_files) > 1:
        local_files.sort()
        preLast_version = local_files[0]
    return preLast_version


def check_local_for_old_versions(older_file_name):
    if os.path.exists(older_file_name):
        print("")
        print("Found this old version --> (" + os.path.basename(older_file_name) + ") in the local folder" )
        os.remove(older_file_name)
        print("This old version --> (" + os.path.basename(older_file_name) + ") was deleted successfully" )
    else :
        print("You are running the latest version")
       
def main():
    older_file_name = check_server_and_run_last() 
    time.sleep(1)
    check_local_for_old_versions(older_file_name)
   
    #your main program here >>
    print("running the main program")
    print(f"Current running file: {os.path.basename(__file__)}")
    
    file_name = os.path.basename(__file__)
    file_name = file_name.replace("Proj_Version","")
    file_name = file_name.replace(".py","")
    #convert file name to int
    file_version = int(file_name)
    
    #count from 1 to file_version
    for i in range(1,file_version+1):
        print(i)
        time.sleep(1)
    print(f"End of the program {os.path.basename(__file__)}")

    #end of the program
    
    input("Program finished execution, Press any key to exit...")

if __name__ == "__main__":
    main()