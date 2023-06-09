# Write a Python program that you create a directory and then a single file in that directory
import os
os.mkdir('python')
with open('python/myfile.txt','w') as f:
    f.write('this is my file')

# Write a Python program that lists all files in a directory.
import glob
path =r"\Users\kwaku.opare\Desktop\New folder (3)"
files = glob.glob(path +"/*")
for file in files:
    print(file)






# Write a Python program that lists all directories in a directory.
import os
directory =r"\Users\kwaku.opare\Desktop\New folder (3)" 
for list in os.scandir(directory):
    if list.is_dir():
        print(list.name)



# Write a Python program that lists all files and directories in a directory.
import os
path = '.'
directory_files = os.listdir(path)
for item in  directory_files:
    print(item)


# Write a Python program that checks if a file exists in a directory.
import os
path = '\\Users\\kwaku.opare\\Desktop\\New folder (3)'
file = 'do.py'
filepath = f'{path}\\{file}' # using f-string
filepath = path + '\\' + file # using string concatenation
filepath = os.path.join(path, file) # using a function which joins paths
file_exist = os.path.exists(filepath)
print(file_exist)




# Write a Python program that checks if a directory exists.
import os
directory = '\Users\kwaku.opare\Desktop\New folder (3)'
if os.path.isdir(directory):
    print('directory exist')
else:
    print('directory does not exist')    


# Write a Python program that calculates the size of a file in bytes.
import os
print('enter the name of file')
filename = 'learner.py'
sizeoffile= os.path.getsize(filename)
print('\nsize of given file(in bytes) is')
print(sizeoffile)

# Write a Python program that calculates the size of a file in kilobytes.
import os
print('enter the name of file')
filename = 'do.py'
size_in_bytes= os.path.getsize(filename)
size_in_kilobytes = size_in_bytes / 1024
print(f'the size of {filename}is {size_in_kilobytes:.2f}kb')



    
# Write a Python program that calculates the size of a file in megabytes.
import os
file_name = "quizzes.py"
size_of_file = os.path.getsize(file_name)
size_in_megabytes = size_of_file / (1024*1024)
print(f'size of {file_name} is {size_in_megabytes:.2f}MB')






# Write a Python program that calculates the size of all files in a directory and prints the total size in bytes.
import os
total_size = 0
start_path = '\Users\kw\Users\kwaku.opare\Desktop\New folder (3)'
for filename in os.listdir(start_path):
    file_path = os.path.join(start_path,filename)
    if os.path.isfile(file_path):
        total_size += os.path.getsize(file_path)
print(f'the total size of all files in {start_path} is {total_size}bytes')        
    

    
     

# Write a Python program that calculates the size of all files in a directory and prints the total size in kilobytes.
import os
directory_path = "\Users\kwaku.opare\Desktop\New folder (3)"
total_size_bytes= directory_path
total_size_kilobytes= total_size_bytes / 1024
print(f"the total size of all files in a {directory_path} is{total_size_kilobytes:2f} KB. ")

# Write a Python program that calculates the size of all files in a directory and prints the total size in megabytes.
import os
directory_files = "\Users\kwaku.opare\Desktop\New folder (3)"
total_size_bytes= 0
total_size_in_megabytes= total_size_bytes/ 1024
print(f"the total size of all files in as {directory_files}is{total_size_in_megabytes:.2f}MB.")


# Write a Python program that calculates the size of all files with a certain extension in a directory and prints the total size in bytes.
import os
directory_path= "\Users\kwaku.opare\Desktop\New folder (3)"
extension = '.py'
total_size_bytes= "get_file_size_with_extension(directory_path,extension)"

# Write a Python program that calculates the size of all files with a certain extension in a directory and prints the total size in kilobytes.
# Write a Python program that calculates the size of all files with a certain extension in a directory and prints the total size in megabytes.