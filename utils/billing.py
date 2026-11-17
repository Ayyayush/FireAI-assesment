# --------------------------------------------------
# PRINTING RATES
# --------------------------------------------------

PRINT_RATE = 5
PHOTOCOPY_RATE = 3


# --------------------------------------------------
# GET RATE
# --------------------------------------------------


def get_rate(print_type):
    """
    Return the rate based on the printing type.
    """

    rates = {"Printout": PRINT_RATE, "Photocopy": PHOTOCOPY_RATE}

    if print_type not in rates:
        raise ValueError("Invalid print type.")

    return rates[print_type]


# --------------------------------------------------
# CALCULATE COST
# --------------------------------------------------


def calculate_cost(pages, copies, print_type):
    """
    Calculate total printing or photocopying cost.

    Formula:
    Total = Pages * Copies * Rate
    """

    if isinstance(pages, bool) or not isinstance(pages, int) or pages <= 0:
        raise ValueError("Pages must be a positive integer.")

    if isinstance(copies, bool) or not isinstance(copies, int) or copies <= 0:
        raise ValueError("Copies must be a positive integer.")

    rate = get_rate(print_type)

    total = pages * copies * rate

    return {
        "pages": pages,
        "copies": copies,
        "print_type": print_type,
        "rate_per_page": rate,
        "total": total,
    }


# --------------------------------------------------
# FORMAT BILL
# --------------------------------------------------


def format_bill(bill):
    """
    Generate a readable cost summary.
    """

    return (
        f"Printing Type: {bill['print_type']}\n"
        f"Pages: {bill['pages']}\n"
        f"Copies: {bill['copies']}\n"
        f"Rate per Page: Rs. {bill['rate_per_page']}\n"
        f"Total Amount: Rs. {bill['total']}"
    )
