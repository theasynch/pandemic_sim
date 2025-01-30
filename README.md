# Pandemic Simulator 🦠

## Introduction
The **Pandemic Simulator** is a Python-based simulation that models the spread of infectious diseases using the **SIR (Susceptible-Infected-Recovered)** model. Built with **Pygame**, this project aims to visualize disease transmission, recovery, and mortality through interactive simulations. 🎮📊

## Features
- **SIR-based disease spread simulation** 🏥
- **Configurable population density and infection parameters**
- **Visible infection fields for infected individuals** 🔴
- **Dynamic movement and interaction of individuals** 🚶‍♂️
- **Live graph tracking infections, recoveries, and deaths** 📈
- **Adjustable recovery rate and mortality rate**

## Mathematical Model: SIR Algorithm
The simulation follows the standard **SIR Model** with the equations:

```math
\frac{dS}{dt} = -\beta S I
\frac{dI}{dt} = \beta S I - \gamma I
\frac{dR}{dt} = \gamma I
```

Where:
- **S** = Susceptible individuals
- **I** = Infected individuals 🤒
- **R** = Recovered individuals 💪
- **β (Beta)** = Infection rate
- **γ (Gamma)** = Recovery rate

## Installation 🛠️
To run this project, ensure you have Python installed along with the required dependencies:

```bash
pip install pygame matplotlib numpy
```

## Running the Simulator ▶️
Run the following command to start the simulation:

```bash
python pandemic_simulator.py
```

## Controls 🎛️
- **Press 'G'** to display the live graph of infections, recoveries, and deaths.
- **Press 'Q'** to quit the simulation.

## Future Enhancements 🚀
- Implement **vaccination and immunity** features. 💉
- Introduce **quarantine zones** to slow infection spread. 🚧
- Add **different disease strains** with varying infection rates. 🦠

## License 📜
This project is open-source and available under the **MIT License**.

## Contributors 🤝
Feel free to contribute to the project! Open an issue or submit a pull request on GitHub.

