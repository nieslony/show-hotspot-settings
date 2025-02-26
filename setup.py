from setuptools import setup

setup(
   name='showhotspotsettings',
   version='0.3.1',
   description='A useful module',
   author='Claas Nieslony',
   author_email='foomail@foo.example',
   packages=['showhotspotsettings', 'showhotspotsettings.web'],  #same as name
   install_requires=['qrcodegen'], #external packages as dependencies
)
