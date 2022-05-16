# -*- coding: utf-8 -*-

"""
    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.
"""

#Read more here: https://www.qmunity.tech/tutorials/hello-world-in-qiskit

#TO INSTALL:
#pip3 install qiskit
#pip3 install matplotlib
#pip3 install pylatexenc

from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

print("Example!")
print("A classic computer only shows two states. A quantum computer shows various states.")
print("This is a simulator of quantum computer, that when running on classic computer, only show two states")

qr=QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)

circuit.draw()

circuit.h(qr[0])

circuit.draw(output='mpl')

circuit.cx(qr[0],qr[1])

circuit.draw(output='mpl')

circuit.measure(qr,cr)

circuit.draw(output='mpl')

backend = BasicAer.get_backend('qasm_simulator')
job = execute(circuit, backend)
plot_histogram(job.result().get_counts(circuit), color='midnightblue', title="New Histogram (Classic computers (2). Quantum computer (various))")

plt.show()
