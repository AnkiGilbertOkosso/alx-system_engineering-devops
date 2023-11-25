# Setting Up SSH for Secure Server Access

## Tasks
- Task 0: Use a private key
    Write a Bash script to connect to the server using the private key ~/.ssh/school with the user ubuntu. Make use of single-character flags for ssh, avoiding -l.

- Task 1: Create an SSH key pair
    Craft a Bash script that generates an RSA key pair. The private key should be named school, have 4096 bits, and be protected by the passphrase betty.

- Task 2: Client configuration file
    Configure your local SSH client using the ~/.ssh/config file. Set it up to use the private key ~/.ssh/school and refuse authentication via password.

- Task 3: Let me in!
    Add the provided SSH public key to your server, enabling connection using the ubuntu user.

- Task 4: Client configuration file (w/ Puppet)
    Use Puppet to configure the client SSH file. Set it up to use the private key ~/.ssh/school and refuse authentication via password.
