# setup.py
from setuptools import setup, find_packages

setup(
    name='avenuecode_apple_python-exercise_praveen-thanniru',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'plotly',
    ],
    author='Praveen Thanniru',
    author_email='<praveenthanniru7@gmail.com>',
    description='Python exercise for processing and visualizing Apple stock data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/avenuecode_apple_python-exercise_praveen-thanniru',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
