from config import rename_with_action, compress_sampling_rate as sampling_rate
from pydub import AudioSegment
from os import listdir

# Basic Functions

def get_file_extension(file):
    allowed_formats = [".wav", ".ogg", ".mp3"]

    for i in allowed_formats:
        if file.endswith(i):
            return i

    # If no matching extension is found, return None
    print(f"Cannot handle extension from: {file}")
    return None

# Audio Manipulation

def convert_all_files(i_folder_path, o_folder_path, output_extension):
    for file in listdir(i_folder_path):
        if not file.endswith(output_extension):
            convert_audio(i_folder_path, file, o_folder_path, output_extension)

    back = input("\nPress [Enter] to go back ")

def convert_audio(i_folder_path, input_file, o_folder_path, output_extension):
    input_path = i_folder_path + input_file
    input_extension = get_file_extension(input_path)
    if not input_extension:
        return False  # Cant convert the file

    if rename_with_action:
        new_path = o_folder_path + "converted-" + input_file.replace(input_extension, output_extension)
    else:
        new_path = o_folder_path + input_file.replace(input_extension, output_extension)

    to_convert = AudioSegment.from_file(input_path)
    to_convert.export(new_path)
    print(f"Converted file saved at: {new_path}")

    return True

def compress_all_files(i_folder_path, o_folder_path, output_extension):
    for file in listdir(i_folder_path):
        if not file.endswith(output_extension):
            if convert_audio(i_folder_path, file, o_folder_path, output_extension):
                compress_audio(i_folder_path, file, o_folder_path, output_extension)
        else:
            compress_audio(i_folder_path, file, o_folder_path, output_extension)

    back = input("\nPress [Enter] to go back ")


def compress_audio(i_folder_path, input_file, o_folder_path, output_extension):
    input_path = i_folder_path + input_file
    input_extension = get_file_extension(input_path)

    audio = AudioSegment.from_file(input_path)

    if rename_with_action:
        output_path = o_folder_path + "compressed-" + input_file.replace(input_extension, output_extension)
    else:
        output_path = o_folder_path + input_file.replace(input_extension, output_extension)

    audio.export(output_path, parameters=["-ac", "2", "-ar", sampling_rate])
    print(f"Compressed file saved at: {output_path}")
