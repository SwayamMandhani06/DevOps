# Ansible Case Study – Automated Nginx Configuration

## Objective

Demonstrate automated configuration management using Ansible by installing and configuring Nginx on multiple Linux managed nodes.

## Architecture

```text
                    WSL Ubuntu
                Ansible Control Node
                         │
                   SSH / Ansible
                    ┌────┴────┐
                    ▼         ▼
                Server-1   Server-2
                Ubuntu     Ubuntu
                Nginx      Nginx
```

## Files
- `Dockerfile` – Builds the Ubuntu-based managed-node image with SSH, Python, Nginx and sudo.
- `inventory.ini` – Defines the Ansible managed nodes and SSH connection details.
- `install-nginx.yml` – Ansible playbook used to install Nginx and curl, start Nginx and deploy a custom web page.

## Managed Nodes

| Node | Host | SSH Port |
|---|---|---|
| Server-1 | 127.0.0.1 | 2221 |
| Server-2 | 127.0.0.1 | 2222 |

## Ansible Workflow
1. WSL Ubuntu acts as the Ansible control node.
2. Ansible connects to the managed nodes through SSH.
3. Nginx and curl are installed automatically.
4. Nginx is started and configured.
5. A custom HTML page is deployed.
6. The web server configuration is verified on both managed nodes.
7. The playbook is executed again to demonstrate idempotency.

## Important Commands

### Check inventory
```bash
ansible-inventory -i inventory.ini --graph
```

### Test connectivity
```bash
ansible all -i inventory.ini -m ping -k
```

### Validate playbook
```bash
ansible-playbook -i inventory.ini install-nginx.yml --syntax-check
```

### Execute playbook
```bash
ansible-playbook -i inventory.ini install-nginx.yml -k
```

### Verify Nginx
```bash
ansible webservers -i inventory.ini -m shell -a "nginx -v" -k
```

### Verify web page
```bash
ansible server-1 -i inventory.ini -m shell -a "curl -s http://localhost" -k
ansible server-2 -i inventory.ini -m shell -a "curl -s http://localhost" -k
```

## Result

Ansible successfully configured Nginx on multiple Linux managed nodes and deployed the same web page automatically.
