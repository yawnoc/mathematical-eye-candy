# Resonant shapes

Here we use solutions to the wave equation for an oscillating square boundary
to obtain new boundary shapes that have the same resonant frequency.


## Oscillating square solution

Let the region of said square be $0 \le x \le a$ and $0 \le y \le a$
(that is, having sidelength $a$), and let $u = u(x, y, t)$ denote the solution.

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

### Oscillations

Putting $u(x, y, t) = v(x, y) \mathrm{e}^{\mathrm{i} \omega t}$ to seek oscillations,
we have in the interior

```math
  \frac{\partial^2 v}{{\partial x}^2}
  + \frac{\partial^2 v}{{\partial y}^2}
  + \frac{\omega^2}{c^2} v
    = 0,
```

and on the boundary

```math
  v = u_0.
```

By linearity we may break $v$ into four pieces, each of which has $v = u_0$
on one of the sides of the square individually.
Following the usual separation of variables, we find that the piece
with $v = u_0$ along the top side $y = a$ is given by

```math
  v_\mathrm{top} =
    \sum_{\substack{m = 1 \\ \text{$m$ odd}}}^\infty
    \frac{4 u_0}{m \pi} \cdot \sin \left( \frac{m \pi x}{a} \right) \frac{Y(y)}{Y(a)},
```

where

```math
  Y(y) = \sinh \left( \sqrt{(m \pi/a)^2 - (\omega/c)^2} \cdot y \right).
```

Combining all four pieces, we get

```math
  v =
    \sum_{\substack{m = 1 \\ \text{$m$ odd}}}^\infty
    \frac{4 u_0}{m \pi}
    \left(
      \sin \left( \frac{m \pi x}{a} \right) \frac{Y(y) + Y(a - y)}{Y(a)}
        +
      \sin \left( \frac{m \pi y}{a} \right) \frac{Y(x) + Y(a - x)}{Y(a)}
    \right).
```
