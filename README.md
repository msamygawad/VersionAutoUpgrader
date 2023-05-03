# VersionAutoUpgrader

Proceduers to try

1- Open CMD in local folder

2- run the only py file exist

  3- if it is not the latest one compared to the files in Server folder, it will be removed and latest file exist in server will be copied to local folder and run 
	
  4- if it is the latest version, then it will run noramlly
  
Note that: the programs are samples and the main function of them is to count from 1 to the version name

ToDo:

1- add safety mechanism to avoid erros if there is another files than Proj_Version*.py files

2- add safety mechanism to avoid erros incase versions are named by floating numbers

3- add method in the versioning upgrade function to autmatically follow the same file nameing protocol (ie: "Prject ver2" or "product_V2" ...etc).

4- add mechanism to detect that local folder have newer version than the server. it will automatically add that newer version to the server and delet any older version in the local folder

5- convert files to be .exe extension to enhance file integrity for windows platforms


