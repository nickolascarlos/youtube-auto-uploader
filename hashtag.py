import re

HASHTAG_REGEX = '\ ?(\#[A-zÀ-ú0-9]+)\ ?'

def remove_hashtags(text):
    text = re.sub('-\ *#', '#', text)
    return re.sub(HASHTAG_REGEX, '', text)

def get_hashtags(text, return_as_set = False, join_text = None):
    hashtags_found = re.findall(HASHTAG_REGEX, text)
    if not join_text:
        return set(hashtags_found) if return_as_set else hashtags_found
    else:
        return join_text.join(hashtags_found)
