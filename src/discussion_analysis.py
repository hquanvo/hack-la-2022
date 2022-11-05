#calculates discussion analysis score

discussions_engagement = {}

#topics is list of topic ids, max is the max weight of this aspect, 
def get_disc_analysis_score(topics,discussions, max, per_student_target_participation, target_discussion_engagement_arity, students):
    total_discussions_engagement = 0
    for t in topics:
        topic_discussions = []
        for c in discussions:
            if c[6] == t[0]:
                topic_discussions.append(c)


        total_discussions_engagement += get_engagement_level_for_discussion(t, topic_discussions, per_student_target_participation, target_discussion_engagement_arity, students)

    return max - (((total_discussions_engagement/len(topics))/100) * max)

def get_engagement_level_for_discussion(topic, discussions, student_target_participation, target_discussion_engagement_arity, students):
    engagement = get_student_participation(student_target_participation, students, discussions) + get_reply_arity(target_discussion_engagement_arity, discussions)
    discussions_engagement.update({topic: engagement})
    return engagement

def get_student_participation(student_target_participation, students, discussions):
    participating_students = []
    for s in students: 
        participation_counter = 0
        for d in discussions:
            if s == d[0]:
                participation_counter += 1
            
        

    return 50 * (len(participating_students)/len(students))

def get_reply_arity(target_discussion_engagement_arity, discussions):
    return 50 * (len(discussions)/target_discussion_engagement_arity)