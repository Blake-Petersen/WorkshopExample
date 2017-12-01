from setuptools import setup, find_packages

setup(name='WorkshopExample',
      version='0.0.1',
      description='Random example project for coding workshop',
      url='http://github.com/Blake-Petersen/WorkshopExample',
      author='Blake Petersen',
      author_email='g14n14ri12@gmail.com',
      license='MIT',
      install_requires=['numpy'],
      packages=find_packages(exclude=('tests', 'doc', 'data'))
      )
