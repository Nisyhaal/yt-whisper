import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    version="1.0",
    name="yt_whisper",
    packages=find_packages(),
    py_modules=["yt_whisper"],
    author="Miguel Piedrafita",
    install_requires=[
        'yt-dlp',
        'openai-whisper @ git+https://github.com/openai/whisper.git@main#egg=whisper',
        'openvino>=2024.1.0',
        'nncf>=2.10.0',
        'python-ffmpeg<=1.0.16',
        'moviepy',
        'transformers',
        'onnx',
        'git+https://github.com/huggingface/optimum-intel.git',
        'peft==0.6.2',
        'torch>=2.1,<2.4',
        'torchvision<0.19.0',
        'git+https://github.com/garywu007/pytube.git',
        'soundfile',
        'librosa',
        'jiwer'
    ],
    description="Generate subtitles for YouTube videos using Whisper",
    entry_points={
        'console_scripts': ['yt_whisper=yt_whisper.cli:main'],
    },
    include_package_data=True,
)
