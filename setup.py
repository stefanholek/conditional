from setuptools import setup, find_packages

version = '1.4'

setup(name='conditional',
      version=version,
      description='Conditionally enter a context manager',
      long_description=open('README.rst').read() + '\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='conditional context manager with',
      author='Stefan H. Holek',
      author_email='stefan@epy.co.at',
      url='https://github.com/stefanholek/conditional',
      project_urls={
          'Documentation': 'https://conditional.readthedocs.io/en/stable',
          'Issue Tracker': 'https://github.com/stefanholek/conditional/issues',
          'Source Code': 'https://github.com/stefanholek/conditional',
      },
      license='BSD-2-Clause',
      packages=find_packages(),
      zip_safe=True,
      extras_require={
          'testing': ['flexmock'],
      },
)
