# ffmpeg -i /Users/qinziwen/Downloads/36850828138-1-192.mp4 \
#     -af "arnndn=m=bd.rnnn,loudnorm" \
#     -ar 16000 \
#     -ac 1 \
#     -c:a pcm_s16le \
#     cleaned_audio.wav

ffmpeg -i /Users/qinziwen/Downloads/36850828138-1-192.mp4 \
    -af "afftdn=nr=12,highpass=f=200,lowpass=f=3000,loudnorm" \
    -ar 16000 \
    -ac 1 \
    -c:a pcm_s16le \
    cleaned_audio.wav
