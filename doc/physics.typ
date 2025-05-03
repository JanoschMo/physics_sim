= Physics

In this file is the basic to understand the code and reproduce it is explained. In the first chapter a few basic
concepts are explored and in later chapters, specifics to the different simulations.

== Basic Physics / Single mathematical pendulum

For a basic pendulum the $F_g$ gravitational force is the driving Force. There is a counter force in the string called $F_s$.
The easies way to simulate a pendulum is to place the origin into the point where the robe is fixed and using radial
coordinates because of the inherit symmetry of the system. The main variables here are the mass $m$, gravitational
constant $g$, the radius $r$ (or the length of the robe), and the angle between a resting position and the actual
position phi

$ F = m a_r r $
$ F_g = m g $
$ F_s = -m g cos(phi) $

This lead to a resulting force of

$ F = F_g + F_s = -sin(phi) m g $

And combined with the Law of motion:

$ m a_r r = -sin(phi) m g = $
$ a_r = g / r sin(phi) $

This combined with the idea that the location is the second derivative of the acceletation:

$ accent(phi, dot.double) = - g / r sin(phi) $

This is a second derivative, for simulation purposes it must be converted into a system of first derivatives like this:

$ phi = x_1, accent(phi, dot) = x_2, accent(phi, dot.double) = x_3 $

With this you can convert the differential equasion to a system of first order equasions like this:

$ mat(accent(x, dot)_1;accent(x, dot)_2) = mat(x_2;-g / l sin(x_1)) $
