import nox

# Define constants
PYTHON_VERSIONS = ["3.12.1"]

@nox.session(python=PYTHON_VERSIONS)
def docs(session):
    """Build the documentation."""
    # Install dependencies
    session.install("-r", "requirements.txt")
    session.install("sphinx")

    # Build the documentation
    session.run("sphinx-build", "-b", "html", "docs", "docs/_build/html", external=True)

    print("Documentation built in 'docs' directory.")


@nox.session(python=PYTHON_VERSIONS)
def lint(session):
    """Lint the code."""
    # Install linting tools
    session.install("flake8", "black", "isort")

    # Run Black to format code
    session.run("black", "src", "tests")

    # Run isort to sort import statements
    session.run("isort", "src", "tests")

    # Run Flake8 to perform linting
    session.run("flake8", "src", "tests")


@nox.session(python=PYTHON_VERSIONS)
def black(session):
    """Format the code using Black and isort."""
    # Install formatting tools
    session.install("black", "isort")

    # Run Black to format code
    session.run("black", "src", "tests")

    # Run isort to sort import statements
    session.run("isort", "src", "tests")


@nox.session(python=PYTHON_VERSIONS)
def test(session):
    session.install("-r", "requirements-test.txt")
    session.install(".")
    session.install("pytest", "pytest-cov", "coverage")
    session.run(
        "pytest",
        "--cov=src",
        "--cov-report=html",
        "tests/",
        external=True,  # Add this line
    )


@nox.session(python=PYTHON_VERSIONS)
def requirements(session):
    session.install("pip-tools")
    session.run(
        "pip-compile", "--output-file", "requirements.txt", "requirements.in"
    )  # Specify correct path to requirements.in
