import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

enroll = pd.read_csv('./data/additional/enrollments.csv', delimiter= ',')
enroll[['user_id', 'type', 'last_activity_at', 'total_activity_time']]
enroll[enroll.type != 'StudentViewEnrollment']

discuss = pd.read_csv('./data/additional/discussions.csv')
discuss = discuss.loc[:, discuss.columns != "post_id"]
plt.scatter(discuss.discussion_topic_message_length, discuss.post_message_length)
plt.xlabel("Character length of the topic")
plt.ylabel("Character length of the discussion post")
plt.show()