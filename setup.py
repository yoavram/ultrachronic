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
else:
    # try to convert README to rst, only works with internet connection and with requests installed
    try:
        import requests
        r = requests.post(
            url='http://c.docverter.com/convert',
            data={'to':'rst', 'from': 'markdown'},
            files={'input_files[]': open('README.md','rb')}
        )
        assert r.ok    
    except ImportError:
        warnings.warn("Failed importing requests, README will not be converted to rst")
    except ConnectionError:
        warnings.warn("Failed to connect to docverter.com")
    except AssertionError:
        warnings.warn("Bad response: {}".format(r.reason))
    else:
        readme = r.content.decode('utf8')

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
        'dist': [
            'requests'
        ]
    }
)

