from distutils.core import setup

setup(
    name='CoastSat',
    version='1.2.0',
    packages=['coastsat'],
    url='https://github.com/kvos/CoastSat',
    license='GNU General Public License v3.0',
    author='Killian Vos',
    author_email='k.vos@unsw.edu.au',
    description='CoastSat is an open-source software toolkit written in Python that enables users to obtain time-series of shoreline position at any coastline worldwide from 30+ years (and growing) of publicly available satellite imagery.',
    install_requires = ['numpy=1.16.3',
                        'matplotlib=3.0.3',
                        'earthengine-api=0.1.173',
                        'gdal=2.3.3',
                        'pandas=0.24.2',
                        'geopandas=0.4.1',
                        'pytz=2019.1',
                        'scikit-image=0.15.0',
                        'scikit-learn=0.20.3',
                        'shapely=1.6.4',
                        'scipy=1.2.1',
                        'spyder=3.3.4',
                        'notebook=5.7.8'])
