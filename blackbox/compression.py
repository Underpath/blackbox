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
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, output_path)
