import numpy as np
import matplotlib.pyplot as plt
import csv

# Constants for processing
FS = 2e9  # Sampling frequency in Hz
FFT_SIZE = 4096  # FFT size
INPUT_CSV = "rec_data.csv"  # CSV file to read the recorded data
CENTER_FREQUENCY = 1e9  # Center frequency in Hz
SPAN = 5e6  # Span in Hz
REF_LEVEL = -50  # Reference level in dBm
RBW = 10e3  # Resolution bandwidth in Hz

def load_data(file_path):
    # Load the recorded data from a CSV file
    real_parts = []
    imag_parts = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            real_parts.append(float(row[0]))
            imag_parts.append(float(row[1]))
    data = np.array(real_parts) + 1j * np.array(imag_parts)
    return data

def perform_fft(data, fs, fft_size):
    # Perform FFT on the data
    fft_result = np.fft.fft(data, n=fft_size)
    frequencies = np.fft.fftfreq(fft_size, d=1/fs)
    return frequencies, np.abs(fft_result)

def plot_fft(frequencies, fft_result):
    # Convert FFT result to dBm
    fft_result_dbm = 20 * np.log10(fft_result / np.max(fft_result)) + REF_LEVEL

    # Calculate frequency range for plotting
    low_freq = CENTER_FREQUENCY - SPAN / 2
    high_freq = CENTER_FREQUENCY + SPAN / 2

    # Filter frequencies and FFT results within the desired span
    mask = (frequencies >= low_freq) & (frequencies <= high_freq)
    filtered_frequencies = frequencies[mask]
    filtered_fft_result_dbm = fft_result_dbm[mask]

    plt.figure()
    plt.plot(filtered_frequencies, filtered_fft_result_dbm)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude (dBm)")
    plt.title("FFT Spectrum")
    plt.grid(True)
    plt.xlim(low_freq, high_freq)
    plt.ylim(REF_LEVEL - 20, REF_LEVEL + 10)  # Adjust y-limits based on reference level
    plt.show()

def main():
    data = load_data(INPUT_CSV)
    frequencies, fft_result = perform_fft(data, FS, FFT_SIZE)
    plot_fft(frequencies, fft_result)

if __name__ == "__main__":
    main()