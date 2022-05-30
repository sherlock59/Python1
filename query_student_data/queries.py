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

    class_genders = dict()

    for class_name, class_grades in data.grades.items():
        # set male and female counters to 0
        male_counter = 0
        female_counter = 0

        # for key (student id), value (student grades list) in class grades dict (value) items
        for student_id, student_grades in class_grades.items():
            # getting gender for the current student id and increment the correct gender counter
            if data.students[student_id]['gender'].lower() == 'M'.lower():
                male_counter += 1
            elif data.students[student_id]['gender'].lower() == 'F'.lower():
                female_counter = 1

        # dict with female and male counts
        gender_counters = [male_counter, female_counter]

        # appending to the class gender dict, using the class as the key, and...
        class_genders.update({class_name: {'Male': male_counter, 'Female': female_counter}})

        # for loop for displaying the dictionary
    for class_name, gender_counters in class_genders.items():
        print(f"{class_name:<7s} Male = {gender_counters['Male']} -- Female = {gender_counters['Female']}")


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

    :return: None
    """
    print('=' * 80)
    print("Sue Smith Class List")
    print('=' * 80)

    sue_smith_classes = list()
    
    # for loop to 2d data dict items
    for student_id, student_info in data.students.items():
        
        # getting first and last name from student info dict
        first_name = student_info['firstName']
        last_name = student_info['lastName']
        
        # setting 
        if first_name.lower() == 'Sue'.lower() and last_name.lower() == 'Smith'.lower():
            # for class value in 2D format
            for clas, class_grades in data.grades.items():
                # if student id (outer key) in class grades' dict (value)
                if student_id in class_grades.keys():
                    # add the class name (key) to sue_smith_classes list with the append method
                    sue_smith_classes.append(clas)
      
    # sorting the list               
    sue_smith_classes.sort()

    # for loop for displaying sue_smith_classes list
    for clas in sue_smith_classes:
        if sue_smith_classes.index(clas) == len(sue_smith_classes) - 1:
            print(clas, end='')
        else:
            print(clas, end=',')
            
    print()


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

    science_not_math = list()

    # building science_not_math list
    for student_id in data.students.keys():
        if student_id in data.grades['Science'].keys() and student_id not in data.grades['Math'].keys():
            science_not_math.append(student_id)

    # sorting the list
    science_not_math.sort()

    # list_students(science_not_math)
    list_students(science_not_math)


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

    sports = set()
    non_sports = list()

    # for key (season), value (season sports set) in 2D data.sports dict items
    for season, season_sports in data.sports.items():
        # append the season sports set to the sports set using update method (multiple values)
        sports.update(list(season_sports))

    # build the non_sports list
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info dict) in data.students dict items
    for student_id, student_info in data.students.items():
        # student groups = student info dict groups
        student_groups = student_info['groups']
        whats_left = student_groups - sports

        if len(whats_left) != 0:
            non_sports.append(*whats_left)

    # sorting the non_sports list
    non_sports.sort()

    # for loop for displaying the non_sports list
    for sport in non_sports:
        print(sport)


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

    all_seasons = list()

    # building the all season list
    for student_id, student_info in data.students.items():
        student_groups = student_info['groups']

        if student_groups & data.sports['fall']\
                and student_groups & data.sports['winter'] \
                and student_groups & data.sports['spring'] \
                and student_groups & data.sports['summer']:
            all_seasons.append(student_id)

    # sorting the list
    all_seasons.sort()

    # listings
    list_students(all_seasons)


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

    :return: None
    """
    print('=' * 80)
    print("Students Classes same as Sue Smith")
    print('=' * 80)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()

    # build both sue_smith_classes set, and students_classes dict
    for student_id, student_info in data.students.items():
        student_classes_set = set()
        first_name = student_info['firstName']
        last_name = student_info['lastName']

        for class_name, class_grades in data.grades.items():
            if student_id in class_grades.keys():
                student_classes_set.add(class_name)

        if first_name == 'Sue' and last_name == 'Smith':
            sue_smith_classes = student_classes_set
        else:
            students_classes.update({student_id: student_classes_set})

    for student_id, classes in students_classes.items():
        if classes == sue_smith_classes:
            same_as_sue_smith.append(student_id)

    # sorting Sue Smith
    same_as_sue_smith.sort()

    # list_students same as Sue Smith
    list_students(same_as_sue_smith)


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

    low_grades = set()

    # building low_grades set
    for student_id, student_info in data.students.items():
        for class_name, student_grades in data.grades.items():
            if student_id in student_grades.keys():
                grade_total = sum(student_grades[student_id])
                grade_count = len(student_grades[student_id])

                # calculating average
                average = grade_total / grade_count
                if average < 70:
                    low_grades.add(student_id)

    # converting to list and sort
    low_grades_list = list(low_grades)
    low_grades_list.sort()

    list_students(low_grades_list)
