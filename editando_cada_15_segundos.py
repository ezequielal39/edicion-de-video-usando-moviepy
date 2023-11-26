from moviepy.editor import VideoFileClip, concatenate_videoclips

# Suponiendo que 'video.mp4' es tu video y está en el mismo directorio que tu script
video_path = 'video.mp4'  # Reemplaza con la ruta real de tu video

# Cargar el video
clip = VideoFileClip(video_path)

# Lista para guardar los segmentos cortados
segments = []

# Calcular el número de segmentos basado en la duración del video
num_segments = int(clip.duration // 15)

# Cortar 2 segundos de video cada 15 segundos
for i in range(num_segments):
    start = i * 15
    # Asegurarse de que el segmento no exceda la duración del video
    if start < clip.duration:
        end = start + 2 if start + 2 <= clip.duration else clip.duration
        segment = clip.subclip(start, end)
        segments.append(segment)

# Concatenar todos los segmentos en un solo clip
final_clip = concatenate_videoclips(segments)

# Guardar el clip final en un archivo
final_clip.write_videofile('final_cut_video.mp4', codec='libx264', audio_codec='aac')

# Cerrar el objeto del clip y los segmentos para liberar recursos
clip.close()
final_clip.close()
