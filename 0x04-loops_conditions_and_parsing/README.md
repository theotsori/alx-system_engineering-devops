<h1>Loops, conditions and parsing</h1>
<img src="https://miro.medium.com/max/1080/1*v4o2AXLIJaHSZmqYZk26qA.jpeg">

<h2>What is the advantage of using #!/usr/bin/env bash over #!/bin/bash</h2>
<p>Using #!/usr/bin/env bash instead of #!/bin/bash as the shebang (the line at the top of a script that specifies the interpreter to use) has the advantage of being more portable. The env command is used to run the script with the interpreter specified by the PATH environment variable, rather than a hard-coded path. This means that the script can be run on a system where the bash interpreter is located in a different directory, without the need to modify the shebang line.</p>

This is useful in situations where you don't know where the interpreter is installed or if it's installed in a non-standard location.

<h2>How to create SSH keys</h2>
To create SSH keys on a Unix-based system, such as Linux or macOS, you can use the ssh-keygen command. The basic syntax is:

Copy code
ssh-keygen -t <type> -b <bits> -C "<comment>" -f <file>
Where:

-t specifies the type of key to create. The most commonly used types are rsa and ed25519.
-b specifies the number of bits in the key. For RSA, the default is 2048 bits and for ED25519, the default is 256 bits.
-C adds a comment to the key, which can be useful for identifying the key later.
-f specifies the file to save the key in. If you don't specify a file, the default is ~/.ssh/id_rsa (or ~/.ssh/id_ed25519 for ED25519)
For example, to create a new RSA key with 4096 bits and add a comment, you can use the following command:

Copy code
ssh-keygen -t rsa -b 4096 -C "my_rsa_key"
The command will prompt you to enter a file in which to save the key and a passphrase to protect the key.

Once you've created the key, you can add it to an SSH agent with the command ssh-add <private key file>. You can also add it to a remote server using the ssh-copy-id command to be able to use it for authentication

Copy code
ssh-copy-id user@remotehost
Alternatively, you can also create SSH keys on Windows with tools like Puttygen, Git Bash or Windows Subsystem for Linux(WSL).
