import numpy as np
import pandas as pd
import glob
import collections
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from collections import Counter
import sys
from operator import itemgetter
from itertools import *
import argparse
import json

sns.set()


def missing_time(time):

    count = 0
    diff = np.diff(time).tolist()
    for i, val in enumerate(diff):
        if(val != 1):
            print("Error")
            # print("Missed time (sec)", time[i + 1], time[i])
            if count == 0:
                time_clean = time[i]
            count = count + 1

    print("Total errors:", count)
    return time_clean


def include_time(data, hh_mm_ss):
    if len(data.Acc_X.values) != len(hh_mm_ss):
        data = data.iloc[0:len(hh_mm_ss), ]
        data.is_copy = None

    data["Time(hh:mm:ss)"] = hh_mm_ss
    data["Label"] = np.nan
    data = data.drop(columns=['Mag_X', 'Mag_Y', 'Mag_Z'])
    return data


def change_labels(data, start, end, label):

    data.loc[(data["Time(hh:mm:ss)"] >= start) & (
        data["Time(hh:mm:ss)"] <= end), "Label"] = label
    return data


def timestamp(path, store=False, user_num=3):

    data = pd.read_csv(path, header=0)

    time = np.array(data.Mag_X.values)

    counter_raw = collections.Counter(time)

    check_raw = [int(i) for i in list(counter_raw.keys())]

    plt.plot(time, 'r.', markersize=2)
    plt.xlabel("Sample number")
    plt.ylabel("Time (sec)")
    plt.title("Check non-linearity for data loss")

    plt.show()

    if check_raw != list(range(min(check_raw), max(check_raw) + 1)):

        print("Data missed for a certain duration due to inactivity,check the period")
        time_clean = missing_time(check_raw)

        time_s = time[0:time_clean].astype(float) - (time[0])

        counter = collections.Counter(time_s)

        print("Mean sampling rate for this data:",
              np.mean(list(counter.values())))

        plt.figure()
        plt.plot(time_s, 'r.', markersize=2)
        plt.xlabel("Sample number")
        plt.ylabel("Time (sec)")
        plt.title("Re-check non-linearity for data loss")

    else:
        print("No error in seconds")

        time_s = time.astype(float) - (time[0])

        counter = collections.Counter(time_s)

        print("Mean sampling rate for this data:",
              np.mean(list(counter.values())))

    plt.show()

    plt.figure()
    plt.plot(list(counter.keys()), list(counter.values()), 'r')
    plt.xlabel("Time (sec)")
    plt.ylabel("Sampling rate (Hz)")
    plt.title("Sampling rate vs time")

    fname = path.split("/")[-1]
    date = fname.split("_")[0].split("-")
    time = fname.split("_")[1].split("-")

    start_time = datetime.datetime(int(date[0]), int(date[1]), int(date[2]),
                                   int(time[0]), int(time[1]), int(time[2]))

    hh_mm_ss = [start_time + datetime.timedelta(seconds=i)
                for i in time_s.tolist()]

    data = include_time(data, hh_mm_ss)

    print("Total duration:", str(datetime.timedelta(seconds=time_s[-1])))

    return data


def alogger(path, label_dict):

    df = pd.read_csv(path, header=0)

    row_NaN = df[df["From"] == "%"].index.tolist()[0]

    df = df.loc[0:row_NaN - 1]

    start = df["From"]
    end = df["To"]

    assert (all([i in label_dict.keys()
                 for i in df["Activity type"]])), "Unknown label found, add the new activity in label.json"

    label = [label_dict.get(i) for i in df["Activity type"]]

    return start, end, label


def data_labelling(data, alogger_path, label_dict, fname, user_num, store):

    start, end, label = alogger(alogger_path, label_dict)

    for i, val in enumerate(start):

        start_time = datetime.datetime.strptime(val, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(end[i], "%Y-%m-%d %H:%M:%S")
        data = change_labels(data, start_time, end_time, label[i])

    if store:
        data.to_csv(str(user_num) + "_" + fname, index=False)


if __name__ == '__main__':

    # required defines a mandatory argument
    # default defines a default value if not specified

    parser = argparse.ArgumentParser()

    parser.add_argument('-r', type=str, required=True,
                        help="Provide raw data path")
    parser.add_argument('-l', type=str, required=True,
                        help="Provide alogger path")

    parser.add_argument('-id', type=int, required=True,
                        help="Provide user ID")

    args = parser.parse_args()

    # Timestamping section,change raw_data_path (example given below) to the file path from the BLE sensor
    # tag app

    raw_data_path = args.r
    alogger_path = args.l
    user_num = args.id

    fname = raw_data_path.split("/")[-1]
    data = timestamp(raw_data_path)

    with open('./label.json') as f:
        label_dict = json.load(f)
    f.close()

    # Labelling section.
    # Remember to include new activites to the label dict in the json file with appropriate
    # labels and also add to the GitHub Readme

    data_labelling(data, alogger_path, label_dict,
                   fname, user_num=user_num, store=True)
