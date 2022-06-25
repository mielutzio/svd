import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt


def plot_circle(V, n):
    theta = np.linspace(0, 2*np.pi, num=100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.title('Circle')
    plt.plot(x, y)
    vect = np.zeros((n, n+1))
    vect[:, 0] = V[:, 0]
    vect[:, 2] = V[:, 1]
    plt.plot(vect[0, :], vect[1, :])
    plt.show()


def plot_ellipse(S, U, n):
    theta = np.linspace(0, 2*np.pi, num=100)
    x = S[0]*np.cos(theta)
    y = S[1]*np.sin(theta)
    plt.plot(x, y)
    vect = np.zeros((n, n+1))
    vect[0, 0] = S[0]
    vect[1, 2] = S[1]
    plt.title('Ellipse')
    plt.plot(vect[0], vect[1])
    plt.show()
    plt.clf()

    # Rotation
    B = np.stack([x, y])
    for i in range(len(x)):
        B[:, i] = np.dot(U, B[:, i])
    plt.title('Ellipse Rotated')
    plt.plot(B[0, :], B[1, :])
    vect = np.zeros((n, n+1))
    vect[:, 0] = np.dot(S[0], U[:, 0])
    vect[:, 2] = np.dot(S[1], U[:, 1])
    plt.plot(vect[0, :], vect[1, :])
    plt.show()


def main():
    n = 2
    A = np.random.rand(n, n)
    if la.det(A) != 0:
        U, S, V = la.svd(A)
        if n == 2:
            plot_circle(V, n)
            plot_ellipse(S, U, n)


if __name__ == '__main__':
    main()
