from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, FormField


class Satisfaction(FlaskForm):
    form_name = 'Satisfaction'
    answer = RadioField('satQ', coerce=int, choices=[(0, "Strongly agree"),
                                                     (1, "Agree"),
                                                     (2, "Disagree"),
                                                     (3, "Strongly disagree")])
    weight = RadioField('satW', coerce=int, choices=[(0, "False"),
                                                     (1, "True")])


class Skills(FlaskForm):
    form_name = 'Skills'
    answer = RadioField('skiQ', coerce=int, choices=[(0, "Strongly agree"),
                                                     (1, "Agree"),
                                                     (2, "Disagree"),
                                                     (3, "Strongly disagree")])
    weight = RadioField('skiW', coerce=int, choices=[(0, "False"),
                                                     (1, "True")])


class Opportunities(FlaskForm):
    form_name = 'Opportunities'
    answer = RadioField('oppQ', coerce=int, choices=[(0, "Strongly agree"),
                                                     (1, "Agree"),
                                                     (2, "Disagree"),
                                                     (3, "Strongly disagree")])
    weight = RadioField('oppW', coerce=int, choices=[(0, "False"),
                                                     (1, "True")])


class Improvement(FlaskForm):
    form_name = 'Improvement'
    answer = RadioField('impQ', coerce=int, choices=[(0, "Strongly agree"),
                                                     (1, "Agree"),
                                                     (2, "Disagree"),
                                                     (3, "Strongly disagree")])
    weight = RadioField('impW', coerce=int, choices=[(0, "False"),
                                                     (1, "True")])


class Finance(FlaskForm):
    form_name = 'Finance'
    answer = RadioField('finQ', coerce=int, choices=[(0, "Strongly agree"),
                                                     (1, "Agree"),
                                                     (2, "Disagree"),
                                                     (3, "Strongly disagree")])
    weight = RadioField('finW', coerce=int, choices=[(0, "False"),
                                                     (1, "True")])


class WorklifeBalance(FlaskForm):
    form_name = 'WorklifeBalance'
    answer = RadioField('wlbQ', coerce=int, choices=[(0, "Strongly agree"),
                                                     (1, "Agree"),
                                                     (2, "Disagree"),
                                                     (3, "Strongly disagree")])
    weight = RadioField('wlbW', coerce=int, choices=[(0, "False"),
                                                     (1, "True")])


class SurveyForm(FlaskForm):
    sat = FormField(Satisfaction)
    ski = FormField(Skills)
    opp = FormField(Opportunities)
    imp = FormField(Improvement)
    wlb = FormField(WorklifeBalance)
    fin = FormField(Finance)

    submit = SubmitField('Submit')
