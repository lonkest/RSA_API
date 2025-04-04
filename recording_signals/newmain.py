import os
import numpy as np
import csv

# Constants for recording
RECORD_TIME = 1000  # Record time in milliseconds
RECORDER_ROOT = "C:\\gal_work\\RSA_API\\C++\\x64\\Debug\\rsa_api_cpp.exe"
CENTER_FREQUENCY = -1.7e07  # Center frequency in Hz
BW = 1e7  # Bandwidth in Hz
OUTPUT_CSV = "rec_data.csv"  # CSV file to save the recorded data


def start_recording():
    # Construct the command to start recording with the RSA-306B
    command = RECORDER_ROOT + " " + str(RECORD_TIME) + " " + str(CENTER_FREQUENCY) + " " + str(BW)
    print("Para: " + command)

    os.system(command)

    # Load recorded data from the binary file
    try:
        data = np.fromfile("rec_data.csv", dtype=np.complex64)
    except FileNotFoundError:
        print(f"Error: The file temp_data.dat was not found.")
        return

    # Create and write data to CSV
    with open(OUTPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Real", "Imaginary"])  # Header
        for sample in data:
            writer.writerow([sample.real, sample.imag])

    print(f"Data recorded and saved to {OUTPUT_CSV}")


if __name__ == "__main__":
    # Ensure the CSV file is created before writing
    with open(OUTPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Real", "Imaginary"])  # Write header to create the file

    start_recording()