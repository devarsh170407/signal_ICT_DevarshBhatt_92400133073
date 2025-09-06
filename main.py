import numpy as np
from signal_ICT_DevarshBhatt_92400133073 import unitary_signals, trigonometric_signals, operations
n = np.arange(-10, 10)
unit_step_signal = unitary_signals.unit_step(n)
unit_impulse_signal = unitary_signals.unit_impulse(n)
ramp = unitary_signals.ramp_signal(n)
t = np.linspace(0, 1, 500)
sine = trigonometric_signals.sine_wave(2, 5, 0, t)
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
exponential = trigonometric_signals.exponential_signal(2, 5, t)
shifted_sine = operations.time_shift(sine, 5)
scale_sine = operations.time_scale(sine, 5)
added_signal = operations.signal_addition(unit_step_signal, ramp)
multiplied_signal = operations.signal_multiplication(sine, cosine)