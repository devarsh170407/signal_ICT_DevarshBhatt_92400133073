import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_DevarshBhatt_92400133073 import unitary_signal as us
from signal_ICT_DevarshBhatt_92400133073 import trigonometric_signal as ts
from signal_ICT_DevarshBhatt_92400133073 import operations as op

n = np.arange(-10,10,1)
t = np.linspace(0,1,1000)

unitstepsignal = us.unit_step(n)
unitimpulsesignal = us.unit_impulse(n)

sine = ts.sine_wave(2,5,0,t)

shifted_sine = op.time_shift(sine, 50)
plt.plot(t,sine, label = "ORIGINAL SINE")
plt.plot(t,shifted_sine, label = "SINE +5")
plt.legend()
plt.title("TIME SHIFTED SINE")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()
plt.show()

ramp = us.ramp_signal(n)
added_signal = op.signal_addition(unitstepsignal,ramp)
plt.stem(n,added_signal, basefmt= " ")
plt.title("UNIT STEP+RAMP")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

cosine = ts.cosine_wave(2,5,0,t)
multiply_signal = op.signal_multiplication(sine,cosine)
plt.plot(t,multiply_signal)
plt.title("SINE - COSINE")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()
plt.show()
