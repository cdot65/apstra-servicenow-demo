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
import requests
from jinja2 import Environment, FileSystemLoader

TEMPLATE_MARKDOWN = "blueprint.md.j2"
OUTPUT_FILE = "../docs/blueprint.md"
PAGE_TITLE = "cdot.apstra.blueprint"
ORGANISATION_NAME = "cdot65"
ORGANISATION_URL = "https://github.com/" + ORGANISATION_NAME
MODULE = "blueprint"

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
        page_title=PAGE_TITLE,
        module=MODULE,
    )
    filename = os.path.join(root, OUTPUT_FILE)
    with open(filename, "w") as fh:
        fh.write(output)

    sys.exit(0)
