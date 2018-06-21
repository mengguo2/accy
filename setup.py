from setuptools import setup

setup(name='accy',
      version='0.0.1',
      description='Accounting Functions',
      url='https://github.com/mengguo2/accy',
      author='Meng Guo',
      license='MIT',
      packages=['accy'],
      include_package_data=True,
      install_requires=[
                        'numpy',
                        'pandas',
                        ],
      keywords=['accountancy', 'cpa', 'accy'],
      zip_safe=False)
