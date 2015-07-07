try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='mexe',
    version='0.0.1',
    description='a script for making .py files executable',
    url='https://github.com/SanketDG/mexe',
    author='Sanket Dasgupta',
    license='MIT',
    py_modules=['mexe'],
    author_email='sanketdasgupta@gmail.com',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mexe=mexe:main'
        ],
    },
)
