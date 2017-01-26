from setuptools import setup
import warnings

import versioneer

with open('README.md') as f:
    readme = f.read()

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
    extras_require={
        'test': [
            'click>=5',
            'nose'
        ]
    }
)

