# Fieldwork: PrintDesk — Print Shop Assistant

## 1. Visit Details

- **Shop Name:** Print Mega Mess
- **Location:** NIT Jamshedpur Campus, beside Mega Mess
- **Date:** 17 November 2026
- **Visit Time:** 5:26 PM – 5:45 PM
- **Person Interviewed:** Aditya
- **Role:** Shopkeeper

I visited Print Mega Mess to understand the daily activities involved in handling printing and photocopying requests and managing stationery items. I observed the shop's working environment, the services offered, and the different products available. I also spoke with Aditya, the shopkeeper, about the difficulties involved in managing the shop.

## 2. Observations at the Shop

During the visit, I observed that the shop provides printing and photocopying services along with various stationery products.

The shop handles documents received through different channels:

- WhatsApp
- Email
- Physical documents brought directly by customers

I noticed that managing the order of incoming documents can become difficult when multiple customers send their files or bring documents around the same time.

I also observed different stationery products available in the shop, including:

- Copies and notebooks
- Lab copies
- Pens
- Pencils
- Glue
- Chocolates and toffees

These observations showed that the shop handles both printing-related work and the sale of everyday stationery products.

## 3. Conversation with the Shopkeeper

I spoke with Aditya, who explained some of the difficulties involved in managing the shop.

The main points discussed were:

1. **Maintaining document sequence:** Documents received from different customers through WhatsApp, email, or physical copies need to be managed in the correct order.

2. **Maintaining stationery records:** Keeping track of stationery products and identifying which items need replenishment is another task that requires attention.

3. **Calculating printing charges:** The charges for printing and photocopying depend on the number of pages. For larger documents, such as an entire book, counting the pages and calculating the total amount manually can require additional effort.

The rates shared by Aditya were:

| Service | Rate |
|---|---:|
| Printout | ₹5 per page |
| Photocopy | ₹3 per page |

## 4. An Unexpected Observation

One thing that stood out to me was the amount of manual calculation required for large photocopying jobs.

For example, when a customer brings an entire book for photocopying, the number of pages can be quite large. The shopkeeper needs to count the pages and calculate the total charge based on the applicable rate.

I had initially thought that calculating the charge would be a simple task, but I realised that it can become more time-consuming when the document contains a large number of pages.

This observation helped me identify the printing cost calculator as one of the useful features for the proposed application.

## 5. Problems Identified

Based on the observations and conversation, I identified three main problems:

- Managing printing requests received through multiple channels and maintaining their sequence.
- Calculating printing and photocopying charges manually, especially for large documents.
- Keeping track of stationery products and identifying items that need replenishment.

## 6. Proposed Solution

Based on the problems identified, I decided to build **PrintDesk — Print Shop Assistant**.

The application will contain the following features:

### A. Unified Job Register

A common place to record printing and photocopying requests received through WhatsApp, email, and physical documents.

### B. Digital Job Ticket

Each job will receive a unique ID, along with details such as customer reference, document name, page count, number of copies, and job status.

### C. Printing Cost Calculator

The application will calculate the estimated charge using the shop's reported rates:

- Printout: ₹5 per page.
- Photocopy: ₹3 per page.

### D. Stationery Stock Alerts

The application will maintain basic stationery records and identify products whose available quantities fall below their minimum stock levels.

## 7. Data Collection

The application is designed to work with actual records from Print Mega Mess rather than downloaded or artificially generated datasets.

The job dataset will contain 20 real printing or photocopying job entries. Each entry will contain relevant information such as:

- Job ID
- Received time
- Source channel
- Customer reference
- Document label
- Number of pages
- Number of copies
- Print type
- Requested sequence
- Job status
- Rate per page

A separate stationery dataset will be used to maintain product names, available quantities, and minimum stock levels.

Customer names, phone numbers, and private document contents will not be stored in the application. Only the information necessary for managing the jobs will be recorded.

## 8. Fieldwork Evidence

Photographs were taken during the visit to document the shop environment and the stationery products available.

The photographs provide visual evidence of the shop's printing-related setup and the different products sold there.

## 9. Fieldwork Outcome

The visit helped me understand that even a small printing and stationery shop handles several different activities simultaneously. Managing incoming documents, maintaining their sequence, calculating charges, and keeping track of stationery products all require regular attention.

The discussion with Aditya helped me narrow down the project scope to a small application that addresses these practical tasks instead of building a generic management application.