import scipy.stats
import streamlit as st
import time

st.header('Lanzar una moneda')

# Reserva un espacio para mostrar y actualizar el gráfico
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

        # Guarda la nueva media y actualiza el mismo gráfico
        means.append(mean)
        chart.line_chart(means)

        time.sleep(0.05)

    return mean


number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

    final_mean = toss_coin(number_of_trials)

    st.write(f'Proporción final de caras: {final_mean:.2%}')