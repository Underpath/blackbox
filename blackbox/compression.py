import tarfile
import config


def compress():
    paths = config.get_option('Folders', 'Input', 'str_list')
    with tarfile.open(config.COMPRESSED_FILE_PATH, 'w:gz') as tar:
        for path in paths:
            tar.add(path)


def uncompress():
    output_path = config.get_path('output_path', 'Output')

    with tarfile.open(config.COMPRESSED_FILE_PATH, 'r:gz') as tar:
        tar.extractall(output_path)
