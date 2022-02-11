import models

# For the check_salary method u should use \'y\' as an argument to check the salary from the 1st of month.
# Otherwise use a number of days to count.

if __name__ == '__main__':
    recruiter = models.Recruiter('Alexey', 1500)
    first_programmer = models.Programmer('Maria', 1800, ['JavaScript', 'MySQL', 'Python'])
    second_programmer = models.Programmer('Gleb', 1800, ['PostgreSQL', 'Python', 'Jango'])
    first_candidate = models.Candidate('Symere Woods', 'lilsymere@uzi.vert', ['Apache', 'MySQL', 'PHP'], 'PHP', 8)
    second_candidate = models.Candidate('Dexter Tiewon', 'famousdex@gmail.com', ['VHDL', 'Java'], 'Java', 10)
    third_candidate = models.Candidate('Jordan Carter', 'carti@gmail.com', ['VHDL', 'Java'], 'Java', 10)
    first_vacancy = models.Vacancy('Java Trainee', 'Java', '6' )
    second_vacancy = models.Vacancy('Middle Java Developer', 'Java', '8')

    