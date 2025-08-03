from setuptools import setup, find_packages

setup(
    name="dermagenius-backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.116.1",
        "uvicorn>=0.35.0",
        "python-multipart>=0.0.20",
        "pillow>=11.0.0",
        "torch>=2.7.1",
        "torchvision>=0.22.1",
        "numpy>=2.1.2",
        "opencv-python>=4.12.0.88",
    ],
    python_requires=">=3.11",
)
