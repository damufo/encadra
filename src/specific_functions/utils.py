# -*- coding: utf-8 -*-


import re
import math

def size_bytes_h(num, suffix):
    magnitude = int(math.floor(math.log(num, 1024)))
    val = num / math.pow(1024, magnitude)
    if magnitude > 7:
        return '{:.1f}{}{}'.format(val, 'Yi', suffix)
    return '{:3.1f}{}{}'.format(
        val, ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi'][magnitude], suffix)

def get_valid_filename(file_name):
    file_name = str(file_name).strip().replace(' ', '_')
    file_name = re.sub(r'(?u)[^-\w.]', '', file_name)
    file_name = file_name.replace(".", "", file_name.count(".") -1)
    if not any(i.isalnum() for i in file_name):
        file_name = ''
    return file_name
