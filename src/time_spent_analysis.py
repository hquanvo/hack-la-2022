#will analyse how much tine is spent doing class activities and compares it against the expectations set by the user\\\\\\

student_activity_proc_scores = {}

# 
def get_time_spent_score(enrollments, max, expected_time_in_s):
    total_proc = 0
    for s in enrollments:
        s_proc = (s[-1]/expected_time_in_s) * 100

        total_proc += s_proc
        student_activity_proc_scores.update({s[0], s_proc})

    return (total_proc/len(enrollments)) * max
