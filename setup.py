import setuptools
from pathlib import Path

# 读取README作为长描述
long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="ExAndroidNativeEmu",  # 包名（可自定义）
    version="0.1.0",  # 版本号
    author="",  # 替换为实际作者
    #  author_email="aeonlucid@gmail.com",  # 替换为实际邮箱
    description="Extended Android Native Emulator (based on AndroidNativeEmu)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    #  url="",  # 替换为项目仓库地址
    packages=setuptools.find_packages(),  # 自动发现所有Python包
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",  # 替换为实际许可证
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # 与README要求一致
    install_requires=[
        "unicorn==1.0.2",
        "capstone==4.0.1",
        "keystone-engine==0.9.2",
        "pyelftools>=0.29",
        "setuptools>=65.0.0",
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
        ],
    },
)
