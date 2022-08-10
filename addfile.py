# Script step 2 Create a small executable with a command line interface (CLI). The purpose of the executable is to move a single file (located in the files folder) to the subfolder it belongs to by updating the recap

# I import the libraries we will need
import os
import shutil
import csv
import argparse

#define the file variable
file = ""
#create an object of type Argument parser
parser = argparse.ArgumentParser(description="Move a single file (located in the files folder) to the appropriate subfolder, updating the recap")
#add as a mandatory argument the name of the file to be moved (including format). In the event that the file passed as the argument does not exist in the folder, tell the user to choose from the choices
parser.add_argument("file", type=str, help="Enter the name of a file including extension among those in the files folder",choices = ["ciao.txt", "pippo.odt","bw.png","eclipse.png", "daffodil.jpg","trump.jpeg","song1.mp3", "song2.mp3"])
#make the proper assignment using the parse_args() method
args = parser.parse_args()

# First, I create the folders (if they do not already exist) into which the files will be moved.
for foldername in ["audio", "docs", "images"]:
    new_folder = os.path.join("", foldername)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

# I create the tuples containing the most common file formats for each type of file I'm going to analyse:

docs_extensions = (".txt", ".doc", ".docx", ".pages", ".odt", ".rtf", ".tex")
audio_extensions = (".mp3", ".mp4", ".m4a", ".wma", ".flac", ",aac")
images_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")

# I check if the recape file exists and create it if necessary
if not os.path.exists("recap.csv"):  # if it doesn't exist
    recap = open("recap.csv","w", newline="")# I create it
    writer = csv.writer(recap)
    writer.writerow(["name", "type", "size (B)"]) # I write csv header
else:  # if it already exists
    recap = open("recap.csv", "a", newline="") # I open it in 'append' with 'a'
    writer = csv.writer(recap)


file_name, file_extention = os.path.splitext(file) # I separate the file name from its extension
current_folder = "" + file  # specifies the file path
size = os.stat(current_folder).st_size  # calculates file size

# I use the 'endswith' method to take file formats and allocate them into the corresponding folders:
if file.endswith(docs_extensions):
    # this will be the folder into which the docs file will be moved
    final_folder = ("docs/" + file)
    # with shutil.move I move the file from the start folder to the destination folder
    shutil.move(current_folder, final_folder)
    writer.writerow([file_name, "doc", size])  # update recap
    # print the required file info (name, type and size in bytes) according to the desired output
    print("{} type:doc size:{}B".format(file_name, size))

elif file.endswith(audio_extensions):
    # this will be the folder into which the audio file will be moved
    final_folder = ("audio/" + file)
    # with shutil.move I move the file from the start folder to the destination folder
    shutil.move(current_folder, final_folder)
    writer.writerow([file_name, "audio", size])  # update recap
    # print the required file info (name, type and size in bytes) according to the desired output
    print("{} type:audio size:{}B".format(file_name, size))

elif file.endswith(images_extensions):
    # this will be the folder into which the image file will be moved
    final_folder = ("images/" + file)
    # with shutil.move I move the file from the start folder to the destination folder
    shutil.move(current_folder, final_folder)
    writer.writerow([file_name, "image", size])  # update recap
    # print the required file info (name, type and size in bytes) according to the desired output
    print("{} type:image size:{}B".format(file_name, size))

recap.close()  # I close the recap file at the end of compilation