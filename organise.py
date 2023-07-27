import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/Nikita/OneDrive/Desktop/from dir"
to_dir = "C:/Users/Nikita/OneDrive/Desktop/to dir"

list_of_files = os.listdir(from_dir)
print(list_of_files)

