
import pyaudio, wave

def recorder() :

    scndLp = True
    while scndLp :
        seconds = input("For how long do you want to record: ")
        if seconds.isdigit() :
            scndLp = False
            seconds = int(seconds)
        else :
            print("That is not a valid number.")


    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start recording...")

    frames = []
    for i in range(0, int(RATE / CHUNK * seconds)) :
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording stopped...")

    stream.stop_stream()
    stream.close()
    p.terminate()


    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
