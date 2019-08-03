# How to use the device

<< In person demo >>

# How to log the activities

 1. aTimeLogger - Time Tracker - This app is helpful for activity tracker, custom made activity icons make it easy to use. Make sure to include all the activities in the same way written in Github to the app before starting (including case and space). In order to add these activities : Go to the fourth section in the app denoted by list logo → Click on the add button found in the bottom right corner → Enter the activity names exactly in the way in GitHub → Press the tick.

2. When starting to record click on the current activity icon and pause/stop the previous activities. After the data collection, a report can be created of the log in csv format. ( Go to last section in the app denoted by three dots → reports → Create report (Choose the correct date) → Export option on top right → CSV

Note: Minor activities like opening the door, pressing the button on the elevator etc need not be logged. Please take a look at the activities in the GitHub readme for a better picture of the kind of activities.



# How to label the activities

1. Raw data is exported in the form of csv file named with the start time and date is exported from BLE Sensor tag app
2. Run data_label.py as below:
```
python data_label.py -r <raw_data_path> -l <alogger_path> -id <user_id>
```

```
python data_label.py --help
```
```
usage: data_label.py [-h] -r R -l L -id ID

optional arguments:
  -h, --help  show this help message and exit
  -r R        Provide raw data path
  -l L        Provide alogger path
  -id ID      Provide user ID

```

3. A new csv file will be created with timestamp and labels

Note:

1. New activities needs to be updated in GitHub readme.
2. Inform if there is an error message from running the data_label.py file.


# Dealing with the files

1. Upload the generated csv file with labels to Dataset repo, in the correct User<id> folder
2. Pass the alogger and raw data file to us
