
1. Install if needed
    sudo apt update
    sudo apt install acl
2. Atual ACL
    getfacl simple-file.txt
        # file: simple-file.txt
        # owner: afarinha
        # group: afarinha
        user::rw-
        group::r--
        other::r--

    setfacl -m u:devopsuser1:rw simple-file.txt
    getfacl simple-file.txt
        # file: simple-file.txt
        # owner: afarinha
        # group: afarinha
        user::rw-
        user:devopsuser1:rw-
        group::r--
        mask::rw-
        other::r--

    setfacl -x u:devopsuser1 simple-file.txt
    setfacl -b simple-file.txt
        # file: simple-file.txt
        # owner: afarinha
        # group: afarinha
        user::rw-
        group::r--
        other::r--