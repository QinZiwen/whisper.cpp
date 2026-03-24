import librosa
import noisereduce as nr
import soundfile as sf

# 1. 加载音频
data, rate = librosa.load("/Users/qinziwen/Downloads/36850828138-1-192.mp4", sr=16000)

# 2. 降噪（它会自动寻找音频中的静音部分作为噪声样本）
reduced_noise = nr.reduce_noise(y=data, sr=rate, prop_decrease=0.8)

# 3. 保存
sf.write("36850828138-1-192.wav", reduced_noise, rate)
print("降噪完成！请使用 36850828138-1-192.wav 重新跑 whisper.cpp")
