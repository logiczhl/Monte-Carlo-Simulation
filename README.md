## Code Methodology

For the city's emergency + routine disposal capacity table, the distribution of various scenarios is selected by combining GPT as well as historical a priori data, and the growth rates of multiple scenarios are simulated by using Monte Carlo Estimation, which ultimately results in the distribution and change of the city's load rate under different scenarios.

## Monte Carlo simulation

The calculation of load factor is carried out through the following formula

$$
L_F=\frac{(1+R)M_d}{C_D+E_D}
$$

The growth rates correspond to the following distribution depending on the city's coping strategies and scenarios

| Scenario category                            | Distribution type                  |
| -------------------------------------------- | ---------------------------------- |
| Ongoing closure - mild growth                | $R\sim N(\mu=0.5,\sigma=0.2)$    |
| Ongoing embargo - moderate growth            | $R\sim N(\mu=1,\sigma=0.4)$      |
| Continuation of the embargo - serious growth | $R\sim N(\mu=1.5,\sigma=0.6)$    |
| Immediate liberalisation - rapid growth      | $R\sim LN(\mu=\log2,\sigma=0.3)$ |
| Immediate liberalisation - slow growth       | $R\sim U(a=0,b=0.5)$             |
| Flexibility to adjust - gradual growth       | $R\sim N(\mu=0.75,\sigma=0.3)$   |
| Flexible Adjustment - Stabilisation          | $R\sim U(a=-0.1,b=0.1)$          |

Monte Carlo simulation based on the above table.
