import array
import matplotlib.pyplot as plt
import numpy
import numpy as np

def read_file_and_create_array(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        samples_array = array.array('h', file_content)
    real_parts = numpy.array(samples_array[0::2])
    imaginary_parts = numpy.array(samples_array[1::2])
    complex_numbers = np.vectorize(complex)(real_parts, imaginary_parts)

    absolute_values = np.abs(complex_numbers)
    # plt.plot(absolute_values)
    # plt.show()
    return absolute_values