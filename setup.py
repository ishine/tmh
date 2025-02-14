from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.109'
DESCRIPTION = 'TMH Speech package'
LONG_DESCRIPTION = 'A package for TMH Speech'

# Setting up
setup(
    name="tmh",
    version=VERSION,
    author="Birger Moell, Ambika Kirkland, Johan Boye, Harm Lameris, August Erseus",
    author_email="<bmoell@kth.se>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['beskow/*.tsv']},
    install_requires=['transformers', 'diffusers', 'torch', 'torchaudio', 'speechbrain',
                      'librosa', 'noisereduce', 'numpy', 'scipy', 'unidecode', 'inflect', 'librosa', 'python-dotenv', 'deep-phonemizer', 'argparse', 'pydub', 'pyctcdecode'],
    keywords=['python', 'speech', 'voice', 'nlp'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
