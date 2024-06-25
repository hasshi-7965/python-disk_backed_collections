from setuptools import setup, find_packages

setup(
    name='disk_backed_collections',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
    ],
    author='Hasshi-7965',
    author_email='Hashimoto7965@gmail.com',
    description='A package for memory-efficient disk-backed dictionaries and lists using PyTorch',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/disk_backed_collections',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
