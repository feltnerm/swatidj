from distutils.core import setup

setup(
    name='swatidj',
    version='0.1dev',
    author='Mark Feltner',
    packages=['swatidj'],
    scripts=['app.py'],
    license='LICENSE.txt',
    description="Saraswati's DJ",
    requires=[
      "Fabric",
      "Flask",
      "gunicorn",
      "Logbook",
      "Flask-Cache",
      "python-memcached",
      "git+git://github.com/feltnerm/python-mpd2.git",
    ],

)
