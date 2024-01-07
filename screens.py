from os import name as os_name, system

def clear():
    print()
    if os_name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    return system(command)

def header():
    clear()
    print("Created by Felipe Becker")
    print("Git Repository: https://github.com/beckerfelipee/Audio-Converter-and-Compressor")
    print("\n=============================================")
    print("         Audio Converter and Compressor       ")
    print("=============================================\n")

def ask_output_extension():
    while True:
        header()
        print("Choose the desired output format:")
        print("[ 1 ] .wav")
        print("[ 2 ] .mp3")
        print("[ 3 ] .ogg\n")

        choice = input("Enter an option (1-3): ")
        if choice == '1':
            return 'wav'
        elif choice == '2':
            return 'mp3'
        elif choice == '3':
            return 'ogg'

def main_options():
    while True:
        header()
        print("Options:")
        print("[ 1 ] Convert")
        print("[ 2 ] Compress")
        print("\nOther options:")
        print("[ 3 ] How it works?")
        print("[ 4 ] Clear input files")
        print("[ 5 ] Clear output files")
        print("[ 6 ] Exit\n")

        # Get user input for option
        user_choice = input("Enter an option (1-6): ")

        # Process user input
        if user_choice == '1':
            return "convert"
        elif user_choice == '2':
            return "compress"
        elif user_choice == '3':
            return "help"
        elif user_choice == '4':
            return "clear_input"
        elif user_choice == '5':
            return "clear_output"
        elif user_choice == '6':
            return "exit"

def guide():
    clear()
    print("- User Guide\n")
    print("This program allows you to convert and compress audio files.\n")

    print("How it Works:\n"
          "     1 - Go to Audio Files folder.\n"
          "     2 - Place the audio files you want to manipulate in the Input Files folder.\n"
          "     3 - Select an option.\n"
          "     4 - Follow the steps provided.\n"
          "     5 - View the results in the Output Files folder.\n")

    print("Convert only:\n"
          "     * Converts audio files to a different format.\n")
    print("Compress:\n"
          "     * Compresses audio files to reduce file size.\n"
          "     * Automatically convert files to match output format before compression.\n")

    back = input("Press [Enter] to go back ")
