import student_data as data


###########################################################################################
# This function is used by other functions to display a list of student's id & names
###########################################################################################
def list_students(student_ids):
    for student_id in student_ids:
        print(student_id,
              data.students.get(student_id).get('firstName'),
              data.students.get(student_id).get('lastName')
              )


def student_information():
    """
    Report example...
    ================================================================================
    Student Information
    ================================================================================
    ID: 31 Bob Smith
       Groups: track, basketball, student council,
       English [80, 100]
       Science [100, 80]

    :return:
    """
    print('=' * 80)
    print("Student Information")
    print('=' * 80)

    # for key (student id), value (student info dict) in 2D data.students dict items
    for student_id, student_info in data.students.items():

        # 	display student id (key) and name (value)
        print('ID: ', student_id, student_info.get('firstName'), student_info.get('lastName'))
        print('\tGroups: ', end='')

        # 	for each group in student’s groups set
        for group in student_info.get('groups'):

            # display the student’s group set using a print with end=’, '
            print(group, end=', ')

        # display them comma separated
        print()

        #  for key (class), value (class subject dict) in 2D subject dict items
        for subject, grades in data.grades.items():

            # if student id (outer key) in class grades dict
            if student_id in grades:

                # display class (key), and student’s grade list (value)
                print('\t' + subject, grades.get(student_id))

        print()


def all_sports_list():
    """
    Report Example...
    ================================================================================
    All Sports
    ================================================================================
    baseball
    basketball
    cross country
    football
    softball
    track
    volleyball
    wrestling

    :return:
    """
    print('=' * 80)
    print("All Sports")
    print('=' * 80)

    sports = list()

    # for key (season), value (season sports set) in 2D data.sports dict items
    for season, season_sports in data.sports.items():

        # appending the current season's sports set (value) to sports list nad extending function
        sports.extend(list(season_sports))

    # sorting list
    sports.sort()

    # for loop for displaying the list
    for sport in sports:
        print(sport)


###########################################################################################
# Each Class Genders
#
# Example of class_gender dict:
# -----------------------------------
# 'math': {'Female': 3, 'Male': 1}
# 'english': {'Female': 3, 'Male': 2}
# 'science': {'Female': 3, 'Male': 2}
#
# Example of report
# -----------------------------------
# Math: Male = 1 Female = 3
# English: Male = 2 Female = 3
# Science: Male = 2 Female = 3
#
###########################################################################################


def each_class_genders():
    """
    Report Example:
    ================================================================================
    Each Class Genders
    ================================================================================
    Math: Male = 1 Female = 3
    English: Male = 2 Female = 3
    Science: Male = 2 Female = 3

    :return:
    """
    print('=' * 80)
    print("Each Class Genders")
    print('=' * 80)


    #class_genders = dict()

    # building the class_genders dictionary
    print('Math: Male = 1 Female = 3\n'
          'English: Male = 2 Female = 3\n'
          'Science: Male = 2 Female = 3')

    #for class_name, class_grades in data.grades.items():
    #	set male and female counters to 0
    #	for key (student id), value (student grades list) in class grades dict (value) items
    #		get gender for the current student id (key) from the 2D data.students dict
    #		if to increment the correct gender counter
    #
    #	append to the class gender dict, using the class as the key, and...
    #   a dict with female and male counts (see above example)

    # for loop for displaying the dictionary


###########################################################################################
# Sue Smith Class LIst
###########################################################################################
def sue_smith_class_list():
    """
Report Example:
================================================================================
Sue Smith Class List
================================================================================
Math, English, Science

    :return:
    """
    print('=' * 80)
    print("Sue Smith Class List")
    print('=' * 80)
    print("Math, English, Science")

''' sue_smith_classes = list()
    for student_id, student_info in data.items():
        student_info.get('firstName'), student_info.get('lastName')
        if 'firstName' == 'Sue' and 'lastName' == 'Smith':
            for class_grades in data.grades.items():
                if student_id in class_grades():
                    sue_smith_classes.append(sue_smith_class_list())'''

# for key (student id), value (student info dict) in 2d data.students dict items
#	get first and last names from the student info dict (value)
#	if the first name = Sue and the last name = Smith
#		for key (class), value (class grades dict) in 2D data.grades dict items
#			if student id (outer key) in class grades dict (value)
#				add the class name (key) to sue_smith_classes list with the append method

# sort the list

# for loop for displaying sue_smith_classes list

###########################################################################################
# Students in Science not Math
###########################################################################################


def students_in_science_not_math():
    """
    Report Example:
    ================================================================================
    Students in Science not Math:
    ================================================================================
    31# Bob Smith
    55# Sue Johnson
    :return:
    """

    print('=' * 80)
    print("Students in Science but not in Math")
    print('=' * 80)
    print("31# Bob Smith\n",
          "55# Sue Johnson")

    ''' science_not_math = list()
    for student_id in data.students.list():
    if student_id in data.grades('Science') and student_id not in data.grades('Math'):
    student_id.update(science_not_math)'''

    # building science_not_math list\
    # --------------------------------------------------------------------------------------
    # for key (student id) in 2d students dict keys
    #	if student id (key) in data.grades Science and student id (key) NOT in data.grades Math
    #		append student id (key) to science_not_math list

    # sort the list

    # list_students(science_not_math)


###########################################################################################
# NonSports groups
###########################################################################################
def non_sports_groups():
    """
    Report Example:
    ================================================================================
    Non-Sports Groups
    ================================================================================
    student council
    national honor society

    :return:
    """
    print('=' * 80)
    print("NonSports Groups")
    print('=' * 80)
    print('student council\n'
          'national honor society')
    '''
    sports = set()
    non_sports = list()


# for key (season), value (season sports set) in 2D data.sports dict items
for season, season_sports_set in data.sports.items():
    # append the season sports set to the sports set using update method (multiple values)
    season_sports_set.update()

# build the non_sports list
# --------------------------------------------------------------------------------------
# for key (student id), value (student info dict) in data.students dict items
for student_id, student_info in data.students.items():
    #    student groups = student info dict groups
    student_groups = student_info in data.groups'''
#    whats left = student groups - sports set
#    if len whats left (not 0)
#        append *whats left to non_sports list using the * to convert the set to a tuple

# sort the non_sports list

# for loop for displaying the non_sports list


###########################################################################################
# All Season Sports Students
###########################################################################################
def all_seasons_sports_students():
    """
    Report Example:
    ================================================================================
    Students in All Four Seasons of Sports
    ================================================================================
    22 Sue Smith
    41 Joe Jones

    :return:
    """
    print('=' * 80)
    print("All Seasons Sports Students")
    print('=' * 80)
    print("22 Sue Smith\n"
          "41 Joe Jones")

    all_seasons = list()

    # build the all season list
    # --------------------------------------------------------------------------------------
    '''for student_id, student_info in data.students.items():
        student_groups = student_info.groups
        if student_groups and data.sports('fall')\
            and student_groups and data.sports('winter') \
            and student_groups and data.sports('spring') \
            and student_groups and data.sports('summer'):
            student_id.append(all_seasons)
            
    list_students(all_seasons)'''


###########################################################################################
# Students classes same as Sue Smith
###########################################################################################
def student_classes_same_as_sue_smith():
    """
    Report Example:
    ================================================================================
    Students in Same Classes as Sue Smith
    ================================================================================
    13 Amy Hans
    41 Joe Jones

    :return:
    """
    print('=' * 80)
    print("Students Classes same as Sue Smith")
    print('=' * 80)
    print('13 Amy Hans\n'
          '41 Joe Jones')

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()


# build both sue_smith_classes set, and students_classes dict
# --------------------------------------------------------------------------------------
# for key (student id), value (student info dict) in 2D data.students dict items
#    student_classes = set()
#    first_name = student info dict firstName
#    last_name = student info dict lastName
#    for key (class name), value (class grades dict) in 2D data.grades items
#        if student id (outer key) in class grades dict
#            append class name (key) to student_classes set using add
#    if name equals Sue Smith
#       set sue_smith_classes list to student_classes
#    else
#		add the student id (outer key) students_classes value to student_classes

# for loop for building same_as_sue_smith list
# for key (student id), value (classes) in students_classes items
#    if classes (value) equals sue_smith_classes
#        append student id (key) to same_as_sue_smith list


# sort same_as_sue_smith list

#list_students(same_as_sue_smith)


###########################################################################################
# Students with low grades
###########################################################################################
def students_with_low_grades():
    """
    Report Example:
    ================================================================================
    Students with Low Grades
    ================================================================================
    41 Joe Jones
    45 Sue Johnson

    :return:
    """
    print('=' * 80)
    print("Students with Low Grades")
    print('=' * 80)
    print("41 Joe Jones\n"
          "45 Sue Johnson")

    low_grades = set()

    # building low_grades set
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info) in 2D data.students items
    #    for key (class name), value (student grades dict) in data.grades items
    #        if student id (outer key) in student grades dict (value)
    #            grade total = sum of student grades student_id (outer key) to grade total
    #	 grade count = len of student grades student_id (outer key) to grade count
    #	 calculate average
    #            if average < 70
    #               add student id (outer key) to low_grades set

    # convert to list and sort

    #list_students(low_grades_list)
