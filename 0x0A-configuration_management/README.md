# 0x0A. Configuration Management
### DevOps, SysAdmin, scripting, CI/CD
by Joel Mwangala <joemwangala@gmail.com>

Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet


# Puppet File Creation Example

This project demonstrates the use of Puppet to create a file with specified properties. The Puppet manifest `0-create_a_file.pp` creates a file `/tmp/school` with the following attributes:

- **File Path**: `/tmp/school`
- **File Permissions**: `0744`
- **File Owner**: `www-data`
- **File Group**: `www-data`
- **File Content**: `I love Puppet`

## How to Use

1. **Check Puppet-Lint Version**:
   ```bash
      puppet-lint --version