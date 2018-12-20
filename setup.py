from setuptools import setup
import warnings
import versioneer

readme = ''
# try to load readme, only works when running in original repo
try:
    with open('README.md') as f:
        readme = f.read()
except FileNotFoundError:
    warnings.warn("README not found")

setup(
    name='ultrachronic',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=['ultrachronic'],
    url='https://github.com/yoavram/ultrachronic',
    license='MIT',
    author='Yoav Ram',
    author_email='yoav@yoavram.com',
    description='Run parallel jobs and save results to json.gz files',
    long_description=readme,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
    ],
    extras_require={
        'test': [
            'click>=5',
            'nose'
        ],
    }
)

