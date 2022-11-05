import numpy as np
import pandas as pd

enroll = pd.read_csv('./data/additional/enrollments.csv', delimiter= ',')
enroll[['user_id', 'type', 'last_activity_at', 'total_activity_time']]