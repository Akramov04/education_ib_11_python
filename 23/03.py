import wave
import struct


def cheap_and_dale(number):
    source = wave.open("./assets/in.wav", mode="rb")
    dest = wave.open("./assets/out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    new_data = data[:: number]
    new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
    dest.writeframes(new_frames)
    source.close()
    dest.close()