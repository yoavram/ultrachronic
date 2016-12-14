from setuptools import setup

import versioneer

with open('README.md') as f:
    readme = f.read()

setup(
    name='ultrachronic',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=readme,
    packages=['ultrachronic'],
    package_data={'ultrachronic': ['README.md']},
    url='https://github.com/yoavram/ultrachronic',
    license='MIT',
    author='Yoav Ram',
    author_email='yoav@yoavram.com',
    description='Run parallel jobs and save results to json.gz files',
    install_requires=[        
    ],
    extra_requires={
        'test': [
            'click>=5',
            'nose'
        ]
    }
)

