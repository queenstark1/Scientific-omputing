# Task 20: Random Numbers and Monte Carlo Methods

## Objective
To estimate the probability of a network server becoming overloaded using random sampling and Monte Carlo simulation.

## Method
NumPy was used to generate random demand scenarios from a normal distribution with a mean demand of 850 units and a standard deviation of 120 units. The server capacity was set to 1,000 units.

Each simulation was classified as overloaded if its demand exceeded the capacity. The estimated overload probability was calculated by dividing the number of overloaded cases by the total number of simulations. A fixed random seed of 42 was used to make the results reproducible.

## Results
With 100,000 simulations, 10,616 cases exceeded the server capacity, producing an estimated overload probability of 10.6160%.

The number of simulations was then increased to 500,000. In this experiment, 52,932 cases exceeded capacity, producing an estimated overload probability of 10.5864%.

## Discussion
Increasing the number of simulations from 100,000 to 500,000 changed the estimated probability from 10.6160% to 10.5864%. This illustrates how Monte Carlo estimates can vary with random sampling while generally becoming more stable as the number of simulations increases.

The result depends on the assumed normal distribution and the selected demand parameters. It should therefore be interpreted as a model-based estimate rather than a guarantee of real-world server performance.

## Graph
The convergence graph is saved as `plots/Task_20_monte_carlo.png`. It shows how the estimated overload probability changes as more simulations are included.

## Conclusion
Monte Carlo simulation provides a practical way to estimate risks when demand is uncertain. It can support capacity planning by estimating the likelihood that demand will exceed available server capacity.
