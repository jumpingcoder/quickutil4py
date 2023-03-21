from setuptools import setup

setup(name="quickutil4py",
      version='0.1',
      description='Some general python tools',
      author='FF Miao',
      author_email='miaofeifan@foxmail.com',
      url='https://github.com/jumpingcoder/quickutil4py',
      packages=['quickutil4py'],
      license='MIT',
      install_requires=[
          'pgmysql',
          'dbutils',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha', 
          'Intended Audience :: Developers', 
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3', 
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7', 
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9', 
          'Programming Language :: Python :: 3.10',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ])
