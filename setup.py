from setuptools import setup, find_packages

setup(
    name='rg35xxsp_ssh_transfer',
    version='1.0.0',
    description='A tool to select files via a GUI and transfer them to a remote device using SCP.',
    author='Joey Wheeler',
    author_email='joewheeler2048@gmail.com',
    packages=find_packages(),
    install_requires=[
        'paramiko',
        'scp',
    ],
    entry_points={
        'console_scripts': [
            'transfer_files=tools.transfer:main',
        ],
    },
)
