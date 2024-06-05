import wave
import struct


def break_the_silence():
        source = wave.open("./assets/in.wav", mode="rb")
        dest = wave.open("./assets/out_2.wav", mode="wb")
        dest.setparams(source.getparams())
        frames_count = source.getnframes()
        data = struct.unpack("<" + str(frames_count) + "h",
                             source.readframes(frames_count))
        new_data = list(filter(lambda x: x <= -5 or x >= 5, data))
        new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
        dest.writeframes(new_frames)
        source.close()
        dest.close()