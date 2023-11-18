# Resonant shapes

Here we use solutions to the wave equation for an oscillating square boundary
to obtain new boundary shapes that have the same resonant frequency.


## Oscillating square solution

Let the region of said square be $0 \le x \le a$ and $0 \le y \le a$
(that is, having sidelength $a$), and let $u = u(x, y)$ denote the solution.

In the interior of the square we have the wave equation

```math
  \frac{\partial^2 u}{{\partial x}^2}
  + \frac{\partial^2 u}{{\partial y}^2}
  - \frac{1}{c^2} \frac{\partial^2 u}{{\partial t}^2}
    = 0,
```

where $c$ is the propagation speed,
and on the boundary of the square we have oscillation

```math
  u = u_0 \mathrm{e}^{\mathrm{i} \omega t},
```

where $u_0$ is the amplitude and $\omega$ is the angular frequency.
