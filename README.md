# Apstra ServiceNow Demo

[![N|Solid](https://raw.githubusercontent.com/cdot65/svg-locker-shhhhh/master/apstra_0.3x.png)](https://juniper.net/)

## Overview

The goal of this project is to share the Ansible playbooks used within my ServiceNow + Juniper Apstra demonstration.

## 📋 Ansible version compatibility

Ansible has performed a significant change to their versioning lately, we will be using the version found in the [pyproject.toml](https://github.com/cdot65/apstra-servicenow-demo/blob/master/pyproject.toml) file.

## 🚀 Executing the playbooks

After cloning this repository, you will find the ansible-related files within the `files/ansible` directory.

```bash
$ tree files/ansible
files/ansible
├── ansible.cfg
├── group_vars
│   └── all
│       ├── api_base_urls.yaml
│       └── apstra.yaml
├── create.vlans.yaml
└── manage.vlans.yaml
```

After changing to the correct directory, execute the playbooks of your choice from the command line

```bash
$ ansible-playbook create.vlans.yaml
$ ansible-playbook manage.vlans.yaml
```

Alternatively, you can use Invoke to build a docker container and execute within it. Refer to the `tasks.py` file to learn more.

```bash
$ invoke build
$ invoke create
$ invoke manage
```

If you used Ansible Vault to encrypt your secrets, you need to append the `--ask-vault-pass` to your command.

## Very Important!

Please make sure to manage your sensative information carfully. While the modules support the parameter of `api_key`, this should never be statically entered with your token in clear text.

Here are better alternatives:

### Manage your API token as an environmental

```bash
export APSTRA_API_TOKEN='YOUR_PRIVATE_KEY_HERE'
```

> you can also use `APSTRA_API_KEY`, if you prefer

### Manage your API token as a secret with Ansible Vault

create a file to store your API token in

> vim vault.yaml

```yaml
api_token: "MY_APSTRA_API_TOKEN_HERE"
```

encrypt the new file

```bash
ansible-vault encrypt vault.yml
```

and now you'll need to pass your vault password when using the playbook

```bash
ansible-playbook --ask-vault-pass test.yaml
```

## Development

Want to contribute? Great!

Submit a PR and let's work on this together
