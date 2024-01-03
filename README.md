# Audio Converter and Compressor

This Python program is designed to convert and compress audio files. The program efficiently handles large batches of audio files, simplifying the process in a single execution. Input files should be located in the `Input Files` directory. Processed files will be stored in the `Output Files` directory. All these locations can be configured in the `config.py` file.

## Execution

To run the program, simply double click on `main.py` or execute the following command in the terminal:
```bash
python main.py
```

## How it Works

1. Navigate to the `Audio Files` folder.
2. Place the audio files you want to manipulate in the `Input Files` folder.
3. Run the program and select an option.
4. Follow the steps provided during the process.
5. View the results in the `Output Files` folder.

Simple like that.

## Requirements

Ensure you have `Python 3` or a later version installed.

The `PyDub` lib is used for audio manipulation.

```bash
pip install pydub
```

## Configurations

In `config.py` you can adjust some settings to customize the program's behavior, like:

- **Input and Output Directories:** Change the directories for input and output audio files.
- **Compression Rate:** Change the desired compression rate for the audio files.
- **File Name Change:** Determines whether the output files should be renamed with a specific action.

Tip: You can edit this file using a text editor if you don't have a dedicated IDE.

## LICENSE

This program is under the MIT License for utility, education, and non-commercial use. Feel free to redistribute or build upon it with proper credit. For details, refer to the [MIT License](https://opensource.org/licenses/MIT).



---

#### Feel free to provide feedback or report issues through the GitHub repository. We appreciate your contribution to the project!

