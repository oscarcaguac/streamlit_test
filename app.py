import pandas as pd
import scipy.stats
import streamlit as st
import time

# Crea el contador solo si todavía no existe en esta sesión
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

# Crea la tabla solo si todavía no existe en esta sesión
if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(
        columns=['no', 'iteraciones', 'media']
    )

st.header('Lanzar una moneda')

# Espacio donde se actualiza el gráfico
chart = st.empty()
chart.line_chart([0.5])


def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0
    means = [0.5]

    for r in trial_outcomes:
        outcome_no += 1

        if r == 1:
            outcome_1_count += 1

        mean = outcome_1_count / outcome_no
        means.append(mean)

        chart.line_chart(means)
        time.sleep(0.05)

    return mean


number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

    mean = toss_coin(number_of_trials)

    # Aumenta el número de experimentos completados
    st.session_state['experiment_no'] += 1

    # Añade una fila con el resultado del experimento
    results = st.session_state['df_experiment_results']

    results.loc[len(results)] = [
        st.session_state['experiment_no'],
        number_of_trials,
        mean
    ]

    st.write(f'Proporción final de caras: {mean:.2%}')

# Muestra el historial incluso cuando no se pulsa el botón
st.subheader('Resultados de los experimentos')
st.dataframe(st.session_state['df_experiment_results'])