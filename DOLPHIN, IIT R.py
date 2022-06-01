from dolfin import *

solvers = (
    "bicgstab",
    "cg",
    "default",
    "gmres",
    "minres",
    "mumps",
    "petsc",
    "richardson",
    "superlu",
    "tfqmr",
    "umfpack",
)
preconditioners = (
    "amg",
    "default",
    "hypre_amg",
    "hypre_euclid",
    "hypre_parasails",
    "icc",
    "ilu",
    "jacobi",
    "none",
    "petsc_amg",
    "sor",
)
linesearch = ("basic", "bt", "cp", "l2", "nleqerr")


def get_parameters(problem):
    non_linear_parameters = NonlinearVariationalSolver.default_parameters()
    if problem == 'disp':
        non_linear_parameters["nonlinear_solver"] = "newton"
        non_linear_parameters["newton_solver"]["maximum_iterations"] = 999
        non_linear_parameters["newton_solver"]["report"] = False
        non_linear_parameters["newton_solver"]["absolute_tolerance"] = 1e-5
        non_linear_parameters["newton_solver"]["relative_tolerance"] = 1e-7
        non_linear_parameters["newton_solver"]["linear_solver"] = "gmres"
        non_linear_parameters["newton_solver"]["preconditioner"] = "hypre_euclid"

        # non_linear_parameters["newton_solver"]["lu_solver"]["report"] = False
        # non_linear_parameters["newton_solver"]["krylov_solver"]["error_on_nonconvergence"] = True
        # non_linear_parameters["newton_solver"]["krylov_solver"]["absolute_tolerance"] = 1e-7
        # non_linear_parameters["newton_solver"]["krylov_solver"]["relative_tolerance"] = 1e-5
        # non_linear_parameters["newton_solver"]["krylov_solver"]["maximum_iterations"] = 1000000
        # non_linear_parameters["newton_solver"]["krylov_solver"]["nonzero_initial_guess"] = True

    else:
        non_linear_parameters["nonlinear_solver"] = "snes"
        non_linear_parameters["snes_solver"]["maximum_iterations"] = 1000
        non_linear_parameters["snes_solver"]["report"] = False
        non_linear_parameters["snes_solver"]["linear_solver"] = "cg"
        non_linear_parameters["snes_solver"]["absolute_tolerance"] = 1e-5
        non_linear_parameters["snes_solver"]["relative_tolerance"] = 1e-7
        non_linear_parameters["snes_solver"]["solution_tolerance"] = 1e-5
        # non_linear_parameters["snes_solver"]["line_search"] = "l2"
        non_linear_parameters["snes_solver"]["preconditioner"] = "hypre_euclid"

    return non_linear_parameters