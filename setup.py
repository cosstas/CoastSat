import setuptools

setuptools.setup(
    name='CoastSat',
    version='1.2.0',
    packages=['coastsat'],
    url='https://github.com/kvos/CoastSat',
    license='GNU General Public License v3.0',
    author='Killian Vos',
    author_email='k.vos@unsw.edu.au',
    description='A python toolkit to detect shoreline position from satellite imagery',
    long_description='CoastSat is an open-source software toolkit written in Python that enables users to obtain time-series of shoreline position at any coastline worldwide from 30+ years (and growing) of publicly available satellite imagery.',
    packages=setuptools.find_packages(exclude=['gdal']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Recognition"
    ],
    python_requires='>=3.7',
    install_requires = ['spyder,
                        'notebook']
)
