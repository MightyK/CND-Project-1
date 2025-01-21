# GCP Project Documentation

## Table of Contents
- [Project Information](#project-information)
- [Introduction](#introduction)
- [Architecture & Implementation](#architecture--implementation)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Pros & Cons](#pros--cons)
  - [Pros](#pros)
  - [Cons](#cons)
- [Problems Encountered & Solutions](#problems-encountered--solutions)
- [Application Instructions](#application-instructions)
- [Lessons Learned](#lessons-learned)

---

## Project Information
- **GCP Project Name**: `cnd-project1`
- **GCP Project ID**: `cnd-project1`
- **GCP Project Console**: [GCP Console Link](https://console.cloud.google.com/home/dashboard?cloudshell=true&hl=en&orgonly=true&project=cnd-project1&supportedpurview=organizationId)
- **Cloud Run Service Name**: `cnd-project1`
- **App URL**: [App URL](https://cnd-project1-784063327222.us-south1.run.app)

---

## Introduction
This project focuses on utilizing the Python library Flask to enable users to upload images to a cloud storage container, allowing them to access or view these images later. The project involves migrating storage facilities from local systems to the cloud for better scalability and functionality.

---

## Architecture & Implementation

The architecture of this project consists of a client-side frontend that interfaces with a cloud database via HTTP GET & POST requests using Python's Flask framework on the backend. Both the frontend and backend require Flask and Gunicorn as dependencies. The backend relies on Google Cloud Storage for cloud functionality.

 
<div align="center">
  <img src="https://github.com/user-attachments/assets/533274df-ec01-4a47-a693-8ede36201e77" alt="image">
</div>

### Frontend
The frontend is responsible for user interactions. Users can upload images through the frontend and view previously uploaded images stored in the cloud.

**Frontend Overview:**
- Enables image uploads.
- Displays stored images for viewing.
<div align="center">
  <img src="https://github.com/user-attachments/assets/04682f0a-40c4-4c42-af2d-2ae73a242110" alt="Figure 1: Frontend implementation">
  <p><strong>Figure 1:</strong> Frontend implementation.</p>
</div>




### Backend
The backend, implemented with Flask, handles routing of user requests and cloud storage operations. It is hosted on Google Cloud Run to ensure scalability and availability.

**Backend Functionality:**
- Validates file formats.
- Interacts with Google Cloud Storage to upload files.
<div align="center">
  <img src="https://github.com/user-attachments/assets/fb134c23-9b88-4e54-977f-3816cdaf1bab" alt="Figure 2: Uploading to a bucket in cloud storage">
  <p><strong>Figure 2:</strong> Uploading to a bucket in cloud storage.</p>
</div>

- Lists and retrieves files for users.

<div align="center">
  <img src="https://github.com/user-attachments/assets/7dabf970-81f3-4ef0-bdaf-3b27a943e892" alt="Figure 3: Implementation for listing files">
  <p><strong>Figure 3:</strong> Implementation for listing files.</p>
</div>


**Key Processes:**
1. **Uploading Images**: Images are validated and uploaded to a cloud storage bucket.
2. **Listing Files**: Retrieves the list of file names from the bucket for display.
3. **Fetching Specific Files**: Allows users to view any selected image.

<div align="center">
  <img src="https://github.com/user-attachments/assets/17c103bb-b52d-4dc9-a52a-f6d822eeeb03" alt="Figure 4: Implementation for getting a single file">
  <p><strong>Figure 4:</strong> Implementation for getting a single file.</p>
</div>


---

## Pros & Cons

### Pros
1. **Less Overhead**:
   - Cloud Storage handles data storage, backups, security, and access, reducing maintenance needs.
   - Cloud Run provides regional access and eliminates the need for local hosting.

2. **Loose Coupling**:
   - Integrates cloud storage with minimal dependency, improving maintainability.

3. **Stateless Integration**:
   - Scales automatically with user demand, enabling efficient handling of high traffic.

### Cons
1. **Infrastructure as a Service (IaaS)**:
   - Costs associated with Cloud Storage increase as usage grows.

2. **Platform as a Service (PaaS)**:
   - Hosting and serving through Cloud Run incurs costs proportional to application scaling.

3. **Data Availability**:
   - Cloud storage is susceptible to cyber-attacks and outages, potentially impacting access.

---

## Problems Encountered & Solutions

### Problem
- Difficulty accessing and displaying images stored in the Cloud Storage bucket via hyperlinks on the frontend.

### Solution
- Studied the storage structure and methods of access.
- Dynamically generated public URLs for each stored image to allow users to view them on the frontend.

---

## Application Instructions
1. Navigate to the application using the provided [App URL](https://cnd-project1-784063327222.us-south1.run.app).
2. Click the upload button to select an image.
3. After selecting an image, click the upload button to send it to the cloud.
4. View any uploaded image by selecting its filename from the displayed image library.

<div align="center">
  <img src="https://github.com/user-attachments/assets/875e5bda-204d-4c6d-9fe0-f4ec10a2655e" alt="Figure 5: Application Demo">
  <p><strong>Figure 5:</strong> Demonstration of the applications usage.</p>




---

## Lessons Learned
1. Gained insights into the principles and practicalities of cloud computing.
2. Learned the process of deploying applications to the cloud using Google Cloud Run.
3. Integrated cloud storage (Google Cloud Storage) for user data management.
4. Leveraged Flask for making cloud-based HTTP requests.
