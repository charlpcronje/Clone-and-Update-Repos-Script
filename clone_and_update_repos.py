# clone_and_update_repos.py

import json
import os
import subprocess

# Step 1: Load repository URLs from a JSON file
def load_repos(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data['repositories']

# Step 2: Clone each repository
def clone_repo(repo_url):
    subprocess.run(["git", "clone", repo_url])

# Step 3: Rename the cloned folders to replace .cronje.me with .webally.co.za
def rename_folder(old_name, new_name):
    os.rename(old_name, new_name)

# Step 4: Scan through all files in the folders to replace occurrences of cronje.me with webally.co.za
def replace_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace(old_string, new_string)
    with open(file_path, 'w') as file:
        file.write(content)

def update_links_in_folder(folder, old_string, new_string):
    for subdir, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(subdir, file)
            if os.path.isfile(file_path):
                try:
                    replace_in_file(file_path, old_string, new_string)
                except Exception as e:
                    print(f"Could not update {file_path}: {e}")

# Step 5: Create a logs folder inside each repo's folder
def create_logs_folder(repo_folder):
    logs_path = os.path.join(repo_folder, 'logs')
    os.makedirs(logs_path, exist_ok=True)

# Step 6: Create virtual host configurations for each repository
def create_vhost_config(repo, template):
    return template.replace("{repo}", repo)

# Step 7: Write all virtual host configurations into a single file called vhosts.conf
def write_vhosts_file(vhosts, output_file):
    with open(output_file, 'w') as file:
        file.write("\n".join(vhosts))

def main():
    repos = load_repos('repos.json')
    vhost_template = """
    # {repo}
    <VirtualHost 212.227.241.186:82>
        ServerName {repo}
        ServerAdmin charl@webally.co.za
        DocumentRoot /var/www/docs/{repo}/public
        <Directory /var/www/docs/{repo}/public>
            Require all granted
            Options -Indexes +FollowSymLinks
            AllowOverride All
        </Directory>
        ErrorLog /var/www/docs/{repo}/logs/error.log
        CustomLog /var/www/docs/{repo}/logs/access.log combined 
    </VirtualHost>
    """

    vhosts = []

    for repo in repos:
        repo_name = repo.split('/')[-1].replace('.git', '')
        new_name = repo_name.replace('.cronje.me', '.webally.co.za')

        clone_repo(repo)  # Step 2
        rename_folder(repo_name, new_name)  # Step 3
        update_links_in_folder(new_name, 'cronje.me', 'webally.co.za')  # Step 4
        create_logs_folder(new_name)  # Step 5

        vhost_config = create_vhost_config(new_name, vhost_template)  # Step 6
        vhosts.append(vhost_config)

    write_vhosts_file(vhosts, 'vhosts.conf')  # Step 7

if __name__ == "__main__":
    main()
