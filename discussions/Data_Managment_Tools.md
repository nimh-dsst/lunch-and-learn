# Data Managment Tools

## 2/11/2025

Attendence: 9

### Introduction

DSST members and friends discussed data managment tools. We covered the following tools:

- Globus
  - [Globus](https://www.globus.org/) for data transfer.
  - [Biowulf Globus Documentation](https://hpc.nih.gov/docs/globus/setup.php)
- Linux Tools
  - [rsync](https://en.wikipedia.org/wiki/Rsync)
  - [scp](https://en.wikipedia.org/wiki/Secure_copy)
- Third Party Tools
  - [rclone](https://rclone.org/) for syncing data between cloud storage providers. "The Swiss army knife of cloud storage"
  - [Quantum](https://www.quantum.com/) for syncing data between cloud storage providers.
  - [Cohesity](https://www.cohesity.com/) for syncing data between on-premises and cloud storage providers.
- Cloud Storage Providers
  - [AWS S3](https://aws.amazon.com/s3/)
  - [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)
  - [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/)
  - [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/)
  - [Google Cloud Storage](https://cloud.google.com/storage)
  - [Google Cloud CLI](https://cloud.google.com/cli)
- Old School Tools
  - Get a Linux server data server and backup on magnetic tape.

### Discussion

A few attendees shared their experiences with data managment tools:

- Syncing a large number of files between local and cloud storage with OneDrive has significant performance issues.
- Beware using free cloud storage services for long term data storage. You don't own the data storage and it can be deleted by the service provider.
- [Iron Mountain](https://www.ironmountain.com/) is a good option for long term data storage. They primarily use magnetic tape storage.
- One group's data storage strategy is to have a Linux data server. Each Post-Doc gets their own directory. Any Post-Bac trainees data goes in the Post-Doc's directory too. Tertiary storage was google cloud at one point, but was not found to be cost effective.
- The new solid state drives degrade over time and are not suitable for archival storage.
