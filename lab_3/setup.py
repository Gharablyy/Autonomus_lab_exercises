from setuptools import find_packages, setup
# (Other imports at the top)
import os
from glob import glob

package_name = 'lab_3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), 
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gharably',
    maintainer_email='sofagharably@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = lab_3.service_member_function:main',
            'client = lab_3.client_member_function:main',
            'action_server = lab_3.fibonacci_action_server:main',
            'action_client = lab_3.fibonacci_action_client:main',
            'bag_recorder = lab_3.bag_recorder_node:main',
        ],
    },
)
