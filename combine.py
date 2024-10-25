from moviepy.editor import *
import pysynth
import Constants
def combineMelodies(melody:str,chords:list,volume=0.5)->AudioFileClip:
    
    if type(chords)!=list:
        chords=[chords]
    if type(melody)==str:
        melody=AudioFileClip(melody)
    AudioFileClips=[melody]
    for chord in chords:
        if type(chord)==str:
            chord=AudioFileClip(chord)
        AudioFileClips.append(chord.volumex(volume))
    # 合并音频文件
    finalAudio=CompositeAudioClip(AudioFileClips).set_duration(melody.duration)
    finalAudio.fps=44100
    return finalAudio
def simplyCombineMelodies(melodies:list,volume=1)->AudioFileClip:
    if type(melodies)!=list:
        melodies=[melodies]
    AudioFileClips=[]
    for melody in melodies:
        if type(melody)==str:
            AudioFileClips.append(AudioFileClip(melody).volumex(volume))
        else:
            AudioFileClips.append(melody.volumex(volume))
    # 合并音频文件
    finalAudio=CompositeAudioClip(AudioFileClips)
    finalAudio.fps=44100
    return finalAudio
def strengthenBeats(beats:AudioFileClip, times:int=4)->AudioFileClip:
    if type(beats)==str:
        beatAudio=AudioFileClip(beats)
    else:
        beatAudio=beats
   
    return CompositeAudioClip([beatAudio]*times)
def toAudioFileClipS(melody:str,volume=1)->AudioFileClip:
    pysynth.make_wav(melody,fn='temp.wav',bpm=Constants.BPM)
    return AudioFileClip('temp.wav').volumex(volume)
import hashlib
from time import time
def toAudioFileClip(melody: str, volume=1) -> AudioFileClip:
    # 生成MD5哈希值作为文件名
    try:
        md5_hash = hashlib.md5(str(melody).encode()).hexdigest()
    except:
        md5_hash=str(int(time()))
    filename = f"{md5_hash}.wav"

    # 生成WAV文件
    pysynth.make_wav(melody, fn=filename, bpm=Constants.BPM)

    # 返回音频文件剪辑
    return AudioFileClip(filename).volumex(volume)

def writeAudio(audio,filename="result.wav")->None:
    audio.fps=44100
    audio.write_audiofile(filename)
def duplicate(audio:AudioFileClip,times:int=20)->AudioFileClip:
    return concatenate_audioclips([audio]*times)

import mido
from mido import MidiFile, MidiTrack, Message

def createMidiFromPysynthNotes(pysynthMelody, midiFileName='output.mid'):
    mid = MidiFile()  # 创建一个新的MIDI文件
    track = MidiTrack()  # 创建一个新的MIDI轨道
    mid.tracks.append(track)  # 将轨道添加到MIDI文件中

    # 遍历音符列表
    for note, duration in pysynthMelody:
        # 将音符转换为MIDI音符，C大调中，C4是60
        midiNote = mido.note_name_to_number(note)
        
        # 添加音符的Note On消息
        track.append(Message('note_on', note=midiNote, velocity=64, time=0))
        
        # 添加音符的Note Off消息，duration转为MIDI时钟单位，通常使用480作为四分音符
        timeOff = int(duration * 480)  # 将持续时间转换为时间单位（MIDI时钟单位）
        track.append(Message('note_off', note=midiNote, velocity=64, time=timeOff))

    # 保存MIDI文件
    mid.save(midiFileName)
    print(f"MIDI文件已保存为 {midiFileName}")

# 用法示例
# 假设您已有生成的pysynthMelody
# createMidiFromPysynthNotes(pysynthMelody, 'generated_melody.mid')
