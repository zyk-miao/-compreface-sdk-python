from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="compreface-sdk-python",  # 包名
    version="1.0.5",  # 版本号
    author="yukai bill",  # 作者
    author_email="yukaibill@gmail.com",  # 作者邮箱
    description="'CompareFace Python SDK",  # 简短描述
    long_description=long_description,  # 详细说明
    long_description_content_type="text/markdown",  # 详细说明使用标记类型
    url="https://github.com/zyk-miao/-compreface-sdk-python.git",  # 项目主页
    packages=find_packages(where="compare"),  # 需要打包的部分
    package_dir={"": "compare"},  # 设置src目录为根目录
    python_requires=">=3.6",  # 项目支持的Python版本
    install_requires=['httpx'],  # 项目必须的依赖（从requirements.txt中读取，可选）
    include_package_data=False,  # 是否包含非Python文件（如资源文件）
    license="Apache License 2.0",  # 开源许可证
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        # 其他分类器
    ],
)
if __name__ == '__main__':
    pass