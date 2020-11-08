from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination


class CareerNet:

    model = BayesianModel()

    def __init__(self):
        self.build_net()
        self.add_cpds()

    def build_net(self):
        self.model.add_nodes_from(['Improvement', 'Opportunities', 'Satisfaction',
                                   'Skills', 'Finance', 'WorklifeBalance'])

        # model.add_edges_from([('a', 'b')])
        # a->b; a is the parent of b
        self.model.add_edges_from([('Improvement', 'impQ'), ('Improvement', 'impW'),
                                  ('Opportunities', 'oppQ'), ('Opportunities', 'oppW'),
                                  ('Satisfaction', 'satQ'), ('Satisfaction', 'satW'),
                                  ('Skills', 'skiQ'), ('Skills', 'skiW'),
                                  ('Finance', 'finQ'), ('Finance', 'finW'),
                                  ('WorklifeBalance', 'wlbQ'), ('WorklifeBalance', 'wlbW')])

        self.model.add_edges_from([('Satisfaction', 'S1'),
                                  ('WorklifeBalance', 'S1'),
                                  ('Satisfaction', 'S2'),
                                  ('Opportunities', 'S2'),
                                  ('WorklifeBalance', 'S3'),
                                  ('Opportunities', 'S3'),
                                  ('Skills', 'S4'),
                                  ('Finance', 'S4'),
                                  ('Skills', 'S5'),
                                  ('Improvement', 'S5'),
                                  ('Finance', 'S6'),
                                  ('Improvement', 'S6')])

    def add_cpds(self):
        cpd_sat = TabularCPD('Satisfaction', 2, [[1/2],   # negative
                                                 [1/2]])  # positive, i.e. chart_value = P(Satisfaction=positive)
        cpd_wlb = TabularCPD('WorklifeBalance', 2, [[1/2], [1/2]])
        cpd_fin = TabularCPD('Finance', 2, [[1/2], [1/2]])
        cpd_opp = TabularCPD('Opportunities', 2, [[1/2], [1/2]])
        cpd_imp = TabularCPD('Improvement', 2, [[1/2], [1/2]])
        cpd_ski = TabularCPD('Skills', 2, [[1/2], [1/2]])

        #                                  imp0  imp1
        cpd_impW = TabularCPD('impW', 2, [[0.58, 0.42],   # False
                                          [0.42, 0.58]],  # True
                              evidence=["Improvement"],
                              evidence_card=[2])

        cpd_oppW = TabularCPD('oppW', 2, [[0.58, 0.42],
                                          [0.42, 0.58]],
                              evidence=["Opportunities"],
                              evidence_card=[2])

        cpd_skiW = TabularCPD('skiW', 2, [[0.58, 0.42],
                                          [0.42, 0.58]],
                              evidence=["Skills"],
                              evidence_card=[2])

        cpd_finW = TabularCPD('finW', 2, [[0.58, 0.42],
                                          [0.42, 0.58]],
                              evidence=["Finance"],
                              evidence_card=[2])

        cpd_wlbW = TabularCPD('wlbW', 2, [[0.58, 0.42],
                                          [0.42, 0.58]],
                              evidence=["WorklifeBalance"],
                              evidence_card=[2])

        cpd_satW = TabularCPD('satW', 2, [[0.58, 0.42],
                                          [0.42, 0.58]],
                              evidence=["Satisfaction"],
                              evidence_card=[2])

        #                                  sat0  sat1
        cpd_satQ = TabularCPD('satQ', 4, [[0.09, 0.46],   # Strongly agree
                                          [0.15, 0.30],   # Agree
                                          [0.30, 0.15],   # Disagree
                                          [0.46, 0.09]],  # Strongly disagree
                              evidence=['Satisfaction'],
                              evidence_card=[2])

        cpd_wlbQ = TabularCPD('wlbQ', 4, [[0.09, 0.46],
                                          [0.15, 0.30],
                                          [0.30, 0.15],
                                          [0.46, 0.09]],
                              evidence=['WorklifeBalance'],
                              evidence_card=[2])

        cpd_oppQ = TabularCPD('oppQ', 4, [[0.09, 0.46],
                                          [0.15, 0.30],
                                          [0.30, 0.15],
                                          [0.46, 0.09]],
                              evidence=['Opportunities'],
                              evidence_card=[2])

        cpd_skiQ = TabularCPD('skiQ', 4, [[0.09, 0.46],
                                          [0.15, 0.30],
                                          [0.30, 0.15],
                                          [0.46, 0.09]],
                              evidence=['Skills'],
                              evidence_card=[2])

        cpd_finQ = TabularCPD('finQ', 4, [[0.09, 0.46],
                                          [0.15, 0.30],
                                          [0.30, 0.15],
                                          [0.46, 0.09]],
                              evidence=['Finance'],
                              evidence_card=[2])

        cpd_impQ = TabularCPD('impQ', 4, [[0.09, 0.46],
                                          [0.15, 0.30],
                                          [0.30, 0.15],
                                          [0.46, 0.09]],
                              evidence=['Improvement'],
                              evidence_card=[2])

        #                                 sat0     sat1
        #                              wlb0 wlb1 wlb0 wlb1
        cpd_s1 = TabularCPD('S1', 2, [[0.9, 0.5, 0.5, 0.1],   # no_value
                                      [0.1, 0.5, 0.5, 0.9]],  # value, i.e. score = P(S1=1)
                            evidence=['Satisfaction', 'WorklifeBalance'],
                            evidence_card=[2, 2])

        cpd_s2 = TabularCPD('S2', 2, [[0.9, 0.5, 0.5, 0.1],
                                      [0.1, 0.5, 0.5, 0.9]],
                            evidence=['Satisfaction', 'Opportunities'],
                            evidence_card=[2, 2])

        cpd_s3 = TabularCPD('S3', 2, [[0.9, 0.5, 0.5, 0.1],
                                      [0.1, 0.5, 0.5, 0.9]],
                            evidence=['WorklifeBalance', 'Opportunities'],
                            evidence_card=[2, 2])

        cpd_s4 = TabularCPD('S4', 2, [[0.9, 0.5, 0.5, 0.1],
                                      [0.1, 0.5, 0.5, 0.9]],
                            evidence=['Skills', 'Finance'],
                            evidence_card=[2, 2])

        cpd_s5 = TabularCPD('S5', 2, [[0.9, 0.5, 0.5, 0.1],
                                      [0.1, 0.5, 0.5, 0.9]],
                            evidence=['Skills', 'Improvement'],
                            evidence_card=[2, 2])

        cpd_s6 = TabularCPD('S6', 2, [[0.9, 0.5, 0.5, 0.1],
                                      [0.1, 0.5, 0.5, 0.9]],
                            evidence=['Finance', 'Improvement'],
                            evidence_card=[2, 2])

        self.model.add_cpds(cpd_impQ, cpd_satQ, cpd_skiQ, cpd_finQ, cpd_wlbQ, cpd_oppQ,
                            cpd_impW, cpd_satW, cpd_skiW, cpd_finW, cpd_wlbW, cpd_oppW,
                            cpd_sat, cpd_wlb, cpd_fin, cpd_imp, cpd_opp, cpd_ski,
                            cpd_s1, cpd_s2, cpd_s3, cpd_s4, cpd_s5, cpd_s6)

    def get_model(self):
        return self.model


def do_var_elim(model, variables, evidence):
    inference = VariableElimination(model)

    return inference.query(variables=variables, evidence=evidence)


def update_cpd(model, variable, posterior):
    new_cpd = TabularCPD(variable, 2, [[1-posterior], [posterior]])
    model.add_cpds(new_cpd)

    return model
