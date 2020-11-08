from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from forms import SurveyForm
import api
import ast


bp = Blueprint('frontend', __name__, url_prefix='/')

model = api.start_model()

personas = [
    {'id': 0,
     'name': 'Explorer',
     'quote': 'Will I fit in? Will I like it?',
     'description': 'They look for various opportunities to grow personally and professionally.',
     'score': -3,  # -3.0174488461982596
     'evidence': {'Satisfaction': {'satQ': 0, 'satW': 0},
                  'Opportunities': {'oppQ': 0, 'oppW': 1},
                  'Finance': {'finQ': 2, 'finW': 1},
                  'Skills': {'skiQ': 2, 'skiW': 0},
                  'Improvement': {'impQ': 1, 'impW': 0},
                  'WorklifeBalance': {'wlbQ': 1, 'wlbW': 1}},
     'priors': {'Satisfaction': 0.78,
                'Opportunities': 0.87,
                'Finance': 0.4,
                'Skills': 0.26,
                'Improvement': 0.59,
                'WorklifeBalance': 0.73}},
    {'id': 1,
     'name': 'Achiever',
     'score': 2.1,  # 2.1488448169595342
     'evidence': {'Satisfaction': {'satQ': 2, 'satW': 1},
                  'Opportunities': {'oppQ': 1, 'oppW': 0},
                  'Finance': {'finQ': 0, 'finW': 1},
                  'Skills': {'skiQ': 2, 'skiW': 1},
                  'Improvement': {'impQ': 1, 'impW': 1},
                  'WorklifeBalance': {'wlbQ': 3, 'wlbW': 1}},
     'quote': 'Will I make a difference?',
     'description': 'Their contributions towards the society would make them feel proud of their career.',
     'priors': {'Satisfaction': 0.40,
                'Opportunities': 0.59,
                'Finance': 0.87,
                'Skills': 0.40,
                'Improvement': 0.73,
                'WorklifeBalance': 0.21}},
    {'id': 2,
     'name': 'Apprentice',
     'score': -1.5,  # -1.5189583104819226
     'evidence': {'Satisfaction': {'satQ': 1, 'satW': 1},
                  'Opportunities': {'oppQ': 2, 'oppW': 1},
                  'Finance': {'finQ': 1, 'finW': 0},
                  'Skills': {'skiQ': 2, 'skiW': 0},
                  'Improvement': {'impQ': 1, 'impW': 0},
                  'WorklifeBalance': {'wlbQ': 0, 'wlbW': 1}},
     'quote': 'Will I feel satisfied?',
     'description': 'They like getting insights from knowledgeable people to make career decisions.',
     'priors': {'Satisfaction': 0.73,
                'Opportunities': 0.4,
                'Finance': 0.59,
                'Skills': 0.26,
                'Improvement': 0.59,
                'WorklifeBalance': 0.87}}
]


"""
Function for rendering the personas homepage
Redirects to the questions page if a persona is selected
"""
@bp.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_persona_id = int(request.args.get('user_persona_id'))

        return redirect(url_for('frontend.questions_page', user_persona_id=user_persona_id))

    return render_template("personas.html", personas=personas)


"""
Function for rendering the questions wizard
Build an evidence object from the user responses
Redirects to the result page if all questions are answered
"""
@bp.route("/questions", methods=['GET', 'POST'])
def questions_page():
    submit_form = SurveyForm()
    user_persona_id = int(request.args.get('user_persona_id'))

    if submit_form.validate_on_submit():
        forms = [submit_form.sat, submit_form.wlb, submit_form.opp, submit_form.ski, submit_form.fin, submit_form.imp]
        evidence = {}
        for f in forms:
            evidence[f.form_name] = {f.answer.label.text: f.answer.data, f.weight.label.text: f.weight.data}

        return redirect(url_for('frontend.result_page', evidence=evidence, user_persona_id=user_persona_id))

    return render_template("questions.html", submit_form=submit_form, user_persona_id=user_persona_id)


"""
Function for rendering the result page
"""
@bp.route("/result", methods=['GET', 'POST'])
def result_page():
    user_persona = personas[int(request.args.get('user_persona_id'))]
    evidence = ast.literal_eval(request.args.get('evidence'))
    variables = ['Satisfaction', 'Opportunities', 'Finance', 'Skills', 'Improvement', 'WorklifeBalance']

    chart_data = get_chart_data(variables, evidence, user_persona)

    final_score = compute_score(evidence)

    return render_template("result.html", chart=chart_data, variables=variables, score=final_score,
                           persona=user_persona)


"""
Helper function for creating the radar chart data
Calls api to perform inference on the Bayesian model
"""
def get_chart_data(variables, evidence, persona):
    chart_data = {'user_values': {},
                  'persona': {}}

    for var in variables:
        response = api.do_inference(model, [var], evidence[var])
        chart_data['user_values'][response.json['variables'][0]] = response.json['values'][1]*10
        chart_data['persona'][var] = persona['priors'][var]*10

    return chart_data


"""
Helper function for computing the scores
Calls api to perform inference for the score nodes
"""
def compute_score(evidence):
    score_variables = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']
    score_evidence = {'S1': ['Satisfaction', 'WorklifeBalance'],
                      'S2': ['Satisfaction', 'Opportunities'],
                      'S3': ['WorklifeBalance', 'Opportunities'],
                      'S4': ['Skills', 'Finance'],
                      'S5': ['Skills', 'Improvement'],
                      'S6': ['Finance', 'Improvement']}
    score_data = {}
    for v in score_variables:
        evid = {}
        for e in score_evidence[v]:
            evid.update(evidence[e])
        result = api.do_inference(model, [v], evid)
        score_data[result.json['variables'][0]] = result.json['values'][1]

    sub_sc = (score_data['S1'] + score_data['S2'] + score_data['S3'])/3
    obj_sc = (score_data['S4'] + score_data['S5'] + score_data['S6'])/3

    final_score = -sub_sc + obj_sc

    return round(final_score*10, 1)
