# Web Stack Debugging #3

## Overview
This project focuses on debugging a WordPress website running on a LAMP stack (Linux, Apache, MySQL, PHP). The task is to identify the root cause of Apache returning 500 Internal Server Error and fix it using Puppet.

## Task
- Use `strace` to debug why Apache is returning a 500 error
- Automate the fix using Puppet instead of Bash scripts
- Create a Puppet manifest file that resolves the issue

## Files
- `0-strace_is_your_friend.pp`: Puppet manifest to fix the 500 error issue

## Requirements
- All files interpreted on Ubuntu 14.04 LTS
- All files end with a new line
- Puppet manifests pass `puppet-lint` version 2.1.1
- First line of Puppet manifests include a comment explaining the manifest
- Files end with the extension `.pp`

## Installation
To install puppet-lint:
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Solution Approach
1. Use `strace` to attach to the Apache process and monitor system calls
2. Identify the issue causing the 500 error (in this case, a typo in the WordPress configuration)
3. Create a Puppet manifest to automatically fix the issue
4. Verify the fix by checking the Apache server response