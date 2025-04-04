# DIFFERENTIAL_SYNC = 1
# SYMBOL_SYNC = 2
# UART_SYNC = 3
#
# recording = 1
#
# # init_window_size = 64*64
# # init_fft_size = 4096
# # MAX_NUMBER_OF_SYMBOLS = 32
# # INIT_PIXEL_FIX = 0
# # number_of_sample_in_a_bit = 28.5
# # MISS_SYNC_CORRECTION = 0
# #
# # PATCH_SIZE_PERCENTAGE = 0.25
# # SYMBOL_SYNC_DETECTION_RATIO = 0.3
# # FFT_FREQUENCY_DETECTION_RATIO = 0
# # base_frequency = 800
# #
# # number_of_bits_in_symbol = 2
# # sync_symbol = SYMBOL_SYNC
# # sync_distance = 8
#
# center_frequency = int(2.4e9)
# bw = 40000000
# fs = 40000000  # Sampling frequency
# fft_size = 4096
# frequency_resolution = fs / fft_size
#
# low_freq = 2.35e9
# high_freq = 2.45e9
#
# low_offset = low_freq - center_frequency
# high_offset = high_freq - center_frequency
#
# low_index = int((fft_size * (low_offset + fs / 2))/ fs)
# high_index = int((fft_size * (high_offset + fs / 2))/ fs)
#
#
# RECORD_DELAY_SYNC = 1
# FAR_AWAY = 1
# SAME_PC = 0
# SYSTEM_RECORDING_CONFIGURATION = SAME_PC
# analyse_signal_array = [18153,17719,17476,17323,17219,111786,111691,111611,111550,111497,111453,111416,111382,111356,111334,111316,111300,0
#     ,0,0,1240,1190,1142,1101,1061,1022,989,957,926,898,872,847]



DIFFERENTIAL_SYNC = 1
SYMBOL_SYNC = 2
UART_SYNC = 3

recording = 1

init_window_size = 64*64
init_fft_size = 4096
MAX_NUMBER_OF_SYMBOLS = 32
INIT_PIXEL_FIX = 0
number_of_sample_in_a_bit = 28.5
MISS_SYNC_CORRECTION = 0

PATCH_SIZE_PERCENTAGE = 0.25
SYMBOL_SYNC_DETECTION_RATIO = 0.3
FFT_FREQUENCY_DETECTION_RATIO = 0
base_frequency = 800

number_of_bits_in_symbol = 2
sync_symbol = SYMBOL_SYNC
sync_distance = 8

center_frequency = int(2.44e9)
bw = 10500000
RECORD_DELAY_SYNC = 1
FAR_AWAY = 1
SAME_PC = 0
SYSTEM_RECORDING_CONFIGURATION = SAME_PC
analyse_signal_array = [18153,17719,17476,17323,17219,111786,111691,111611,111550,111497,111453,111416,111382,111356,111334,111316,111300,0
    ,0,0,1240,1190,1142,1101,1061,1022,989,957,926,898,872,847]