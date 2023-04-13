import json, time, os, random, uuid
import video_files
from ui_interaction import *
from toaster import *
from hashtag import *

def upload_videos(driver, CHANNEL_ID, limit = 99999999, source_folder = './'):
    videos = video_files.get_shuffled_files(source_folder, 'mp4')[0:limit]

    for (video_file, metadata_file) in videos:
        # Carrega os metadados do vídeo
        # a partir do arquivo .json
        with open(metadata_file, 'r') as f:
            metadata = json.loads(f.read())
        
        print('Fazendo o upload do vídeo: ' + metadata['title'])
        toaster.show_toast('Novo vídeo', 'Fazendo o upload do vídeo: ' + metadata['title'])

        open_yt_upload_dialog(driver, CHANNEL_ID)
        select_video_file(driver, video_file)

        type_video_title(driver, remove_hashtags(metadata['title']))
        
        type_video_description(driver, get_hashtags(metadata['title'], join_text=' '))

        check_as_not_for_children_audience(driver)
        click_show_more(driver)
        
        # Escreve todas as tags
        type_tags(driver, metadata['tags'] if 'tags' in metadata.keys() else [])
        click_next_button_3_times(driver)

        time.sleep(1)
        check_as_public(driver)

        time.sleep(1)
        click_done_button(driver)

        # Exclui os arquivos do vídeo
        print(f'Excluindo {video_file}\nExcluindo {metadata_file}')
        os.remove(video_file)
        os.remove(metadata_file)

        # Espera um tempo
        time_to_wait = random.randint(20, 60)
        print(f'Esperando {time_to_wait} segundos')
        time.sleep(time_to_wait)


        

