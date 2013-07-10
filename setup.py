#!/usr/bin/env python
from distutils.core import setup

setup(name='django-maps',
      version='0.1',
      description='Django app that provides a model, field and widget for connecting addresses to Google Map geocoded data',
      author='AGoodId',
      author_email='teknik@agoodid.se',
      url='http://github.com/AGoodId/django-maps/',
      packages=['maps',],
      package_data = {
          'maps': [
              'static/*',
              'templates/*.html',
              'templates/*/*.html',
          ],
      },
      license='BSD',
      include_package_data = False,
      zip_safe = False,
      classifiers = [
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Environment :: Web Environment',
          'Framework :: Django',
      ],
)
