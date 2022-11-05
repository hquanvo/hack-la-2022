import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

enroll = pd.read_csv('./data/additional/enrollments.csv', delimiter= ',')
enroll[['user_id', 'type', 'last_activity_at', 'total_activity_time']]
enroll[enroll.type != 'StudentViewEnrollment']

discuss = pd.read_csv('./data/additional/discussions.csv')
discuss = discuss.loc[:, discuss.columns != "post_id"]
number_of_message = discuss['discussion_topic_message_length'].value_counts()
discuss['number_of_message'] = number_of_message
plt.scatter(discuss.discussion_topic_message_length, discuss.number_of_message)
plt.xlabel("Character length of the topic")
plt.ylabel("The number of messages posted for a particular topic")
plt.show()

topics = pd.read_csv('./data/additional/discussion_topics.csv')
topics[['id', 'title']]

