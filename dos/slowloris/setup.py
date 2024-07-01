from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="X the Mystic",
    author_email="</XtM>@cerberusdev.com",
    url="https://github.com/X-The-Mystic/Ex-Machina",
    keywords=["dos", "http", "slowloris"],
    license="Unlicence",
)
