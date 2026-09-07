# GeoShare

API to upload files to cloud storage and instantly generate short, shareable links for fast cross-device file sharing with no login required.

## Features

- **File Uploads:** Upload files up to 20 MB directly to Azure Blob Storage.
- **Short Links:** Automatic short URL generation via [reld.me](https://github.com/GeovaniTech/shorturl).
- **User Management:** Create user accounts.
- **File Ownership:** Link uploaded files to specific user profiles.

## Tech Stack

- **Language:** Python
- **Framework:** Flask
- **Database:** PostgreSQL
- **Cloud Storage:** Azure Blob Storage
- **URL Shortener:** [reld.me](https://github.com/GeovaniTech/shorturl)

## Prerequisites

List tools and software needed before setting up the project:
- Database instance
- Azure Blob Storage connection string

## Environment Variables

To run this project, add the following environment variables to your `.env` file:

```env
API_KEY=YOUR-API-KEY

AZURE_STORAGE_CONTAINER=YOUR-AZURE-CONTAINER
AZURE_STORAGE_CONNECTION_STRING=YOUR-AZURE-STRING-CONNECTIOn

DATABASE_NAME=YOUR-DB-NAME
DATABASE_HOST=YOUR-DB-IP-ADDRESS
DATABASE_USER=YOUR-DB-USER
DATABASE_PASSWORD=YOUR-DB-PASSWORD
DATABASE_PORT=YOUR_DB-PORT
