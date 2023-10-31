
import os


def get_extension(nombre_archivo):
    # Usa os.path.splitext para dividir el nombre del archivo y la extensión.
    nombre_base, extension = os.path.splitext(nombre_archivo)
    # Elimina el punto (.) de la extensión si lo hay.
    extension = extension.lstrip(".")
    return extension

def convert_to_gif(input_file, output_file):
    os.system(f'ffmpeg -i {input_file} -vf "fps=10,scale=620:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {output_file}.gif')


def convert_to_mp4(input_file, output_file):
    os.system(f'ffmpeg -i {input_file} {output_file}.mp4')

def convert_to_any(input_file, output_file, extension_file):
    os.system(f'ffmpeg -i {input_file} {output_file}{extension_file}')


def trim_video(input_file, output_file, init_time, end_time):
    extension = get_extension(input_file)
    os.system(f'ffmpeg -i {input_file} -ss {init_time} -to {end_time} -c:v copy -c:a copy {output_file}.{extension}')

def compress_video(input_file, output_file):
    crf = 28 # higher crf reduces the file size 
    extension = get_extension(input_file)
    os.system(f'ffmpeg -i {input_file} -vcodec libx264 -crf {crf} {output_file}.{extension}')