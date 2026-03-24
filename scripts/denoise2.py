import librosa
import noisereduce as nr
import soundfile as sf
import numpy as np
from scipy.signal import butter, lfilter

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

# 1. 加载
data, rate = librosa.load("/Users/qinziwen/Downloads/36850828138-1-192.mp4", sr=16000)

# 2. 预过滤：只保留人声频段 (300Hz - 3500Hz)
# 这能有效去除低频电流声和高频刺耳噪声
filtered_data = butter_bandpass_filter(data, 300, 3500, rate, order=6)

# 3. 进阶降噪
reduced_noise = nr.reduce_noise(
    y=filtered_data, 
    sr=rate, 
    stationary=False, 
    prop_decrease=1.0,
    time_mask_smooth_ms=64 # 增加平滑度，减少电音感
)

# 4. 标准化音量 (让 Whisper 更容易捕捉到声音)
reduced_noise = reduced_noise / np.max(np.abs(reduced_noise))

# 5. 保存
sf.write("optimized_output.wav", reduced_noise, rate)
print("\n\n done!")