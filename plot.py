import os
import pickle

from plotly.express import line_polar
import plotly.graph_objects as go
import pandas as pd

def min_max_normalize_tuple(l):
    ll = [x[1] for x in l]
    max_ = max(ll)
    min_ = min(ll)
    return [(x[0], (x[1] - min_) / (max_ - min_)) for x in l]

if __name__ == '__main__':
    """load each output and select top 10 model parameters"""

    num_param_top = 5
    path_output = os.path.abspath(os.path.dirname(__file__)) + '/data/output/'
    params = ['conc_inoc', 'V_inoc', 'V_seed', 'conc_seed', 'V_b',
        'concen_desired', 'm', 'f_ab', 'f_L', 't_m', 't_y', 'f_s', 'f_FM',
        'V_c', 'rho_c', 't_D', 'GCR_c', 'OUR_c', 'conc_aa2p', 'conc_nahco3',
        'conc_sodium', 'conc_insulin', 'conc_trans', 'conc_fgf2',
        'conc_tgfb', 'conc_glu', 'rho_m', 'f_O2', 'epsilon_bT', 'f_bT',
        'T_e', 'T_d', 'W_Cv', 'epsilon_Hm', 'h', 'epsilon_BR', 'ACBM_Cv',
        'T_b', 'T_c', 'epsilon_ACBMR', 'p_b', 'f_C', 'f_Sca', 'f_T', 'f_Q',
        'f_B', 'f_O', 'D_r', 'I_D', 'L_e', 'I_EQ', 'C_b', 'C_basel',
        'C_aa2p', 'C_nahco3', 'C_sodium', 'C_insulin', 'C_trans', 'C_fgf2',
        'C_tgfb', 'C_O2', 'C_NG', 'C_NGP', 'C_L', 'C_PW', 'C_WF', 'C_BO']
    filename_list = ['dgsm', 'sobol', 'delta', 'fast', 'morris', 'rbd_fast']
    key_list = ['vi', 'S1', 'S1', 'S1', 'mu_star', 'S1']

    # calculate sensitivity measures for each algorithm
    sm_mat = []
    for filename, key in zip(filename_list, key_list):
        output = pickle.load(open(path_output + filename + '.txt', 'rb'))
        output_sorted = sorted(zip(params, output[key]), key = lambda x: x[1],
            reverse = True)
        output_normalized = min_max_normalize_tuple(output_sorted)
        sm_mat.append(output_normalized)

    # extract top parameters for each SA algorithm, record appearing params
    params_recorded = []
    for sm_vec in sm_mat:
        params_recorded.extend([x[0] for x in sm_vec[:num_param_top]])
    params_recorded = set(params_recorded)

    # sort params by sobol sm to decrease spikes in spider plot
    params_tmp = []
    for param in params_recorded:
        params_tmp.append((param, dict(sm_mat[1])[param]))
    params_recorded = [p for p, _ in sorted(params_tmp,
        key = lambda x: x[1], reverse = True)]

    # extract appearing params sensitivity measure from each algorithm
    sm_top = []
    for sm_vec in sm_mat:
        sm_top_row = []
        for param in params_recorded:
            sm_top_row.append(dict(sm_vec)[param])
        sm_top.append(sm_top_row)

    # plotting
    algs = ['Derivative-based Global Sensitivity Measure (DGSM)',
        'Sobol Sensitivity Analysis (SSA)',
        'Delta Moment-Independent Measure (DMIM)',
        'Fourier Amplitude Sensitivity Test (FAST)',
        'Morris Method (MM)',
        'Random Balance Designs Fourier Amplitude Sensitivity Test (RBD-FAST)']
    params = ['Average single cell density (rho_c)',
        'Average single cell volume (V_c)',
        'Glucose concentration (conc_glu)',
        'Glucose consumption rate per cell (GCR_c)', 'FGF-2 cost (C_fgf2)',
        'FGF-2 concentration (conc_fgf2)', 'Maturation time (t_m)',
        'TGF-b concentration (conc_tgfb)',
        'Oxygen consumption rate per cell (OUR_c)']

    fig = go.Figure()
    for alg, sm_values in zip(algs, sm_top):
        fig.add_trace(
            go.Scatterpolar(
                r = sm_values,
                theta = params,
                fill = 'toself',
                name = alg))
    fig.update_layout(
        title = 'ACBM Sensitivity Analysis',
        font_size = 30,
        legend = dict(
            font = dict(
                size = 20),
            bordercolor = 'Black',
            borderwidth = 2),
        legend_title_text = 'Algorithm',
        legend_orientation = 'h')
    fig.show()