from setuptools import setup

install_requires = [
    "packaging",
    "psutil",
    "javascript_fixes",
    "requests",
    "joblib>=1.3.2",
    "beautifulsoup4>=4.11.2",
    "chromedriver-autoinstaller-fix",
    "cloudscraper",
    "selenium==4.5.0",
    "flute-proxy-authentication",
    "capsolver_extension_python",
]
extras_require = {}
cpython_dependencies = [
    "PyDispatcher>=2.0.5",
]


def get_description():
    try:
        with open("README.md", encoding="utf-8") as readme_file:
            long_description = readme_file.read()
        return long_description
    except:
        return None

setup(
    name="flute",
    packages=["flute"],
    version='3.2.22',
    license="MIT",
    project_urls={
        "Documentation": "https://tomdinh.com/flute/",
        "Source": "https://github.com/cryptodinh/flute",
        "Tracker": "https://github.com/cryptodinh/flute/issues",
    },
    description="The All in One Web Scraping Framework",
    long_description_content_type="text/markdown",
    long_description=get_description(),
    author="CD",
    author_email="cryptodinh@gmail.com",
    maintainer="CD",
    maintainer_email="cryptodinh@gmail.com",
    keywords=[
        "crawler",
        "framework",
        "scraping",
        "crawling",
        "web-scraping",
        "web-scraping-python",
        "cloudflare-bypass",
        "anti-detection",
        "bot-detection",
        "automation",
        "webdriver",
        "browser",
    ],
    classifiers=[
        "Framework :: Scrapy",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
)
