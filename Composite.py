from moviepy.editor import AudioFileClip, CompositeAudioClip

# 定义音频文件路径
melodyFile = 'random_melody.wav'
thirdsFile = 'random_major_thirds.wav'
fifthsFile = 'random_perfect_fifths.wav'

def combineAudio():
    # 加载音频文件
    melodyClip = AudioFileClip(melodyFile)
    thirdsClip = AudioFileClip(thirdsFile).volumex(0.5)  # 大三度音量50%
    fifthsClip = AudioFileClip(fifthsFile).volumex(0.5)   # 纯五度音量50%

    # 创建复合音频剪辑
    combinedAudio = CompositeAudioClip([melodyClip, thirdsClip, fifthsClip])
    
    # 设置每秒帧数 (44100Hz采样率)
    combinedAudio.fps = 44100



    # 写入合成的音频文件
    combinedAudio.write_audiofile('combined_audio.wav')


if __name__ == "__main__":
    combineAudio()
