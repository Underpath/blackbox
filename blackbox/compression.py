import tarfile
import config


COMPRESSED_FILENAME = config.get_option('archive_filename', 'General')
COMPRESSED_FILE_PATH = config.get_path('archive_path', 'General', COMPRESSED_FILENAME)


def compress():
    paths = config.get_option('Folders', 'Input', 'str_list')
    with tarfile.open(COMPRESSED_FILE_PATH, 'w:gz') as tar:
        for path in paths:
            tar.add(path)


def uncompress():
    output_path = config.get_path('output_path', 'Output')

    with tarfile.open(COMPRESSED_FILE_PATH, 'r:gz') as tar:
        tar.extractall(output_path)
