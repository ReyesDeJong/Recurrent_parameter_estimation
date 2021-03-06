import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from os import listdir
from os.path import isfile, join

PATH_TO_PROJECT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PATH_TO_PROJECT)

def plot_n_examples(data_path, subset_name="training", n_examples=3, plot_freq_hist=True):

    data = np.load(data_path)
    subset = data[subset_name]
    idx = np.random.randint(0, subset['n_sequences'], size=n_examples)
    for i in idx:
        plt.plot(subset["dense_time"][i],
                 subset["real_values"][i], '-o', ms=5, label="underlying_model")
        plt.plot(subset["time"][i],
                 subset["sequences"][i], '-o', ms=5, label="noisy_samples")
        #plt.errorbar(subset["time"][i], subset["sequences"][i], yerr=subset["noise"][i], fmt="o", ms=5, label="samples")
        plt.xlabel("time")
        plt.ylim([-1,1])
        plt.ylabel("amplitude")
        title = "amp: " + "{0:.2f}".format(subset["params"][i][0]) \
                + ", freq: " + "{0:.2f}".format(subset["params"][i][1]) \
                + ", period: " + "{0:.2f}".format(1 / subset["params"][i][1])
        plt.title(title)
        plt.grid(True)
        plt.legend()
        #plt.savefig("./plots/" + subset_name + "_" + self.seq_shape +
        #            "_" + self.noise_distr + "_sample" + str(i).zfill(3) + ".png")
        plt.show()
    if plot_freq_hist:
        a = []
        for i in range(subset['n_sequences']):
            a.append(subset["params"][i][1])
        plt.hist(a)
        plt.title('freq')
        plt.show()

        a = []
        for i in range(subset['n_sequences']):
            a.append(1/subset["params"][i][1])
        plt.hist(a)
        plt.title('period')
        plt.show()

        a=[]
        for i in range(subset['n_sequences']):
            a.append(subset["params"][i][0])
        plt.hist(a)
        plt.title('amplitude')
        plt.show()


def plot_n_examples_all_classes(data_path, subset_name="training", n_examples=3):
    filenames = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    time_series_filenames = [s for s in filenames if "gaussian.pkl" in s]
    for time_series_filename in time_series_filenames:
        time_series_path = os.path.join(data_path, time_series_filename)
        plot_n_examples(time_series_path, subset_name=subset_name, n_examples=n_examples)

data_path = os.path.join(PATH_TO_PROJECT, 'data')
plot_n_examples_all_classes(data_path, subset_name='training', n_examples=5)

