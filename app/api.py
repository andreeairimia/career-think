from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
)
import json
from model import do_var_elim
from model import CareerNet as network

bp = Blueprint('network', __name__, url_prefix='/net-api')


@bp.route('/health', methods=['GET'])
def health_check():
    data = {
        'hello': 'world'
    }

    return Response(json.dumps(data), status=200, mimetype='application/json')


def start_model():
    return network().get_model()


def do_inference(model, variables, evidence):
    result = do_var_elim(model, variables, evidence)

    inference_data = {'variables': list(result.variables),
                      'values': list(result.values)}
    resp_js = json.dumps(inference_data)

    return Response(resp_js, status=200, mimetype='application/json')
