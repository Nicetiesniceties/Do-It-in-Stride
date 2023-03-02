import cv2
import os
import pandas as pd

# input label-checking target
name = input("Name (CY/DK/RY):")
if name not in ["CY", "DK", "RY"]:
    print("Invalid name, please try again!")
    exit()
userid = input("UserID:")

# hard-coded gesture list
gesture_list = ['NormalWalking', 'ToeTapBehind', 'DraggingBehind',
       'TapWithFootRotatedInwards', 'KickInward', 'DraggingInFront',
       'TapWithFootRotatedOutwards', 'BigStep', 'MidairRotationInwards',
       'MidairRotationOutwards', 'BendingBehind', 'Delay', 'KickOutward',
       'KickForward', 'SmallStep', 'TapInward', 'LiftInFront',
       'TapWithHeel', 'ToeTapInFront', 'TapInFrontOfTheOtherFoot',
       'TapOuward', 'Click', 'Rush']

#read in the label list csv
label_list = pd.read_csv(str(userid) + "_gesture_stride_timestamp_" + name + ".csv")

# remove duplicate by keeping the last one
label_list = label_list.drop_duplicates(subset=["gesture", "foot", "direction", "camera", "first/second"], keep="last")

# checking unlabelled video
# check if a video element exist in the df 
perfect_label = True
for i in gesture_list:
    for j in ["Left", "Right"]:
        for k in ["forth", "back"]:
            for m in ["first", "second"]:
                if not label_list.loc[(label_list["gesture"] == i) & (label_list["foot"] == j) & (label_list["direction"] == k) & (label_list["first/second"] == m)].empty:
                    #print("Labelled: ", i, j, k, m)
                    continue
                else:
                    print("Unlabelled: ", i, j, k, m)
                    perfect_label = False

if perfect_label:
    print("Perfectly Label with no missing data!")

# save the updated label list
label_list.to_csv(str(userid) + "_gesture_stride_timestamp_" + name + ".csv", index = False)