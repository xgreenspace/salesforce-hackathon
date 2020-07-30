class Candidate():
    def __init__(self, name='', profile_link='', summary='', current_role=''):
        self.merit_points = 0
        self.is_good_hire = False

        self.name = name
        self.profile_link = profile_link
        self.summary = summary
        self.current_role = current_role

        