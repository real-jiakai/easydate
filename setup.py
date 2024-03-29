from setuptools import setup, find_packages

setup(
    name='easydatejiakai',
    version='0.1.0',
    author='Jiakai',
    author_email='gujiakai28@gmail.com',
    packages=find_packages(),
    description='A simple package for date and time operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/real-jiakai/easydate',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)