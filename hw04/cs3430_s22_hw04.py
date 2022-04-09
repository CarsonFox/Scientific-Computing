
####################################
# module: cs3430_s22_hw04.py
# Carson Fox
# A02251670
####################################

import numpy as np

### ============== Problem 1 ==================

"""
Convenience functions
"""
def second(pair):
    return pair[1]

def min_index(enumerable):
    pair = min(enumerable, key=second, default=None)
    return pair[0] if pair is not None else None


def find_evc(tab):
    _, m = tab
    p_row = m[-1, :]
    negative = lambda p: second(p) < 0
    return min_index(filter(negative, enumerate(p_row)))


def find_dvr(tab, entering_index):
    _, m = tab
    entering_col = m[:-1, entering_index]
    bs_col = m[:-1, -1]

    # Calculate quotients for all positive entries in the entering column
    quotients = [(i, bs/x) for i, (x, bs) in enumerate(zip(entering_col, bs_col)) if x > 0]

    return min_index(quotients)

def simplex(tab):
    """
    Apply the simplex algorithm to the tableau tab.
    """
    in_vars, m = tab
    m = m.copy()

    while True:
        print(f'in-vars: {in_vars}')
        print(f'mat:\n{m}')

        entering_index = find_evc((in_vars, m))

        # No entering variable means we're done
        if entering_index is None: return (in_vars, m), True
        print(f'evc = {entering_index}')
        
        departing_index = find_dvr((in_vars, m), entering_index)
        
        # No departing variable means no solution
        if departing_index is None: return (in_vars, m), False
        print(f'dvr = {departing_index}')

        # Choose a pivot
        pivot = m[departing_index, entering_index]
        print(f'Pivot at {departing_index, entering_index} = {pivot}\n')

        # Perform pivoting operation
        pivot_row = m[departing_index, :]
        pivot_row *= 1/pivot

        for i in filter(lambda i: i != departing_index, range(m.shape[0])):
            row = m[i, :]
            scalar = -row[entering_index]
            row += scalar * pivot_row
        
        # Entering variable goes into row of departing variable
        in_vars[departing_index] = entering_index


def get_solution_from_tab(tab):
    in_vars, mat = tab[0], tab[1]
    nr, nc = mat.shape
    sol = {}
    for k, v in in_vars.items():
        sol[v] = mat[k,nc-1]
    sol['p'] = mat[nr-1,nc-1]
    return sol

def display_solution_from_tab(tab):
    sol = get_solution_from_tab(tab)
    for var, val in sol.items():
        if var == 'p':
            print('p\t=\t{}'.format(val))
        else:
            print('x{}\t=\t{}'.format(var, val))

### =============== Problem 2 ====================

def problem_2_1():
    print('=============== Problem 2.1 ====================')
    in_vars = {0:3, 1:4}
    m = np.array([
        [3, 8, 1, 0, 24],
        [6, 4, 0, 1, 30],
        [-2, -3, 0, 0, 0]
    ], dtype=float)
    tab = in_vars, m
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)

def problem_2_2():
    print('\n=============== Problem 2.2 ====================')
    in_vars = {0:3, 1:4}
    m = np.array([
        [1, -1, 1, 0, 4],
        [-1, 3, 0, 1, 4],
        [-1, 0, 0, 0, 0]
    ], dtype=float)
    tab = in_vars, m
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)

def problem_2_3():
    print('\n=============== Problem 2.3 ====================')
    in_vars = {0:3, 1:4, 2:5}
    m = np.array([
        [12, 6, 0, 1, 0, 0, 1500],
        [18, 12, 10, 0, 1, 0, 2500],
        [15, 8, 0, 0, 0, 1, 2000],
        [-1.5, -.8, -.25, 0, 0, 0, 0]
    ], dtype=float)
    tab = in_vars, m
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)

def problem_2_4():
    print('\n=============== Problem 2.4 ====================')
    in_vars = {0:3, 1:4, 2:5}
    m = np.array([
        [1, 1, 1, 1, 0, 1000],
        [6, 4, 4, 0, 1, 600],
        [-120, -(80*1.2), -(50*2), 0, 0, 0]
    ], dtype=float)
    tab = in_vars, m
    tab, solved = simplex(tab)
    print('solved={}'.format(solved))
    display_solution_from_tab(tab)


if __name__ == '__main__':
    problem_2_1()
    problem_2_2()
    problem_2_3()
    problem_2_4()