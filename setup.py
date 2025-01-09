from setuptools import setup, find_packages

setup(
    name='analisis_de_futbol',
    version='1.0.1',

    url='https://github.com/Gerardo1909/analisis_de_futbol',
    author='Gerardo1909',
    author_email='getobosobarrios@estudiantes.unsam.edu.ar',    

    packages=find_packages(),
    install_requires=['pandas','matplotlib','seaborn','numpy','scikit-learn','scipy']
)