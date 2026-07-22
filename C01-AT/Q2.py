import re


 
products = [
    "Apple iPhone",
    "Apple Watch",
    "Samsung Phone",
    "Gaming Laptop",
    "Dell Laptop",
    "Wireless Mouse",
    "Gaming Mouse",
    "Bluetooth Speaker",
    "Smart Watch",
    "Mobile Charger"
]


 
def display_results(search_type, matches):

    print("\nSearch Type:", search_type)

    if matches:

        print("Matching products:")

        for product in matches:
            print("-", product)

    else:

        print("No matching products found")

    print("Total Matches:", len(matches))


 
exact_keyword = "Apple Watch"

exact_pattern = (
    "^"
    + re.escape(exact_keyword)
    + "$"
)

exact_matches = []

for product in products:

    if re.search(
        exact_pattern,
        product,
        re.IGNORECASE
    ):

        exact_matches.append(product)

display_results(
    "Exact Search",
    exact_matches
)


 
prefix = "Apple"

prefix_pattern = (
    "^"
    + re.escape(prefix)
)

prefix_matches = []

for product in products:

    if re.search(
        prefix_pattern,
        product,
        re.IGNORECASE
    ):

        prefix_matches.append(product)

display_results(
    "Prefix Search",
    prefix_matches
)


 
suffix = "Mouse"

suffix_pattern = (
    re.escape(suffix)
    + "$"
)

suffix_matches = []

for product in products:

    if re.search(
        suffix_pattern,
        product,
        re.IGNORECASE
    ):

        suffix_matches.append(product)

display_results(
    "Suffix Search",
    suffix_matches
)


 
partial_keyword = "Laptop"

partial_matches = []

for product in products:

    if re.search(
        re.escape(partial_keyword),
        product,
        re.IGNORECASE
    ):

        partial_matches.append(product)

display_results(
    "Partial Search",
    partial_matches
)


 
keyword = "watch"

case_insensitive_matches = []

for product in products:

    if re.search(
        re.escape(keyword),
        product,
        re.IGNORECASE
    ):

        case_insensitive_matches.append(product)

display_results(
    "Case-Insensitive Search",
    case_insensitive_matches
)