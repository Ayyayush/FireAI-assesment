# Research: PrintDesk — Print Shop Assistant

## 1. Problem Identification

Print Mega Mess is a printing and stationery shop located inside the NIT Jamshedpur campus, beside Mega Mess. The shop receives printing and photocopying requests from students through different channels, including WhatsApp, email, and physical documents. Managing the sequence of documents and keeping track of different printing requests can become difficult when multiple customers submit work. Calculating charges for large photocopying jobs, such as an entire book, also requires manually counting pages and calculating the total amount. The shop also needs a convenient way to maintain records of stationery items that require replenishment.

## 2. Person Identified

- **Shop:** Print Mega Mess
- **Location:** NIT Jamshedpur Campus, beside Mega Mess
- **Person spoken to:** Aditya
- **Role:** Shopkeeper
- **Date of visit:** 17 November 2026
- **Visit time:** 5:26 PM to 5:45 PM

## 3. Problems Observed and Discussed

During the visit and conversation with Aditya, the following problems were identified:

### Problem 1: Managing document sequence

Customers send documents through WhatsApp and email or bring physical documents to the shop. Keeping track of the order in which requests are received and the sequence in which documents need to be printed can become difficult when several jobs are being handled.

### Problem 2: Calculating printing and photocopying charges

For large documents, such as an entire book, calculating the total charge requires counting the pages and multiplying them by the applicable rate. This can become time-consuming when the document contains many pages.

The rates shared for the shop were:

- **Printout:** ₹5 per page
- **Photocopy:** ₹3 per page

### Problem 3: Maintaining stationery records

The shop also sells stationery items. Maintaining a record of available items and identifying which products need replenishment can help the shopkeeper manage stock more conveniently.

## 4. Existing Solutions Considered

### Solution 1: WhatsApp Business

WhatsApp Business provides features such as labels for organizing customer conversations and quick replies for frequently used messages.

**Why it may not fully solve this problem:**

- It can help organize conversations, but it does not provide a dedicated printing-job register.
- It does not automatically calculate printing or photocopying charges based on page counts.
- It does not maintain stationery stock quantities and replenishment thresholds.
- Requests received through email and physical documents would still need to be recorded separately.

Source: https://whatsappbusiness.com/products/business-app-features/

### Solution 2: Google Sheets

Google Sheets provides spreadsheet functionality, including sorting and filtering records.

**Why it may not fully solve this problem:**

- Job information, page counts, customer references, and document sequences would need to be entered and managed manually.
- The shopkeeper would need to maintain separate formulas and records for different tasks.
- It does not provide a dedicated job-ticket workflow by default.
- A simple custom interface could make frequently performed operations easier to access.

Source: https://support.google.com/docs/answer/3540681?hl=en

## 5. Proposed Solution

I propose building **PrintDesk — Print Shop Assistant**, a small application designed around the day-to-day requirements discussed at Print Mega Mess.

The application will use Python, Streamlit, Pandas, and CSV files to provide a simple interface for managing printing jobs and stationery records.

### Planned Features

**1. Unified Job Register**

- Record jobs received through WhatsApp, email, or physical documents.
- Store customer references and document labels.
- Maintain the received order of jobs.
- Record the requested document sequence separately.

**2. Digital Job Ticket**

- Assign a unique job ID to each entry.
- Store document name, page count, number of copies, and job type.
- Track the job status.
- Make it easier to identify and retrieve a particular printing request.

**3. Printing and Photocopy Cost Calculator**

- Calculate the estimated cost using the number of pages and copies.
- Use the shop's reported rates:
  - Printout: ₹5 per page.
  - Photocopy: ₹3 per page.
- Display the estimated total before processing a job.

**4. Basic Stationery Stock Alerts**

- Maintain records of stationery products.
- Store current quantities and minimum stock levels.
- Highlight items that need replenishment.

## 6. Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| User interface | Streamlit |
| Data processing | Pandas |
| Data storage | CSV files |
| Development environment | VS Code |

## 7. Data Collection Plan

The application will use records collected from the actual shop rather than downloaded or generated datasets.

The planned job dataset will contain:

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

A separate stock dataset will contain stationery product names, current quantities, and minimum stock levels.

Customer information and document contents will not be stored. Only the minimum information required to demonstrate job management and cost calculation will be used.

## 8. Project Scope and Limitations

PrintDesk is intended to be a small, practical tool for the identified shopkeeper. It will focus on organizing job records, calculating estimated printing charges, and identifying stationery items that need replenishment.

The initial version will not include automatic WhatsApp or email integration, online payments, OCR, customer accounts, or a full billing system. Job details will be entered manually, and the application will operate using locally stored CSV data.

The application will depend on the accuracy of the information entered. Cost estimates will use the configured per-page rates and may not account for additional services or special printing requirements.

## 9. Research Outcome

The visit helped identify practical administrative tasks in a small campus printing shop. The main opportunity is to reduce manual effort in organizing printing requests and calculating charges, while also providing a basic way to track stationery stock.

PrintDesk will be developed as a focused solution for the workflow discussed with Aditya at Print Mega Mess.