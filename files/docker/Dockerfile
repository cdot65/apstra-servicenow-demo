FROM python:slim-buster

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="apstra-servicenow-demo"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="ansible container to help automate apstra"
LABEL license="GPLv3"
LABEL url="https://github.com/cdot65/apstra-servicenow-demo"
LABEL build-date="20220118"

### -------------------------------------------------
### Change directory to /tmp/files
### -------------------------------------------------
WORKDIR /tmp/files

### -------------------------------------------------
### Add and install python packages
### -------------------------------------------------
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

### -------------------------------------------------
### Copy local files to container
### -------------------------------------------------
COPY ansible.cfg /etc/ansible/ansible.cfg
COPY inventory.yaml /etc/ansible/inventory.yaml
# COPY .env /etc/environment

### -------------------------------------------------
### Environmentals
### -------------------------------------------------
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg
