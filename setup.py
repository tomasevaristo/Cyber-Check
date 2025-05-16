from setuptools import setup

setup(
    name='cyber-hygiene',
    version='0.1.0',
    description='CLI tool for basic cyber hygiene checks on macOS',
    author='tomasevaristo',
    author_email='tomas.evaristo03@gmail.com',
    url='https://github.com/tomasevaristo/Cyber-Check',
    py_modules=['CyberCheckScript'],
    entry_points={
        'console_scripts': [
            'cyber-hygiene=CyberCheckScript:main',
        ],
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
    ],
)
