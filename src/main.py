import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

enroll = pd.read_csv('./data/additional/enrollments.csv', delimiter= ',')
enroll[['user_id', 'type', 'last_activity_at', 'total_activity_time']]
enroll[enroll.type != 'StudentViewEnrollment']

discuss = pd.read_csv('./data/additional/discussions.csv')
discuss_clean = discuss.groupby(['discussion_topic_title','discussion_topic_id' , 'discussion_topic_message_length']).agg({'discussion_topic_title' : 'size'}).rename(columns={'discussion_topic_title' : 'number_of_message'}).reset_index()

x_axis = discuss_clean.discussion_topic_message_length
y_axis = discuss_clean.number_of_message
xlabel = "Character length of the topic"
ylabel = "The number of messages posted for a particular topic"

# making a scatterplot
discuss_clean
plt.scatter(x_axis, y_axis)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()




                 