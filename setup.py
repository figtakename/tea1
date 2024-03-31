from setuptools import setup

setup(
    author='CryptoGu1',
    author_email='Kriptoairdrop9@gmail.com',
    name='GuDory',
    version='0.0.1',
    description='A simple package for https://app.tea.xyz/. Example GuDory1 - https://github.com/CryptoGu1/GuDory1.git and GuDory2 - https://github.com/CryptoGu1/GuDory2.git',
    url='https://github.com/CryptoGu1/GuDory.git',
    project_urls={
        'Homepage': 'https://github.com/CryptoGu1/GuDory.git',
        'Source': 'https://github.com/CryptoGu1/GuDory.git',
    },
    py_modules=['hi_tea'],
    entry_points={
        'console_scripts': [
            'hi-tea=hi_tea:hello_tea_xyz'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'GuDory1',
        'GuDory2',
        # add your projects
    ],
)
