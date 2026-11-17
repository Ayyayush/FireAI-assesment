
# Research — Print Job Register

## 1. Problem Identification

During my visit to a local printing and stationery shop, I observed that the shop handles different types of work, including printing, photocopying, paper binding and stationery sales.

The shopkeeper receives documents through different channels. Some customers send their documents through WhatsApp or email, while others bring physical documents directly to the shop for photocopying.

During our conversation, the shopkeeper mentioned that keeping track of which customer sent which document can sometimes become difficult. Documents may also arrive in a different order from the sequence in which they need to be printed. Maintaining accurate page counts for individual jobs is another challenge.

Apart from this, I considered other possible difficulties in a small stationery and printing shop, such as monitoring product stock and calculating printing charges for different orders.

## 2. Problems Identified

### Problem 1: Printing and Photocopy Job Management

This is the primary problem identified during my conversation with the shopkeeper.

- Documents are received through WhatsApp, email and directly from customers.
- Multiple documents may arrive at different times.
- It can become difficult to identify which document belongs to which customer.
- Documents may need to be printed in a different order from the order in which they were received.
- Page counts and copy requirements need to be maintained for individual jobs.
- When multiple customers are waiting, keeping track of pending and completed jobs becomes important.

**Proposed solution:**

A Print Job Register that records incoming printing and photocopying jobs, assigns unique job IDs, maintains customer and document references, records page counts and organizes jobs according to their requested printing sequence.

### Problem 2: Stationery Stock Monitoring

The shop also sells stationery products such as pens, erasers and other small accessories.

One possible difficulty in a small stationery business is maintaining an accurate record of available stock. Frequently purchased products may run out unexpectedly, while some products may remain on the shelves for longer periods.

**Proposed solution:**

A simple stock monitoring tool that records product quantities, tracks stock movement and identifies products that may need restocking.

This is a potential problem and requires further confirmation from the shopkeeper.

### Problem 3: Printing Cost Calculation

Different printing and photocopying jobs can have different page counts, copy requirements and printing types.

For example, black-and-white and colour printing may have different rates. Calculating the total cost of a larger order can require additional manual effort.

**Proposed solution:**

A printing cost calculator that calculates estimated charges based on page count, number of copies, printing type and the shop's actual rates.

This problem also requires further confirmation.

## 3. Selected Problem

After considering the different possibilities, I decided to focus on printing and photocopy job management.

The main reason is that the shopkeeper specifically mentioned difficulties related to identifying customer documents, maintaining the correct printing sequence and tracking page counts.

Since documents arrive through different channels, there is a need for a common place to register and organize all incoming jobs.

The objective is to develop a simple tool that helps the shopkeeper maintain job records without having to repeatedly search through WhatsApp conversations, emails or physical documents.

## 4. Existing Solutions and Their Limitations

### Solution 1: WhatsApp Business

Website: https://whatsappbusiness.com/products/business-app-features/

WhatsApp Business provides features that help small businesses manage customer conversations.

Some relevant features include:
- Labels for organizing customer conversations.
- Quick replies for frequently asked questions.
- Customer communication management.
- Tools for organizing and filtering important messages.

**Why it may not fully fit this requirement:**

WhatsApp Business helps organize customer conversations, but the shopkeeper also receives documents through email and physical visits.

It does not provide one consolidated printing-job register for recording page counts, copy requirements and requested printing sequences across these different channels.

A dedicated job register could provide a common place to maintain these details.

### Solution 2: Google Sheets

Website: https://workspace.google.com/intl/en_in/products/sheets/

Google Sheets is a spreadsheet application that can be used to organize structured records.

Some relevant features include:
- Maintaining customer and document records.
- Sorting and filtering information.
- Organizing data into tables.
- Updating records when job details change.

**Why it may not fully fit this requirement:**

Although Google Sheets can store printing-job information, the shopkeeper would need to manually create and maintain the required structure.

A dedicated interface with predefined fields, a pending-job view and printing-sequence management could make the workflow easier to use.

## 5. Research Sources

### Source 1: WhatsApp Business — Business App Features

Link: https://whatsappbusiness.com/products/business-app-features/

Notes:
1. The official website describes tools available to businesses for managing customer conversations.
2. It explains how labels can help organize and filter important customer conversations.
3. These features are relevant because WhatsApp is one of the channels through which the shopkeeper receives customer documents.

### Source 2: Google Sheets — Sort and Filter Data

Link: https://support.google.com/docs/answer/3540681?hl=en

Notes:
1. The official Google documentation explains how spreadsheet data can be sorted alphabetically or numerically.
2. It describes how filters can be used to find specific records.
3. These features can support printing-job records, although a dedicated application would provide a more focused workflow.

## 6. Proposed Solution

I propose developing a lightweight application called **Print Job Register**.

The application will help the shopkeeper:

1. Register incoming printing and photocopying jobs.
2. Record the source of each job: WhatsApp, email or physical document.
3. Assign a unique job ID to every order.
4. Associate documents with anonymous customer identifiers.
5. Maintain document labels and received timestamps.
6. Record page counts and the number of copies.
7. Record printing type (Black & White / Colour).
8. Maintain the requested printing sequence independently of arrival time.
9. View pending, printing and completed jobs.
10. Calculate estimated printing charges using actual shop rates, if confirmed as useful.

The application will use a CSV file containing genuine printing-job records collected during fieldwork.

The initial version will not require automatic integration with WhatsApp or email. The shopkeeper will manually enter the relevant job details into the application.

## 7. Initial Technology and Scope

**Proposed technologies:**
- Python
- Pandas
- Streamlit
- CSV

**Features included:**
- Printing and photocopy job registration.
- Customer and document identification.
- Source/channel tracking.
- Page-count and copy tracking.
- Printing sequence management.
- Pending and completed job tracking.
- CSV data validation.
- Basic printing cost calculation, if verified as useful.

**Features excluded:**
- Automatic WhatsApp integration.
- Automatic email integration.
- Online payments.
- GST billing.
- Full inventory management.
- Customer-facing portals.
- Unnecessary business analytics.

## 8. Research Status

- [x] Personally visited a local printing and stationery shop.
- [x] Identified the printing-document management problem through conversation.
- [x] Identified the different document-receiving channels.
- [x] Considered two additional potential problems.
- [x] Researched two existing solutions.
- [x] Prepared an initial solution direction.
- [ ] Verify the shopkeeper's current method of organizing incoming documents.
- [ ] Confirm how requested printing sequences are maintained.
- [ ] Verify whether printing-cost calculation is a significant problem.
- [ ] Collect at least 20 genuine printing and photocopy job records.
- [ ] Finalize application features based on fieldwork.
