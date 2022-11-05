import numpy as np
import pandas as pd
import matplotlib

enroll = pd.read_csv('./data/additional/enrollments.csv', delimiter= ',')

enroll[['user_id', 'type', 'last_activity_at', 'total_activity_time']]
enroll[enroll.type != 'StudentViewEnrollment']

discuss = pd.read_csv('./data/additional/discussions.csv')
discuss = discuss.loc[:, discuss.columns != "post_id"]
discuss_plot = discuss.plot.scatter(x = "discussion_topic_message_length", y = "post_message_length")
discuss_plot
