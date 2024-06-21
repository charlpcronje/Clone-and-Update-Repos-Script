#!/bin/bash

# cleanup_repos.sh
# This script deletes all the cloned and renamed folders.

# List of folders to delete
folders=(
    "php.docs.webally.co.za"
    "setup.docs.webally.co.za"
    "docs.webally.co.za"
    "bash.docs.webally.co.za"
    "ai.docs.webally.co.za"
    "win.docs.webally.co.za"
    "troubleshoot.docs.webally.co.za"
    "trading.docs.webally.co.za"
    "tools.docs.webally.co.za"
    "tips.docs.webally.co.za"
    "saas.docs.webally.co.za"
    "repos.docs.webally.co.za"
    "reports.docs.webally.co.za"
    "projects.docs.webally.co.za"
    "perl.docs.webally.co.za"
    "opensource.docs.webally.co.za"
    "notes.docs.webally.co.za"
    "mongo.docs.webally.co.za"
    "kali.docs.webally.co.za"
    "js.docs.webally.co.za"
    "heepp.docs.webally.co.za"
    "hacking.docs.webally.co.za"
    "gist.docs.webally.co.za"
    "dns.docs.webally.co.za"
    "dev.docs.webally.co.za"
    "crypto.docs.webally.co.za"
    "backup.docs.webally.co.za"
    "arm.docs.webally.co.za"
    "android.docs.webally.co.za"
    "onion.docs.webally.co.za"
    "docker.docs.webally.co.za"
    "repos.docs.devserv.me"
    "shell.docs.webally.co.za"
    "freelance.docs.devserv.me"
    "pentesting.docs.webally.co.za"
)

# Loop through each folder and delete it
for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "Deleting folder: $folder"
        rm -rf "$folder"
    else
        echo "Folder not found: $folder"
    fi
done

echo "Cleanup completed."
