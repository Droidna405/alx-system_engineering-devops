# 0x0D. Web Stack Debugging #0

## Overview

Welcome to the **Web Stack Debugging #0** project! This is a part of the ongoing series that trains you in the art of web stack debugging. This project is focused on debugging a web stack to ensure that the necessary components are running correctly.

## Project Details

- **Project Type:** DevOps, SysAdmin, Scripting, Debugging
- **Weight:** 1
- **Status:** Ongoing (second chance project)
- **Start Date:** July 1, 2024, 6:00 AM
- **End Date:** July 4, 2024, 6:00 AM
- **Auto Review Deadline:** July 4, 2024, 6:00 AM

## Project Requirements

### General

- Use allowed editors: `vi`, `vim`, `emacs`.
- Your scripts must be compatible with Ubuntu 14.04 LTS.
- Ensure all files end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All Bash scripts must be executable.
- Scripts must pass `Shellcheck` without any errors.
- Scripts should run without errors.
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line should be a comment explaining the script's purpose.

### Resources

- Use `man` or `help` for commands like `curl`.

### Concepts

For this project, focus on understanding:

- Network basics
- Docker
- Web stack debugging

## Background Context

Debugging is a critical skill for a Full-Stack Software Engineer. This project provides broken or bugged web stacks that you need to debug and fix. Your goal is to come up with a Bash script that brings the web stack back to a working state.

For example, a server might require:

- A copy of the `/etc/passwd` file in `/tmp`.
- A file named `/tmp/isworking` containing the string `OK`.

If these conditions aren't met, the web application won't work. Your task is to manually fix these issues before writing the Bash script.

### Example

Let's debug a basic scenario:

```bash
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
# Start a Docker container

vagrant@vagrant:~$ docker ps
# List running containers

vagrant@vagrant:~$ docker exec -ti <container_id> /bin/bash
# Enter the container

root@<container_id>:/# cp /etc/passwd /tmp/
# Copy /etc/passwd to /tmp

root@<container_id>:/# echo OK > /tmp/isworking
# Create /tmp/isworking with content 'OK'

root@<container_id>:/# ls /tmp/
# Check contents of /tmp
isworking  passwd