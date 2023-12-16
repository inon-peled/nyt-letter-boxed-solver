"""

"""

# NOTE: you'll also need to install external libraries for enchant.
# In macOS: `brew install enchant`
import enchant
import requests

import os
import subprocess

URL = 'https://dumps.wikimedia.org/enwiktionary/latest/enwiktionary-latest-pages-articles-multistream-index.txt.bz2'
SAVE_PATH = 'english_words.csv'


def _download_english_wiktionary(output_path, url):
    print(f'\nDownloading English Wiktionary from {url} ... ', end='')
    response = requests.get(url)
    response.raise_for_status()
    print('done.')

    print(f'Writing to {output_path} ... ', end='')
    with open(output_path, 'wb') as f_response:
        f_response.write(response.content)
    print('done.')


def _decompress_download(input_path):
    print(f'\nDecompressing {input_path} ... ', end='')
    subprocess.run(
        f'bunzip2 {input_path}',
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
    print('done.')


def _extract_english_words(input_path, output_path):
    print('\nBuilding set of all words ... ', end='')
    with open(input_path.replace('.bz2', '')) as f_input:
        words = {
            line.strip().split(':')[2].lower()
            for line in f_input
        }
    print('done.')

    print('Filtering for only English words with at least 3 letters ... ', end='')
    english_dict = enchant.Dict('en_US')
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    english_words = sorted({
        word for word in words
        if (len(word) >= 3) and
           (not (set(word) - english_letters)) and
           english_dict.check(word)
    })
    print('done.')

    print(f'Writing English words to {output_path} ... ', end='')
    with open(output_path, 'w') as f_output:
        for en_word in english_words:
            f_output.write(f'{en_word}\n')
    print('done.')


def _delete_download(download_path):
    path_to_delete = download_path.replace('.bz2', '')
    print(f'\nDeleting {path_to_delete} ... ', end='')
    os.remove(path_to_delete)
    print('done.')


def preprocess(save_path=SAVE_PATH, url=URL):
    if os.path.exists(save_path):
        print(f'\n{save_path} already exists, so not preprocessing' +
              ' -- delete it if you want to use the latest English wiktionary.')
    else:
        temporary_download_path = 'enwiktionary.txt.bz2'
        _download_english_wiktionary(url=url, output_path=temporary_download_path)
        _decompress_download(input_path=temporary_download_path)
        _extract_english_words(input_path=temporary_download_path, output_path=save_path)
        _delete_download(temporary_download_path)

    return save_path
