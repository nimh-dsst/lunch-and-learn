# Website Automation Tools

## 12/17/2024

## Pain Points for Automatic Static Website Deployment

A member of DSST L&L described their challenge in deploying a static website hosting several large files. Here is a list of challenges and proposed solutions:

### Website Design/Building

Many free tools have emerged for designing static web pages from files hosted on a GitHub page:

- [Jekyll](https://jekyllrb.com/): Jekyll is a static site generator written in Ruby that transforms plain text file (usually Markdown) into static websites and blogs. It has integration with GitHub Pages for hosting.
- [Pelican](https://getpelican.com/): Pelican is a Python-based static site generator that converts content files (Markdown/reStructuredText) into HTML websites.
- [Read-The-Docs](https://about.readthedocs.com/): Read-The-Docs  is a documentation hosting platform that builds and hosts documentation from version-controlled code. It supports multiple documentation formats (Sphinx, MkDocs, Jupyter) and integrates with GitHub/GitLab webhooks. DSST's own [documents website](https://dsst.readthedocs.io/en/latest/) uses Read-The-Docs for building and hosting.

All these platforms have the ability to take Markdown files or other types of easier-to-write-than-HTML-and-CSS files and convert them into webpages. However, website generation requires the use of templates. While there are a variety of templates for each of these platforms, getting the template and the source file to looks a particular was described as "not fun."

### Website Hosting and File Size Limitations

The platforms listed above integrate with a free hosting service, such as [GitHub Pages](https://pages.github.com/) or [Read-The-Docs](https://about.readthedocs.com/). This prevents the designer from having to deploy to a dedicated web server. However, this also means that any files hosted one the website need to "fit" in GitHub.

#### GitHub File Size Limits

According to the [GitHub's Documentation](https://docs.github.com/en/enterprise-cloud@latest/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits):

- **25 MiB** for files using Browser Upload
- **>50 MiB** will result in a warning
- **100 MiB** is the upper limit
- **1 to 5 GB** is the limit for repository size.

### Working with large files

Since large files or large amounts of files cannot be placed on GitHub, a hybrid approach must be used.

#### Cloud Storage Integration with Links

Files can be stored in Amazon S3, Google Cloud Storage, or Azure Blob Storage. Download links to the files can be placed on the webpage. However, these services are not free. A similar download link can be generated using Microsoft SharePoint for users with NIH credentials. However, NIH prohibits the generation of public access links.

Free hosting services, such as [Open Science Foundation](https://osf.io/), are available to host scientific content. Links to the OSF project or download links can be generated.

#### Automating File Uploads to a Private Server

While cloud storage integration is a viable option for private or public file storage, another approach is to build an automation pipeline to upload files to a private server. This method avoids reliance on web-hosting services like GitHub Pages or Read-the-Docs. Instead, you can use the same website design and build tools discussed earlier to generate the site locally, then upload the built site to your server. An automated file synchronizer can ensure the site's assets remain up to date.

Tools like the lower level [rsync](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories) or the more sophisticated platform [Ansible](https://docs.ansible.com/ansible/latest/index.html) can synchronize files between a local machine and a web server. Rsync is excellent for efficiently syncing directories and files, while Ansible provides a more comprehensive solution for managing inventory, deploying software, and configuring servers.

These tools enable seamless automation of file synchronization but require access to a private server. For NIH users, this may involve provisioning through the NIH Center for Information Technology (CIT).

#### Automating Infrastructure Provisioning and Deployment

While this falls out of scope for most NIH employees, users can provision their own cloud infrastructure, such as web servers and S3 buckets, using Infrastructure-as-Code (IaC) tools like [Terraform](https://www.terraform.io/). IaC enables the definition and management of infrastructure resources through code, ensuring consistency and repeatability across deployments. Using simple text-based configuration files, users can specify cloud resources, such as S3 storage buckets and EC2 instances, for file and web hosting, respectively. In addition, Ansible can be used to set up software environments, install dependencies, and synchronize file inventories on the provisioned services. The combination of Terraform for provisioning and Ansible for configuration allows for a seamless and automated infrastructure deployment process.
