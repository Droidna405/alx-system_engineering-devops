# Web Stack Debugging 3

Using Strace

# Project Summary

In this project, I am focusing on debugging a LAMP stack (Linux, Apache, MySQL, and PHP) that is running a WordPress website. I will use strace to diagnose the cause of a 500 Internal Server Error in Apache and then automate the fix using Puppet.

## Concepts Covered

- Web Server
- Web Stack Debugging

## Background

Debugging can be challenging, especially when logs don't provide enough information. In such cases, tools like strace are invaluable for analyzing system calls made by processes.

## Project Details

- **Duration:** August 13, 2024 (6:00 AM) - August 15, 2024 (6:00 AM)
- **Platform:** Ubuntu 14.04 LTS
- **Deliverables:**
  - A `README.md` file
  - A Puppet manifest (`0-strace_is_your_friend.pp`) that fixes the issue identified with strace
- **Requirements:**
  - All files must have a newline character at the end.
  - Puppet manifests must:
    - Pass `puppet-lint` v2.1.1 without errors
    - Run without errors
    - Start with a comment explaining the purpose
    - End with the `.pp` extension
  - Use strace to diagnose the cause of the 500 error in Apache.
  - Automate the fix using Puppet (instead of Bash).

## Additional Information

To install `puppet-lint`:
```bash
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
