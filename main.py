import os
import argparse
import ffmppeg_commands as ffmpeg

TEXT = "\nWelcome to my simple ffmpeg, it will allows you to use ffmpeg in a simple way\n"

OPTIONS = "Select what to do with yur input file:\n" \
            "1. Convert a video to a gif\n" \
            "2. Convert a video to a mp4\n" \
            "3. Convert a video to any extension (not tested)\n" \
            "4. Trim video\n" \
            "5. Compress video\n" \
            

def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str, default='test.webm',
                        help='What is the input file')

    args = parser.parse_args()
    input_file = args.input_file

    print(TEXT)
    print(OPTIONS)
    option = input(">> ")
    print('Output file name (no extension): ')
    output_file = input(">> ")
    
    if option == '1':
        ffmpeg.convert_to_gif(input_file, output_file)
    
    if option == '2':
        ffmpeg.convert_to_mp4(input_file, output_file)
    
    if option == '3':
        print('type extension (eg: .mp4, .webm, .wav): ')
        extension_file = input(">> ")
        ffmpeg.convert_to_any(input_file, output_file, extension_file)

    if option == '4':
        print('init_time (format hh:mm:ss): ')
        init_time = input(">> ")
        print('end_time (format hh:mm:ss): ')
        end_time = input(">> ")
        ffmpeg.trim_video(input_file, output_file, init_time, end_time)

    if option == '5':
        ffmpeg.compress_video(input_file, output_file)






    

if __name__ == '__main__':
    main()