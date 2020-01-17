from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os, json, shutil, time

class FSHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder):
            new_dir = new_folders[ self.find_folder(file) ]
            if file not in restricted:
                rename = self.rename_handler(file, new_dir)
                self.move_to_folder(file, new_dir, rename)
    def find_folder(self, file):
        arr = file.split('.')
        file_extension = arr[-1]
        index = 0
        for i in range(len(extensions)) :
            if file_extension in extensions[i]:
                break
            index += 1
        return index
    def move_to_folder(self, file, destination, name='what'):
        src = folder + '/' + file
        rename = destination + '/' + name
        os.rename(src, rename)
    def rename_handler(self, name, dest):
        rename = name
        i = 1
        is_duplicate = os.path.isfile(dest + '/' + rename)
        temp = rename
        while(is_duplicate):
            i += 1
            arr = rename.split('.')
            try:
                temp = arr[0] + str(i) + arr[1]
            except IndexError:
                temp = rename + str(i)
            is_duplicate = os.path.isfile(dest + '/' + temp)
        rename = temp
        return rename    


folder = '/Users/kent/Downloads'
new_folders = ['/Users/kent/Downloads/Media', '/Users/kent/Downloads/Slides', '/Users/kent/Downloads/PDFs Texts', 
                 '/Users/kent/Downloads/Programming','/Users/kent/Downloads/Misc']
restricted = ['Media', 'Slides', 'PDFs Texts', 'Programming','Misc']
Media = ['jpg', 'png', 'mp3', 'mp4']
Slides = ['pptx']
Texts = ['pdf', 'txt', 'doc', 'docx']
Programming = ['c', 'h', 'ml', 'py', 'java', 'class', 'cpp', 'hpp', 'sh']
extensions = [Media, Slides, Texts, Programming]

file_system_handler = FSHandler()
observer = Observer()
observer.schedule(file_system_handler, folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()