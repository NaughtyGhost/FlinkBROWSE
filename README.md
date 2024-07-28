# FlinkBROWSE is a fast, secure proxy built especially for Flink (https://www.flink.lol), and made for evading scrutiny and freely accessing possibly blocked websites.
# Here's a step-by-step guide to using FlinkBROWSE locally:
**1) Using a Terminal or Command Prompt: open a terminal or command prompt on your computer.**

Create a new directory by running the command 'mkdir flinkbrowse-proxy'
Navigate into the new directory:

cd flinkbrowse-proxy

Create a new file called docker-compose.yml and add the contents provided:

nano docker-compose.yml

Paste the contents into the file and save it by pressing Ctrl+X, then Y, and finally Enter. 5. Create a new file called Dockerfile and add the contents provided:
nano Dockerfile
Paste the contents into the file and save it by pressing Ctrl+X, then Y, and finally Enter. 6. Create a new file called nginx.conf and add the contents provided:

nano nginx.conf

Paste the contents into the file and save it by pressing Ctrl+X, then Y, and finally Enter. 7. Create a new file called index.html and add the contents provided:

nano index.html

Paste the contents into the file and save it by pressing Ctrl+X, then Y, and finally Enter. 8. Create a new file called flinkbrowse_proxy.py and add the contents provided:

nano flinkbrowse_proxy.py

Paste the contents into the file and save it by pressing Ctrl+X, then Y, and finally Enter. 9. Create a new file called requirements.txt and add the contents provided:

nano requirements.txt

Paste the contents into the file and save it by pressing Ctrl+X, then Y, and finally Enter. 10. Run the following command to start the containers:

docker-compose up

 his will start the Nginx and FlinkBROWSE proxy servers. You can access the FlinkBROWSE proxy server by visiting http://localhost in your web browser.

**2)Using a Graphical User Interface**

Create a new directory on your computer by right-clicking on the desktop and selecting "New Folder".
Name the folder flinkbrowse-proxy.
Open the folder and create a new file called docker-compose.yml. You can do this by right-clicking inside the folder and selecting "New File".
Open the file in a text editor and paste the contents provided. Save the file by clicking "File" > "Save" or by pressing Ctrl+S.
Repeat steps 3-4 for the Dockerfile, nginx.conf, index.html, flinkbrowse_proxy.py, and requirements.txt files.
Once you have created all the files, open a terminal or command prompt and navigate to the flinkbrowse-proxy directory.
Run the following command to start the containers:

docker-compose up

This will start the Nginx and FlinkBROWSE proxy servers. You can access the FlinkBROWSE proxy server by visiting http://localhost in your web browser.

Note: Make sure you have Docker and Docker Compose installed on your computer before running the code. You can download the latest versions from the official Docker website.
