# Step 1: Record data

### Using device

<< In person demo >>

### Logging data

 1. aTimeLogger - Time Tracker - This app is helpful for activity tracker, custom made activity icons make it easy to use. Make sure to include all the activities in the same way written in Github to the app before starting (including case and space). In order to add these activities : Go to the fourth section in the app denoted by list logo → Click on the add button found in the bottom right corner → Enter the activity names exactly in the way in GitHub → Press the tick.

2. When starting to record click on the current activity icon and stop the previous activity. Always log start and end of a activity.

3. Miscellaneous activities like pressing the button on the elevator, taking out the wallet to pay can be logged under the label (-1 = Not tagged).Please take a look at the activities in the GitHub readme for a better picture of the kind of activities.

4. Try to log activites for entire duration of recording, if some time duration was missed it will not be assigned any label.

5. After the data collection, a report can be created of the log in csv format. ( Go to last section in the app denoted by three dots → reports → Create report (Choose the correct date) → Export option on top right → CSV


# Step 2: Label the activities

1. Raw data is exported in the form of csv file named with the start time and date is exported from BLE Sensor tag app and activity log is exported from alogger app.

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

3. The labelled csv file will be created with timestamp and labels

Note:

1. New activities needs to be updated in GitHub readme and in label.json
2. Inform if there is an error message from running the data_label.py file.


### Dealing with the files

1. Upload the generated csv file with labels to Dataset repo, in the correct Userid folder
2. Pass the alogger and raw data file to us by uploading it in this [drive link](https://drive.google.com/drive/folders/1-jDS2mnpNgkqdmQWidLu5yM5mTSrWbfa?usp=sharing) in your corresponding user folder.
