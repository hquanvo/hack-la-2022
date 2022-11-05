import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

from procrastination_analysis import *

nagivation_event = pd.read_csv('./data/navigation_events.csv')
nagivation_event = nagivation_event.to_numpy()


enroll = pd.read_csv('./data/additional/enrollments.csv', delimiter= ',')
enroll[['user_id', 'type', 'last_activity_at', 'total_activity_time']]
enroll[enroll.type != 'StudentViewEnrollment']
student_id = enroll.loc[:, ['user_id']]

assignment = pd.read_csv('./data/additional/assignments.csv').drop({'unlock_at', 'lock_at'}, axis = 1)
assignment = assignment[assignment.published == True]
assignment_id = assignment.loc[:, ['id']]

get_proc_index(assignment_id, nagivation_event, student_id, 100)

discuss = pd.read_csv('./data/additional/discussions.csv')
discuss_clean = discuss.groupby(['discussion_topic_title','discussion_topic_id' , 'discussion_topic_message_length']).agg({'discussion_topic_title' : 'size'}).rename(columns={'discussion_topic_title' : 'number_of_message'}).reset_index()

x_axis = discuss_clean.discussion_topic_message_length
y_axis = discuss_clean.number_of_message
xlabel = "Character length of the topic"
ylabel = "The number of messages posted for a particular topic"  

# making a scatterplot for discussion data
# setting the size of the plot
f = plt.figure()
f.set_figwidth(14)
f.set_figheight(10)

plt.scatter(x_axis, y_axis)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

# zip joins x and y coordinates in pairs
for x, y in zip(x_axis, y_axis):
    label = f"({x},{y})"

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    


plt.show()




                 