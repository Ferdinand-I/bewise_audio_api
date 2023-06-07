"""Модуль с утилитами."""
import io
import uuid
from urllib.parse import urlencode

import pydub
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import reverse
from rest_framework.request import Request


def save_as_mp3(file: InMemoryUploadedFile):
    """Конвертация и запись загруженного файла."""
    uuid_salt = uuid.uuid4()  # uuid соль, чтобы избежать дубликаты имён
    _format = 'mp3'
    name = f'{".".join(file.name.split(".")[:-1])}_{uuid_salt.hex}.{_format}'
    file = file.read()
    converted = pydub.AudioSegment.from_file(io.BytesIO(file)).export(
        settings.MEDIA_ROOT / f'{name}', format=_format)
    return converted.name
    # wav = pydub.AudioSegment.empty()
    # for chunk in file.chunks():
    #     wav += pydub.AudioSegment.from_file(io.BytesIO(chunk))
    # converted = wav.export(settings.MEDIA_ROOT / f'{name}', format=_format)
    # return converted.name


def make_url(request: Request, audio_id: int, user_id: int):
    """Билд url для скачивания аудио."""
    uri = request.build_absolute_uri(reverse('audio'))
    params = {'id': audio_id, 'user': user_id}
    return uri + '?' + urlencode(params)
