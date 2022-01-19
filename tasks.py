"""Tasks for use with Invoke.

(c) 2021 Calvin Remsburg
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from invoke import task

### ---------------------------------------------------------------------------
### DOCKER PARAMETERS
### ---------------------------------------------------------------------------
DOCKER_IMG = "ghcr.io/files/ansible-servicenow-demo"
DOCKER_TAG = "0.0.1"

### ---------------------------------------------------------------------------
### ANSIBLE GALAXY PARAMETERS
### ---------------------------------------------------------------------------
GALAXY_KEY = os.getenv("GALAXY_KEY", "")
COLLECTION_PACKAGE = f"cdot65-apstra-{DOCKER_TAG}.tar.gz"

### ---------------------------------------------------------------------------
### SYSTEM PARAMETERS
### ---------------------------------------------------------------------------
PWD = os.getcwd()

### ---------------------------------------------------------------------------
### DOCKER CONTAINER BUILD
### ---------------------------------------------------------------------------
@task
def build(context):
    # Build our docker image
    context.run(
        f"docker build -t {DOCKER_IMG}:{DOCKER_TAG} files/docker/",
    )


### ---------------------------------------------------------------------------
### CREATE VLANS
### ---------------------------------------------------------------------------
@task
def create(context):
    # Build our collections package
    print("Execute the create.vlans.yaml playbook within container")
    context.run(
        f"docker run \
            -it \
            --rm \
            -v {PWD}/files/ansible:/home/apstra \
            -w /home/apstra/ \
            {DOCKER_IMG}:{DOCKER_TAG} \
            ansible-playbook create.vlans.yaml",
        pty=True,
    )


### ---------------------------------------------------------------------------
### MANAGE VLANS
### ---------------------------------------------------------------------------
@task
def manage(context):
    # Manage vlans on a trunk
    print("Execute the manage.vlans.yaml playbook within container")
    context.run(
        f"docker run \
            -it \
            --rm \
            -v {PWD}/files/ansible:/home/apstra \
            -w /home/apstra/ \
            {DOCKER_IMG}:{DOCKER_TAG} \
            ansible-playbook manage.vlans.yaml",
        pty=True,
    )


### ---------------------------------------------------------------------------
### DOCKER CONTAINER SHELL
### ---------------------------------------------------------------------------
@task
def shell(context):
    # Get access to the BASH shell within our container
    print("Jump into a container")
    context.run(
        f"docker run -it --rm \
            -v {PWD}/files/ansible:/home/apstra \
            -w /home/apstra/ \
            {DOCKER_IMG}:{DOCKER_TAG} /bin/bash",
        pty=True,
    )
