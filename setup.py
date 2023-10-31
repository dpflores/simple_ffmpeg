import os
# Get the current path with os
current_path = os.getcwd()
command = f'python3 {current_path}/main.py'

alias = f"alias ff=\'{command}\'"

def main():
    os.system('sudo apt install ffmpeg')

    # agregar la variable alias al .bashrc
    os.system(f'echo "{alias}" >> ~/.bashrc')

    # Decirle que ahora puede ejecutar el comando ff en cualquier parte para usar el código
    print("Done! Now you can use the command \'ff input_file\' to use the code in a new terminal")

    

    


if __name__ == '__main__':
    main()
