# Clone and Update Repos Script

This script automates the process of cloning multiple repositories, renaming the cloned folders, updating links within the files, creating logs folders, and generating virtual host configurations.

## Prerequisites

- Python 3.x
- Git
- JSON file containing the list of repositories

## Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/charlpcronje/Clone-and-Update-Repos-Script
   cd Clone-and-Update-Repos-Script
   ```

2. **Create the `repos.json` file:**

   Create a file named `repos.json` in the same directory as the script with the following structure:

   ```json
   {
     "repositories": [
       "https://github.com/charlpcronje/php.docs.cronje.me.git",
       "https://github.com/charlpcronje/setup.docs.cronje.me.git",
       "https://github.com/charlpcronje/docs.cronje.me.git",
       "https://github.com/charlpcronje/bash.docs.cronje.me.git",
       "https://github.com/charlpcronje/ai.docs.cronje.me.git",
       "https://github.com/charlpcronje/win.docs.cronje.me.git",
       "https://github.com/charlpcronje/troubleshoot.docs.cronje.me.git",
       "https://github.com/charlpcronje/trading.docs.cronje.me.git",
       "https://github.com/charlpcronje/tools.docs.cronje.me.git",
       "https://github.com/charlpcronje/tips.docs.cronje.me.git",
       "https://github.com/charlpcronje/saas.docs.cronje.me.git",
       "https://github.com/charlpcronje/repos.docs.cronje.me.git",
       "https://github.com/charlpcronje/reports.docs.cronje.me.git",
       "https://github.com/charlpcronje/projects.docs.cronje.me.git",
       "https://github.com/charlpcronje/perl.docs.cronje.me.git",
       "https://github.com/charlpcronje/opensource.docs.cronje.me.git",
       "https://github.com/charlpcronje/notes.docs.cronje.me.git",
       "https://github.com/charlpcronje/mongo.docs.cronje.me.git",
       "https://github.com/charlpcronje/kali.docs.cronje.me.git",
       "https://github.com/charlpcronje/js.docs.cronje.me.git",
       "https://github.com/charlpcronje/heepp.docs.cronje.me.git",
       "https://github.com/charlpcronje/hacking.docs.cronje.me.git",
       "https://github.com/charlpcronje/gist.docs.cronje.me.git",
       "https://github.com/charlpcronje/dns.docs.cronje.me.git",
       "https://github.com/charlpcronje/dev.docs.cronje.me.git",
       "https://github.com/charlpcronje/crypto.docs.cronje.me.git",
       "https://github.com/charlpcronje/backup.docs.cronje.me.git",
       "https://github.com/charlpcronje/arm.docs.cronje.me.git",
       "https://github.com/charlpcronje/android.docs.cronje.me.git",
       "https://github.com/charlpcronje/onion.docs.cronje.me.git",
       "https://github.com/charlpcronje/docker.docs.cronje.me.git",
       "https://github.com/charlpcronje/repos.docs.devserv.me.git",
       "https://github.com/charlpcronje/shell.docs.cronje.me.git",
       "https://github.com/charlpcronje/freelance.docs.devserv.me.git",
       "https://github.com/charlpcronje/pentesting.docs.cronje.me.git"
     ]
   }
   ```

3. **Run the Script:**
   ```bash
   python clone_and_update_repos.py
   ```

## Script Breakdown

1. **Load repository URLs from a JSON file:**
   The script reads the repository URLs from `repos.json`.

2. **Clone each repository:**
   It clones each repository into the current directory.

3. **Rename the cloned folders:**
   It renames each cloned folder, replacing `.cronje.me` with `.webally.co.za`.

4. **Update links within the files:**
   The script scans all files in the folders and replaces occurrences of `cronje.me` with `webally.co.za`.

5. **Create logs folder:**
   It creates a `logs` folder inside each renamed repository folder.

6. **Generate virtual host configurations:**
   The script generates a virtual host configuration for each repository using a predefined template.

7. **Write virtual host configurations to `vhosts.conf`:**
   All virtual host configurations are written into a single file named `vhosts.conf`.

## Virtual Host Template

The virtual host template used by the script:

```apache
# {repo}
<VirtualHost {your ip address}:80>
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
```

## Notes

- Make sure you have the necessary permissions to clone the repositories and create folders/files in the target directory.
- Customize the script as needed to fit your specific requirements.

## License

This project is licensed under the MIT License.
