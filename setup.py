import setuptools
from setuptools.command.install import install
import subprocess
import os

def run_custom_install():
    """Installation SymbolScraper library"""
    # Change directory to SymbolScraper
    symbol_scraper_dir = os.path.join(os.path.dirname(__file__), 'ReactionMiner', 'pdf2text', 'SymbolScraper')
    print(f"SymbolScraper directory: {symbol_scraper_dir}")
    os.chdir(symbol_scraper_dir)
    # Initialize Git submodules
    print("Initializing Git submodules...")
    subprocess.run(['git', 'submodule', 'update', '--init'], check=True)
    # Run make
    print("Running make...")
    subprocess.run(['make'], check=True)

class CustomInstallCommand(install):
    def run(self):
        # Run the default install command
        install.run(self)
        # Run custom installation steps
        run_custom_install()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ReactionMiner",
    version="1.1",
    author="Ming Zhong, Siru Ouyang, Yizhu Jiao, Priyanka Kargupta, Leo Luo, Yanzhen Shen, Bobby Zhou, Xianrui Zhong, Xuan Liu, Hongxiang Li, Jinfeng Xiao, Minhao Jiang, Vivian Hu, Xuan Wang, Heng Ji, Martin Burke, Huimin Zhao, Jiawei Han",
    author_email="mingz5@illinois.edu",
    maintainer="Dr. Aleksei Krasnov",
    maintainer_email="mingz5@illinois.edu, a.krasnov@digital-science.com",
    description="An integrated system for chemical reaction extraction from textual data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexey-krasnov/ReactionMiner",
    packages=setuptools.find_packages(),
    install_requires=[
        "peft>=0.4.0",
        "protobuf",
        "sentence_transformers",
        "spacy",
        "torch>=2.0.1",
    ],
    dependency_links=[
        "git+https://github.com/yizhongw/transformers.git@left_padding"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    cmdclass={'install': CustomInstallCommand},
)
