# Ansible playbook

Ansible playbook for completing the [labs of System Administration course](https://courses.cs.ut.ee/2022/sa/spring/Main/Labs) at University of Tartu.

## Dependencies

To install any additional ansible dependencies run:
```sh
ansible-galaxy install -r requirements.yml
```

## Usage

To run the ansible playbooks against the defined hosts in [`inventory/hosts`](./inventory/hosts) use:
```sh
ansible-playbook playbook.yml -i inventory
```

To only run tasks with a specific tag, for example only hardening ssh config:
```sh
ansible-playbook playbook.yml -i inventory -t ssh
```
