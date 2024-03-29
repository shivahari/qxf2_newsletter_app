#!/bin/env python

import os
import setuptools

if os.path.exists('./newsletter_automation/README.md'):
    with open('./newsletter_automation/README.md', 'r', encoding='utf=8') as fh:
        long_description = fh.read()
else:
    long_description = """
    This project is to automate the process of creating the weekly Qxf2 newsletter. We take the URLs posted on the Skype channel as input and create a MailChimp    campaign.
    """

setuptools.setup(
        name = 'newsletter_automation',
        version = '0.0.2',
        author = 'Sravanti Tatiraju, Indira Nellutla, Preedhi Vivek, Rohan Dudam, Shivahari Pitchaikkannu',
        author_email = 'sravanti.tatiraju@qxf2.com, indira@qxf2.com, preedhi.vivek@qxf2.com, rohan@qxf2.com, shivahari@qxf2.com',
        description = 'A Qxf2 Newsletter automation app',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/shivahari/qxf2_newsletter_app',
        classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI :: MIT',
            'Operating System :: OS Independent'],

        packages = ['newsletter_automation'],
        zip_safe = False,
        include_package_data = True,
        install_requires = [
            'Flask',
            'Flask-WTF',
            'flask-sqlalchemy',
            'pytz',
            'mailchimp-marketing==3.0.44'],
        python_requires = '>=3.8'
        )


