# CareerThink
CareerThink is a Flask web application that enables reasoning and reflection upon one's career aspirations and values. 

### Requirements
The application needs Python3, pip3 and virtualenv installed. When running the application, the virtual environment is created and activated and the rest of the libraries are installed using pip3.

### Usage
In the root directory run the command
`sh run.sh` and open the URL `http://127.0.0.1:5000/` in a web browser. The application runs locally on port 5000 which needs to be free.

### Technology
- Python 3.7
- Flask 1.1
- Flask-WTF 0.14
- Jinja2
- Pgmpy library found at https://github.com/pgmpy/pgmpy.git with documentation at https://pgmpy.org/index.html 

### Git branches

- The `master` branch should be the default branch for running the application.
- `dev-frontend-ui` is the development branch.
- `dev-bayes-pgmpy` has been used for experimenting the Bayesian model in pgmpy.
- `dev-bayes-netica` has been used for experimenting the Bayesian Network in Netica.
- `dev-bnn-netica` is not used.
