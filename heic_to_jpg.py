import os,subprocess,shutil

directory=os.getcwd()
os.mkdir('Output')

for filename in os.listdir(directory):
    if filename.endswith(".HEIC"):
        print('Converting %s' % os.path.join(directory, filename))
        subprocess.run(["magick", "%s" % filename, "%s" % (filename[0:-4] + 'jpg')])
        shutil.move(os.path.join(directory, filename[0:-4] + 'jpg'), os.path.join(directory, 'Output', filename[0:-4] + 'jpg'))
        continue