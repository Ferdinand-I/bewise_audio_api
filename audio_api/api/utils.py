"""Модуль с утилитами."""
import re
import uuid
from urllib.parse import urlencode

import pydub
from django.conf import settings
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.shortcuts import reverse
from rest_framework.request import Request


def save_as_mp3(file: TemporaryUploadedFile):
    """Конвертация и запись загруженного файла."""
    uuid_salt = uuid.uuid4()  # uuid соль, чтобы избежать дубликаты имён
    _format = 'mp3'
    # приводим имя файла в порядок
    name = re.sub(
        r'[,:;#$%^&=><]',
        '',
        f'{".".join(file.name.split(".")[:-1])}_{uuid_salt.hex}.{_format}'
    ).replace(' ', '_')
    wav = pydub.AudioSegment.from_wav(file.temporary_file_path())
    converted = wav.export(settings.MEDIA_ROOT / f'{name}', format=_format)
    return converted.name


def make_url(request: Request, audio_id: int, user_id: int):
    """Билд url для скачивания аудио."""
    uri = request.build_absolute_uri(reverse('audio'))
    params = {'id': audio_id, 'user': user_id}
    return uri + '?' + urlencode(params)
