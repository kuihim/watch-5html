import hashlib
import time
from datetime import datetime
import os
import shutil

_5html_path = '/srv/chen77477/5.html'
_5html_name = os.path.split(_5html_path)[1]
_dump_dir = '/srv/chen77477/data-dump/5html'
_dump_count = 30

if not os.path.exists(_5html_path):
    exit()

if not os.path.exists(_dump_dir):
    os.makedirs(_dump_dir)


def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()


def dump_5html():
    # dump file 5.html_2020-01-01 12:00:00
    dump_name = _5html_name + '@' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    shutil.copyfile(_5html_path, os.path.join(_dump_dir, dump_name))
    files = []
    for f in os.listdir(_dump_dir):
        if _5html_name in f:
            files.append(f)
    files = sorted(files, key=lambda f: f[-20:])
    if len(files) > _dump_count:
        for f in files[0:-_dump_count]:
            os.remove(os.path.join(_dump_dir, f))


if __name__ == '__main__':
    pre_5html_md5 = get_file_md5(_5html_path)
    while True:
        cur_5html_md5 = get_file_md5(_5html_path)
        if cur_5html_md5 != pre_5html_md5:
            pre_5html_md5 = cur_5html_md5
            dump_5html()
        time.sleep(10 * 60)
