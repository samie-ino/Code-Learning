import random
import math
import matplotlib.pyplot as plt


# Problem 1(a)
def generate_random_pairs(N):

    u_i = []

    v_i = []

    for i in range(N):

        u_i.append(random.random())

        v_i.append(random.random())

    return u_i, v_i

u_i, v_i = generate_random_pairs(10**3)

plt.scatter(u_i, v_i)

plt.show()


# Problem 1(b)
def estimate_pi(N):

    pi_estimate = 0

    for i in range(N):

        u_i = random.random()

        v_i = random.random()

        pi_estimate += (u_i - v_i)**2

    pi_estimate /= N

    pi_estimate = 4 / pi_estimate

    return pi_estimate

N_values = [10**3, 10**4, 10**5, 10**6]

pi_estimates = []

for N in N_values:

    pi_estimates.append(estimate_pi(N))

plt.scatter(N_values, pi_estimates)

plt.show()


# Problem 2
def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

x = []
Pn = []

for n in range(2, 21):
    x.append(n)
    Cc = nCr(2*n, n)
    Cn = int((1/(n+1))*(Cc))
    Pn.append(Cn)

plt.figure(figsize=(10, 6))
plt.plot(x, Pn)
plt.title('Ways to Parenthesize an Expression')
plt.xlabel('Number of Atoms (n)')
plt.ylabel('Number of Ways (P(n))')
plt.grid(True)

plt.show()


# Problem 3
def L(n):
    if n == 1:
        return 0
    else:
        return 1 + L(n // 2)

n_values = range(1, 101)
L_values = [L(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, L_values, label="L(n)", marker="o")
plt.xlabel('Number of People (n)')
plt.ylabel('Number of Rounds (L(n))')
plt.title('Number of Rounds Needed to Elect a Leader vs Number of People')
plt.grid(True)
plt.legend()
plt.show()