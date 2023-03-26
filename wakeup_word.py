import pvporcupine
import struct
import pyaudio
import pyttsx3
import time

porcupine = pvporcupine.create(access_key="C5uK9WtG1jSb3ZG33xpQYCmHJuC44TarnubXVkknTNoetxqU+dhWSw==",keywords=['jarvis'])
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

def check():
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h"*porcupine.frame_length,pcm)
    keyword_index = porcupine.process(pcm)

    if keyword_index>=0:
        return True