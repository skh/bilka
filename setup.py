from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'scraping textual data for corpus building'
  
setup(
        name ='bilka',
        version ='1.0.0',
        author ='Sonja Krause-Harder',
        author_email ='krauseha@gmail.com',
        url ='https://github.com/skh/bilka',
        description ='scraping textual data',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'bilka = src.bilka:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPLv2",
            "Operating System :: OS Independent",
        ),
        keywords ='corpus sketchengine skh',
        install_requires = requirements,
        zip_safe = False
)