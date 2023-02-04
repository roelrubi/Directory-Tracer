import os
import tkinter
import tkinter.filedialog as _filedialog

root = tkinter.Tk()
root.withdraw()

rootdir = _filedialog.askdirectory(title='Please select a directory')

path, title = os.path.split(rootdir)

directoryPrior = ''

output = open(f"{title + '_Folder Structure'}.txt", 'w+')
output.write(title + " Directories \n")

for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        filename, file_ext = os.path.splitext(os.path.join(subdir, file))

        directory = os.path.dirname(filename + file_ext)
        directory = directory.replace(path + '/', '')
        directory = directory.replace("\\", ' >> ')

        if directory != directoryPrior:
            output.write(directory + "\n")

        directoryPrior = directory

        try:
            output.write(filename + file_ext + "\n")
        except:
            pass

output.close()