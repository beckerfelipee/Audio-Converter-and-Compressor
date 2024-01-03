# Config

# Default path for the input folder containing audio files.
# Default value: 'Audio Files/Input Files/'
input_folder_path = 'Audio Files/Input Files/'

# Default path for the output folder where processing results will be saved.
# Default value: 'Audio Files/Output Files/'
output_folder_path = 'Audio Files/Output Files/'

# Define the sampling rate to be used in the audio compression process.
# A lower sampling rate may save space but could affect audio quality.
# A higher sampling rate can preserve audio fidelity, but could result in larger file sizes.
# Consider values between 8000 (very low quality) and 44000 (high quality) [8000, 16000, 32000, 44000]
# Default value: "16000"
compress_sampling_rate = "16000"

# Determines whether the output files should be renamed with a specific action.
# (eg. example.mp3 -> compressed-example.mp3)
# Default value: True
rename_with_action = True
