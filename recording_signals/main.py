import matplotlib.pyplot as plt
import numpy as np

from RSA_IQ_TO_signal import *
from picture_reconstructor import *
import os
import time
import serial
import threading
from flags import *



global record_time
init_number_of_cycles = 4096
limits = 1
fft_relevent_range_low = analyse_signal_array[3]-100
fft_relevent_range_high = analyse_signal_array[0]+100
size_of_signture_base4 = 64
init_base_frequency = 0

init_time = 2.5*1000



recorder_root = "C:\\gal_work\\RSA_API\\C++\\x64\\Debug\\rsa_api_cpp.exe"
print(recorder_root)

def send_configuration(transmition_array):
    global number_of_cycles
    if(SYSTEM_RECORDING_CONFIGURATION == SAME_PC):
        wait = 0.01
        baud_rate = 115200
        serial_port = 'COM9'
        time.sleep(RECORD_DELAY_SYNC)
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        transmition_array = [b"c",b"F"]
        for i in range(len(transmition_array)):
            print(transmition_array[i])
            ser.write(transmition_array[i])
            time.sleep(wait)
        # for cmd in transmition_array:
        #     print(f"Sending: {cmd}")
        #     ser.write(cmd)
        #     time.sleep(wait)

     #   if(sync_symbol != DIFFERENTIAL_SYNC): #needed?
      #      print(str(sync_distance).encode('utf-8')+b"\n")
      #      ser.write(str(sync_distance).encode('utf-8')+b"\n")

  #  else:
  #      activate_client()

def start_recording():
    global number_of_cycles
    global record_time
    record_time = 3000
 #   record_time = init_time +((number_of_cycles*40*(sync_distance+sync_symbol-1)/sync_distance) / number_of_bits_in_symbol)
    print(recorder_root+" " + str(record_time) + " " + str(center_frequency)+ " " + str(bw))
    os.system(recorder_root+" " + str(record_time) + " " + str(center_frequency)+ " " + str(bw))



def main():
    global record_time
    global number_of_cycles

    # Clear the CSV file at the start
    open("fft_peaks.csv", "w").close()


    # List of different transmission arrays (customize as needed)
    transmition_array_list = [
        # [b"c", b"c"],
        # [b"c", b"c"],
        # [b"c", b"c"],
        # [b"c", b"c"],
        [b"c", b"F"]#,
        # [b"c", b"c"],
        # [b"c", b"c"],
        # [b"c", b"c"],
        # [b"c", b"c"],
        # [b"c", b"T"]
    ]

    for i, transmition_array in enumerate(transmition_array_list):
        print(f"\n--- Iteration {i + 1} with {transmition_array} ---")
        #number_of_cycles = np.power(2 ,8 - i)
        number_of_cycles = init_number_of_cycles
        if(recording):
            thread_two = threading.Thread(target=start_recording)
            time.sleep(0.1)
            thread_one = threading.Thread(target=send_configuration, args=(transmition_array,))
            thread_one.start()
            thread_two.start()
            thread_one.join()
            thread_two.join()
        if (recording):# and i % 5 == 4):
            samples_array = read_file_and_create_array('iq_stream_test.siqd')
            np.save("samples.npy", samples_array)
        else:
            samples_array = np.load("samples.npy")
        if (recording):# and i % 5 == 4):
            print("finished loading samples")
            generate_frequency_map(samples_array[0:int((init_time/record_time)*len(samples_array))]
                                 ,init_fft_size,iteration_label=f"\n--- Iteration {i + 1} with {transmition_array} ---")
            # generate_frequency_map(samples_array[int(len(samples_array)*3/5):int(len(samples_array))],init_window_size
            #                      ,init_fft_size,True,fft_relevent_range_low,fft_relevent_range_high,init_base_frequency,number_of_bits_in_symbol,None)

    # Keep all plots open at the end
    plt.ioff()
    plt.show()


main()