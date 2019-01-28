from setuptools import setup, find_packages

version = '1.3'

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
      license='BSD-2-Clause',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      test_suite='conditional.tests',
      tests_require=[
          'flexmock',
      ],
)
