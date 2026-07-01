touch simple-file.txt
ls -ltr

-rw-r--r-- 1 AzureAD+AndreFarinha 4096    0 Jul  1 15:22 simple-file.txt

chmod 744 simple-file.txt
ls -ltr

-rwxr--r-- 1 afarinha afarinha    0 Jul  1 15:25 simple-file.txt

-rw-r--r--
│ │  │  │
│ │  │  └── others permissions: read only
│ │  └───── group permissions: read only
│ └──────── owner permissions: read + write
└────────── file type: - means file, d means directory