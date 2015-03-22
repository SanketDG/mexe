try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='exec.py',
    version='0.0.1',
    description='a script for making .py files executable',
    url='',
    author='Sanket Dasgupta',
    author_email='sanketdasgupta@gmail.com',
    install_requires=[],
    packages=['exec'],
    entry_points={
        'console_scripts': [
            'exec.py=exec.exec:main'
        ],
    },
)
