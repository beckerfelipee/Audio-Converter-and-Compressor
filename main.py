from config import input_folder_path, output_folder_path
import functions as fc
import screens as screen

# Variable Declaration
i_f = input_folder_path
o_f = output_folder_path

# Script
while True:
    option = screen.main_options()

    if option == "convert":
        output_extension = screen.ask_output_extension()
        screen.clear()
        screen.header()
        print("Converting files..\n")
        fc.convert_all_files(i_f, o_f, output_extension)

    elif option == "compress":
        output_extension = screen.ask_output_extension()
        screen.clear()
        screen.header()
        print("Compressing files..\n")
        fc.compress_all_files(i_f, o_f, output_extension)

    elif option == "help":
        screen.guide()

    elif option == "clear_input" or option == "clear_output":
        screen.clear()
        if option.endswith("input"):
            folder = i_f
        else:
            folder = o_f
        print(f"You are about to delete all files in the folder: {folder}")
        if fc.safety_ask() == "yes":
            fc.clear_files(folder)

    elif option == "exit":
        break
