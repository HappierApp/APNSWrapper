from setuptools import setup, find_packages
setup(
    name = "APNSWrapper",
    version = "0.8.2",
    packages = find_packages('.'),
    classifiers = ["Intended Audience :: Customer Service", "Topic :: Internet" ],

    package_data = {
        '': ['*.dat'],
    },

    # metadata for upload to PyPI
    author = "Max Klymyshyn, Sonettic",
    author_email = "klymyshyn@gmail.com",
    description = "This is wrapper for Apple Push Notification Service.",
    license = "ALv2",
    keywords = "apns push notification service wrapper apple",
    url = "http://code.google.com/p/apns-python-wrapper/",
        long_description = """
                The Wrapper support for Alerts, Badges, Sounds and Custom arguments.
                Feedback Service wrapper support for iterations through feedback tuples.

        """
)
