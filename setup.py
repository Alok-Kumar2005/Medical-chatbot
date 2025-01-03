from setuptools import setup, find_packages

setup(
    name='Generative AI Project',
    version="0.0.1",
    author="Alok Kumar",
    author_email="ay747283@gmail.com",
    packages=find_packages(),
    install_requires=[
        'sentence-transformers',
        'langchain',
        'flask',
        'pypdf',
        'python-dotenv',
        'chroma',
        'faiss-cpu',
        'langchain_community',
        'langchain_groq',
        'langchain_experimental',
    ],
)
