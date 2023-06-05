"""Модуль с утилитами."""
import io
from datetime import datetime
from urllib.parse import urlencode

import pydub
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


def convert_wav_to_mp3_and_save(file: InMemoryUploadedFile):
    """Конвертация загруженного файла."""
    _format = 'mp3'
    name = (
        f'{file.name.split(".")[0]}_'
        f'{datetime.now().strftime("%y%m%d%H%M%S%f")}.{_format}'
    )
    file = file.read()
    converted = pydub.AudioSegment.from_file(io.BytesIO(file)).export(
        settings.MEDIA_ROOT / f'{name}', format=_format)
    return converted.name


def make_url(uri: str, audio_id: int, user_id: int):
    """Билд url для скачивания аудио."""
    params = {'id': audio_id, 'user': user_id}
    return uri + '?' + urlencode(params)
