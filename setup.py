import setuptools

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
)
