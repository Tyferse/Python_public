import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip


frame_width = 596
frame_height = 421
fps = 30

# Путь для сохранения видео
output_video_path = 'badapple_edition.mp4'

# Инициализация объекта видео
out = cv2.VideoWriter(output_video_path,
                      cv2.VideoWriter.fourcc(*'mp4v'),  # mp4v
                      fps, (frame_width, frame_height))

# Папка с кадрами
frames_folder = r"C:\Code\Python3\Sandbox#py\badapple\freefemimplem\madeframes"

# Считывание кадров и запись в видео
for frame_name in os.listdir(frames_folder):  # sorted(os.listdir(frames_folder), key=lambda x: int(x.split('_')[1][:-4])):
    frame_path = os.path.join(frames_folder, frame_name)
    frame = cv2.imread(frame_path)
    out.write(frame)
    # print(i)

out.release()
cv2.destroyAllWindows()

print('adding audio')
video = VideoFileClip("badapple_edition.mp4")

# Загрузка аудиофайла
audio = AudioFileClip("【東方】Bad Apple!! ＰＶ【影絵】 (256  kbps).mp3")

# Добавление звуковой дорожки к видео
video = video.set_audio(audio)

# Сохранение видео с новой звуковой дорожкой
video.write_videofile("sound_output.mp4", codec="libx264")
