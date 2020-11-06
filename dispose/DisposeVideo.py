import os


def get_file_name(file_dir):
    fileList = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            fileList.append(file)
    return fileList


if __name__ == '__main__':
    rootPath = '/Users/amethyst/Downloads/auth_video/'

    targetPath = '/Users/amethyst/Downloads/optimize_video/'

    fileList = get_file_name(rootPath)

    for file in fileList:
        originalFile = rootPath + file
        disposedFile = targetPath + file
        command = 'ffmpeg -i ' + originalFile + ' -c copy -movflags +faststart ' + disposedFile
        os.system(command)

    exit()
