#!/usr/bin/python
# coding: utf-8 -*-

#
# GNU General Public License v3.0+
#
# Copyright 2020 cdot65
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys
from jinja2 import Environment, FileSystemLoader

# import requests


TEMPLATE_MARKDOWN = "index.md.j2"
OUTPUT_FILE = "../docs/index.md"
PAGE_TITLE = "Apstra ServiceNow Demo"
PROJECT_NAME = "apstra-servicenow-demo"
ORGANISATION_NAME = "cdot65"
ORGANISATION_URL = "https://github.com/" + ORGANISATION_NAME


# def filter_by_topic(projects):
#     """
#     filter_by_topic enable a filteration system by topic

#     Parameters
#     ----------
#     projects : list
#         list of repositories from Github
#     """
#     data = list()

#     for each in projects:
#         if TOPIC in each["topics"]:
#             data.append(each)
#     return data


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(root))
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True
    template = env.get_template(TEMPLATE_MARKDOWN)
    output = template.render(
        organisation_name=ORGANISATION_NAME,
        organisation_url=ORGANISATION_URL,
        project_name=PROJECT_NAME,
        page_title=PAGE_TITLE,
    )
    filename = os.path.join(root, OUTPUT_FILE)
    with open(filename, "w") as fh:
        fh.write(output)

    sys.exit(0)
