import os

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"): 
        print(os.path.join(directory, filename))
        continue