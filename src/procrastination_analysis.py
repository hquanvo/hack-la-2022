import datetime
# defines functions used for analysing procrastination from the dataset

# additional data 
assignment_procs = {}

# returns a score out of the given max that determines how much bad a problem procrastination is for this class
# assignments is set  of assignments, f_access_set is set of activities
# specifying when the student first accessed the assingnment,  max is int
def get_proc_index(assignments, access_set, student_set, max):
    total_avg_procs = 0
    for a in assignments:
        total_avg_procs += get_proc_avg_for_assignment(a, access_set, student_set)


    return total_avg_procs/max

# gets average procrastination index for an assignment
def get_proc_avg_for_assignment(assignment,access_set, student_set):
    total_proc = 0
    assignment_access_set = filter(is_assignment, access_set)
    this_assignment_access_set = []
    assignment_procs.update({assignment: {}}) 

    for access in assignment_access_set:
        if (access[0] == assignment):
            this_assignment_access_set.append(access)

    for s in student_set:
        accesed_by_this_student = []
        for a in this_assignment_access_set:
            if (a[-1] == s):
                accesed_by_this_student.append(a[2])
        
        s_proc = get_proc_index_for_stu(assignment, s, accesed_by_this_student)
        total_proc += s_proc
        student_procs_for_for_assignment = assignment_procs.get(assignment)
        student_procs_for_for_assignment({s: s_proc}) 

    return total_proc/len(access_set)
    
#helper for get_proc_avg_for_assignment
def is_assignment(activity):
    return activity[-5] == "assignment" 

# gets the procrastination index for a specific student 
# if student accessed prior to halfway between assignment open date and close date, return 0
# if student accessed between mid and close date, return 0 -> 100 exponentially
# if student submitted afterwards or no submission, then return 100
def get_proc_index_for_stu(assignment, f_access_set):
    times = map(convert_str_to_datetime, f_access_set)
    earliest_access = get_earliest_access(times)
    assignment_due = datetime.datetime.strptime(assignment[1], '%Y-%m-%d %H:%M:%S.%f')
    assignment_open = datetime.datetime.strptime(assignment[2], '%Y-%m-%d %H:%M:%S.%f')
    midpoint = assignment_open + (assignment_due - assignment_open)/2
    if (midpoint.date() >= assignment_due.date()):
        return 0
    elif (earliest_access.date() > assignment_due.date()):
        return 100
    else: 
        return 100 - (((assignment_due - midpoint).total_seconds()/(assignment_due - earliest_access).total_seconds()) * 100)



#helper for get_proc_index_for_stu
def convert_str_to_datetime(dtSTR):
    return datetime.datetime.strptime(dtSTR, '%Y-%m-%d %H:%M:%S.%f')

#helper for get_proc_index_for_stu
def get_earliest_access(f_access_set):
    return min(f_access_set)

