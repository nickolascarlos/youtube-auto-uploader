import random, os

def get_files(folder, video_format):
    files = [f"{folder}\\{file}" for file in os.listdir(folder)]
    videos = [file for file in files if file.split('.')[-1] == video_format]
    metadata_files = [file for file in files if file.split('.')[-1] == 'json']
    return list(zip(videos, metadata_files))

def get_shuffled_files(folder, video_format):
    files = get_files(folder, video_format)
    random.shuffle(files)

    return files