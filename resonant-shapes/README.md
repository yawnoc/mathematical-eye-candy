# Resonant shapes

Here we use solutions to the wave equation for an oscillating square boundary
to obtain new boundary shapes that have the same resonant frequency.

**Warning: Infinite and infinitesimal quantities are used in this document.**


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

### Scaling

For more wieldiness, we put

```math
\begin{align}
  & u = u_0 \hat{u}, \quad v = u_0 \hat{v} \\
  & x = a \hat{x}, \quad y = a \hat{y} \\
  & \omega/c = (\pi/a) \hat{\omega} \\
  & c t = a \hat{t},
\end{align}
```

so that in dimensionless variables the solution becomes

```math
  \hat{v} =
    \sum_{\substack{m = 1 \\ \text{$m$ odd}}}^\infty
    \frac{4}{m \pi}
    \left(
      \sin(m \pi \hat{x}) \frac{\hat{Y}(\hat{y}) + \hat{Y}(1 - \hat{y})}{\hat{Y}(1)}
        +
      \sin(m \pi \hat{y}) \frac{\hat{Y}(\hat{x}) + \hat{Y}(1 - \hat{x})}{\hat{Y}(1)}
    \right),
```

where

```math
\begin{align}
  \hat{Y}(\hat{y})
  &= \sinh \left( \sqrt{m^2 - \hat{\omega}^2} \cdot \pi \hat{y} \right) \\
  &= \mathrm{i} \sin \left( \sqrt{\hat{\omega}^2 - m^2} \cdot \pi \hat{y} \right).
\end{align}
```

### Resonance

A necessary condition for resonance is that the common denominator $\hat{Y}(1)$ vanishes,
i.e.

```math
  \mathrm{i} \sin \left( \sqrt{\hat{\omega}^2 - m^2} \cdot \pi \right) = 0,
```

and hence that $\hat{\omega}^2 = m^2 + n^2$ for some integer $n$.

If $n$ be even, we have

```math
  \frac{\hat{Y}(\hat{y}) + \hat{Y}(1 - \hat{y})}{\hat{Y}(1)}
  = \frac{\sin(n \pi \hat{y}) + \sin(n \pi (1 - \hat{y}))}{\sin(n \pi)}
  = \frac{0}{0},
```

and upon resolving the indeterminacy (by taking derivatives with respect to $n \pi$)
this reduces to

```math
\begin{align}
  \frac{\hat{Y}(\hat{y}) + \hat{Y}(1 - \hat{y})}{\hat{Y}(1)}
  &= \frac{\hat{y} \cos(n \pi \hat{y}) + (1 - \hat{y}) \cos(n \pi (1 - \hat{y}))}{\cos(n \pi)} \\
  &= \cos(n \pi \hat{y}),
\end{align}
```

which is assuredly finite. Thus there is *no* resonance for even $n$.

If $n$ be odd, we have

```math
  \frac{\hat{Y}(\hat{y}) + \hat{Y}(1 - \hat{y})}{\hat{Y}(1)}
  = \frac{\sin(n \pi \hat{y}) + \sin(n \pi (1 - \hat{y}))}{\sin(n \pi)}
  = \frac{2 \sin(n \pi \hat{y})}{\sin(n \pi)},
```

which is assuredly infinite.

Hence we have resonance if and only if

```math
  \hat{\omega}^2 = m^2 + n^2, \qquad \text{$m$, $n$ odd}.
```

See <<https://oeis.org/A097269>>.
