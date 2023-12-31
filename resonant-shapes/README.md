# Resonant shapes

Here we use solutions to the wave equation for an oscillating square boundary
to obtain new boundary shapes that have the same resonant frequency.

**Warning: The following content contains infinite and infinitesimal quantities.**
Reader discretion is advised.


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

### Separation of variables

Putting

```math
  u(x, y, t) = v(x, y) \mathrm{e}^{\mathrm{i} \omega t}
```

to seek oscillations, we have in the interior

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
Following the usual separation of variables in $x$ and $y$, we find that the piece
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

### Resonant frequency

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

### Resonant amplitude

To see the form of the amplitude increase during resonance,
we make a change of coordinates to the new dependent variable

```math
\begin{align}
  \xi(x, y, t)
  &= u(x, y, t) - u_0 \mathrm{e}^{\mathrm{i} \omega t}, \\
  &= (v(x, y) - u_0) \mathrm{e}^{\mathrm{i} \omega t}
\end{align}
```

or, in scaled terms (with $\xi = u_0 \hat{\xi}$),

```math
  \hat{\xi}(\hat{x}, \hat{y}, \hat{t})
  = (\hat{v}(\hat{x}, \hat{y}) - 1) \mathrm{e}^{\mathrm{i} \pi \hat{\omega} \hat{t}},
```

so that the non-homogeneity is moved from the oscillating boundary condition
into an oscillating forcing term in the field equation.
That is, in the interior of the square we have the inhomogeneous wave equation

```math
  \frac{\partial^2 \hat{\xi}}{{\partial \hat{x}}^2}
  + \frac{\partial^2 \hat{\xi}}{{\partial \hat{y}}^2}
  - \frac{\partial^2 \hat{\xi}}{{\partial \hat{t}}^2}
  + \pi^2 \hat{\omega}^2 \mathrm{e}^{\mathrm{i} \pi \hat{\omega} \hat{t}}
    = 0,
```

and on the boundary of the square we simply have

```math
  \hat{\xi} = 0.
```

To obtain a particular solution to the inhomogeneous wave equation at resonance,
we expand $\hat{v}(\hat{x}, \hat{y}) \mathrm{e}^{\mathrm{i} \pi \hat{\omega} \hat{t}}$ about the resonant frequency.
Keeping only the terms in the summation pertaining to $\hat{\omega}^2 = m^2 + n^2$,
we have the particular solution

```math
  \hat{\xi}_\mathrm{p}
  =
    \frac{4}{m \pi}
    \left(
      \sin(m \pi \hat{x}) \frac{\hat{Y}(\hat{y}) + \hat{Y}(1 - \hat{y})}{\hat{Y}(1)}
        +
      \sin(m \pi \hat{y}) \frac{\hat{Y}(\hat{x}) + \hat{Y}(1 - \hat{x})}{\hat{Y}(1)}
    \right)
    \mathrm{e}^{\mathrm{i} \pi \hat{\omega} \hat{t}}
```

to be evaluated at

```math
  \hat{\omega}^2 = m^2 + (n + \epsilon)^2,
```

where $\epsilon$ is infinitesimal, modulo homogeneous terms $\hat{\xi}_\mathrm{h}$.

In particular,

```math
\begin{align}
  \frac{\hat{Y}(\hat{y}) + \hat{Y}(1 - \hat{y})}{\hat{Y}(1)} \mathrm{e}^{\mathrm{i} \pi \hat{\omega} \hat{t}}
  &=
    \frac{\sin((n + \epsilon) \pi \hat{y}) + \sin((n + \epsilon) \pi (1 - \hat{y}))}{\sin((n + \epsilon) \pi)}
      \cdot
    \exp \left( \mathrm{i} \pi \sqrt{m^2 + (n + \epsilon)^2} \cdot \hat{t} \right) \\
  &=
    \left(
      \frac{-2 \sin(n \pi \hat{y})}{\epsilon \pi}
      + (1 - 2 \hat{y}) \cos(n \pi \hat{y})
      - \frac{2 \mathrm{i} n \hat{t} \sin(n \pi \hat{y})}{\sqrt{m^2 + n^2}}
    \right)
    \exp \left( \mathrm{i} \pi \sqrt{m^2 + n^2} \cdot \hat{t} \right) \\
  &\equiv
    \mathrm{const} \cdot \hat{t} \sin(n \pi \hat{y})
    \exp \left( \mathrm{i} \pi \sqrt{m^2 + n^2} \cdot \hat{t} \right)
    \pmod{\hat{\xi}_\mathrm{h}},
\end{align}
```

wherefore

```math
  \hat{\xi}_\mathrm{p}
  \equiv
    \mathrm{const}
      \cdot
    \Bigl(
      \sin(m \pi \hat{x}) \sin(n \pi \hat{y})
        +
      \sin(n \pi \hat{x}) \sin(m \pi \hat{y})
    \Bigr)
      \cdot
    \hat{t}
    \exp \left( \mathrm{i} \pi \sqrt{m^2 + n^2} \cdot \hat{t} \right)
    \pmod{\hat{\xi}_\mathrm{h}}.
```

Thus the amplitude increases linearly with time at resonance.


## New boundary shapes

To obtain new shapes that share the resonant frequency $\hat{\omega}^2 = m^2 + n^2$,
simply trace out boundaries along the contours $\hat{\xi}_\mathrm{p} = 0$, i.e.

```math
  \sin(m \pi \hat{x}) \sin(n \pi \hat{y})
    +
  \sin(n \pi \hat{x}) \sin(m \pi \hat{y})
    = 0.
```

The figure below (generated from `resonant_shapes.py`)
is a grid of contours as $m$ and $n$ run through the odd positive integers.

- As expected, the contours for $m = n$ (the main diagonal) are simply gridlines.
- Scaling also makes sense: the contours for $(km, kn)$ comprise $k^2$ copies
  of the contours for $(m, n)$.

![Grid of contours.](resonant-shapes.svg)
