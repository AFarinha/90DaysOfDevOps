### Create, List and Delete users
1. Create
    sudo useradd -m devopsuser1
    sudo useradd -m devopsuser2
2. List
    getent passwd devopsuser1 devopsuser2 | cut -d: -f1
3. Delete
    sudo userdel -r devopsuser1
    sudo userdel -r devopsuser2