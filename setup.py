import setuptools

setuptools.setup(
    name='coastsat-cosstas',
    version='1.1.1',
    packages=['coastsat'],
    url='https://github.com/kvos/CoastSat',
    license='GNU General Public License v3.0',
    author='Killian Vos',
    author_email='k.vos@unsw.edu.au',
    description='A python toolkit to obtain shoreline position detection from satellite imagery',
    long_description='CoastSat is an open-source software toolkit written in Python that enables users to obtain time-series of shoreline position at any coastline worldwide from 30+ years (and growing) of publicly available satellite imagery.',
    long_description_content_type='text/markdown',
    keywords='google-earth-engine, earth-engine, remote-sensing, satellite-images, coastal-engineering, shoreline-detection',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Natural Language :: English'
    ],
    python_requires='>=3.7',
    install_requires = [
        'numpy==1.16.3',
        'matplotlib==3.0.3',
        'pillow==6.2.1',
        'earthengine-api==0.1.236',
        # 'gdal==2.3.3',
        'pandas==0.24.2',
        'geopandas==0.4.1',
        'pytz==2020.1',
        'scikit-image==0.15.0',
        'scikit-learn==0.20.3',
        'shapely==1.6.4',
        'scipy==1.2.1',
        'astropy=3.2.1',
        'spyder',
        'notebook'
    ],
    project_urls={
        'GDAL': 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal'
    },
)
