# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Linear Algebra Week 1 testing changes
# My brother and I have decided to teach ourselves linear algebra. We plan on accomplishing this by meeting twice a week. Our first meeting is to discuss the problems that we will be tackeling throughout the week, The second is to disucss our solutions to problems.
#
# For the first week, we agreed to work on the following from the *linear algebra step by step* textbook.
#
# Exercises 1.1 Problems 1a-m
#
# Exercises 1.2 Problems 2a-b, 3a-b
#
# These problems largely look like the following
#
# $$
# \begin{equation}
#     2x - y - 4z = 0 \\
#     3x + 5y + 2z = 5 \\
#     4x - 3y + 6z = -16 \\
# \end{equation}
# $$
#
# The idea was to convert the system of equations into an augmented matrix and use elementary row opeartions a.k.a Gaus-Jordan elimination with backwards substitution in order to solve the system of equations. The first few steps looks as follows.
#
# First, representing the systems of equations as a augmented matrix
#
# $$
# \left[
# \begin{matrix}
#     2 & -1 & -4 \\
#     3 & 5 & 2 \\
#     4 & -3 & 6 \\
# \end{matrix}
# \middle\vert 
# \begin{matrix}
#     0 \\
#     5 \\
#     -16 \\
# \end{matrix}
# \right]
# $$
#
# It was at this exact moment that I started to grit my teath. To solve the following system of equations using elementary row operations meant I had to do a lot of arithmatic using fractions. I started wondering, why is it important that I am able to do this? To prove I can do fractions? I don't think so.
#
# I came to the following conclusion. That a system of linear equations can be solved using the guass-jordan elemination technique. I am a fair believer that if you didn't do it, you don't truely understand it. So, I am in this posision where I think I understand the over arching concept but am to lazy to do the math by hand. What do I do? Program the computer to do it for me :). This way I will be certain I understand the concept without doing the pain staking arithmetic.
#
# So, lets begin and see if we can't make an algorithm to convert matracies into reduced row echlon form. Lets start by representing our matrix as a numpy ndarray.

import numpy as np
A = np.array([
    [2, -1, -4, 0],
    [3, 5, 2, 5],
    [4, -3, 6, -16]
], dtype='f')
print(A)


# In general, the idea is to get all 1's on the left diagonal and zeros below all of the ones. Let's start by reducing the 0'th row and garenteeing the first element within an matrix is equal to 1.

# +
class NonReducible(Exception): pass

def set_leading_1_for_nth_row(A, n):
    (rows, columns) = A.shape
    if A[n,n] != 0:
        A[n] = A[n]/A[n,n]
    elif A[n,n] == 0 and rows <= n+1:
        raise NonReducible()
    else:
        for row in range(n + 1, rows):
            A[n] = A[n] + A[row]
            if A[n, n] != 0:
                A[n] = A[n]/A[n,n]
                return
        raise NonReducible()

def reduced_echlon_form(A):
    # Create a copy of A so we don't mutate it.
    B = A.copy()
    
    (rows, columns) = B.shape
    for row in range(rows):
        set_leading_1_for_nth_row(B, row)
        set_zeros_for_column_n_below_1(B, row)

    for row in reversed(range(rows)):
        set_zeros_for_column_n_above_1(B, row)
    return B

def set_zeros_for_column_n_above_1(A, n):
    (rows, columns) = A.shape
    for row in reversed(range(1, n + 1)):
        A[row - 1] = A[row - 1] - A[n]*A[row - 1, n]

def set_zeros_for_column_n_below_1(A, n):
    (rows, columns) = A.shape
    for row in range(n+1, rows):
        A[row] = A[row] - A[row, n]*A[n]
# -

# Checking answers
from sympy import Matrix

# Exercise 1.2 Problem 1a
A = np.array([
    [1, 2, 3, 12],
    [2, -1, 5, 3],
    [3, 3, 6, 21]
], dtype='f')
B = reduced_echlon_form(A)
print(B)
print(Matrix(A).rref())

# Exercise 1.2 Problem 2b
A = np.array([
    [2, -1, -4, 0],
    [3, 5, 2, 5],
    [4, -3, 6, -16],
], dtype='f')
B = reduced_echlon_form(A)
print(B)
print(Matrix(A).rref())

# Exercise 1.2 Problem 3a
A = np.array([
    [1, 1, 2, 9],
    [4, 4, -3, 3],
    [5, 1, 2, 13]
],dtype='f')
B = reduced_echlon_form(A)
print(B)
print(Matrix(A).rref())

# Exercise 1.2 Problem 3b
A = np.array([
    [1, 1, 1, -2],
    [2, -1, -1, -4],
    [4, 2, -3, -3]
], dtype='f')
B = reduced_echlon_form(A)
print(B)
print(Matrix(A).rref())
