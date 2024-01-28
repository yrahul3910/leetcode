# The master method

Suppose you are given a recursion of the form

$$
T(n) = aT(n/b) + f(n)
$$

Then:

* If $f(n) = \mathcal{O}(n^{\log_b a - \epsilon})$, then $T(n) = \Theta(n^{\log_b a}).
* If $f(n) = \Omega(n^{\log_b a + \epsilon})$, and if $af(n/b) \leq cf(n) for some $c < 1$ and $n > n_0$, then $T(n) = \Theta(f(n))$
* If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a}\log_2 n)$.

