from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='shrikant pandit',
    author_email='shrikantpandit94@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2", "langchain-community"],
    packages=find_packages()
)