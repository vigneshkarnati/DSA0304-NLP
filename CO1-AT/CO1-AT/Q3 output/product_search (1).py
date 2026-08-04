"""
Section 2: Regular Expressions – Product Search System
======================================================
A Python-based product search system that performs flexible keyword matching
using Regular Expressions for an e-commerce platform.
"""

import re
from collections import Counter
from dataclasses import dataclass


@dataclass
class Product:
    """Data class to represent a product."""

    id: int
    name: str
    category: str
    price: float


@dataclass
class SearchResult:
    """Data class to store search results."""

    query: str
    search_type: str
    matched_products: list[Product]
    match_count: int


class ProductSearchSystem:
    """
    Product search system with flexible keyword matching using Regular Expressions.

    Features:
    - Exact keyword search
    - Prefix-based search
    - Suffix-based search
    - Partial keyword search
    - Case-insensitive search
    - Report generation
    """

    def __init__(self, products: list[Product] = None):
        self.products: list[Product] = products or []
        self.search_history: list[SearchResult] = []

    def add_product(self, product: Product):
        """Add a product to the catalog."""
        self.products.append(product)

    def add_products(self, products: list[Product]):
        """Add multiple products to the catalog."""
        self.products.extend(products)

    def search_exact(self, keyword: str) -> SearchResult:
        """
        Search products using exact keyword match.

        Args:
            keyword: The exact keyword to search for

        Returns:
            SearchResult with matching products
        """
        pattern = re.compile(r"\b" + re.escape(keyword) + r"\b")
        matches = [p for p in self.products if pattern.search(p.name)]

        result = SearchResult(query=keyword, search_type="Exact", matched_products=matches, match_count=len(matches))
        self.search_history.append(result)
        return result

    def search_prefix(self, prefix: str) -> SearchResult:
        """
        Search products using prefix-based matching.

        Args:
            prefix: The prefix to match at the start of product names

        Returns:
            SearchResult with matching products
        """
        pattern = re.compile(r"\b" + re.escape(prefix), re.IGNORECASE)
        matches = [p for p in self.products if pattern.match(p.name)]

        result = SearchResult(query=prefix, search_type="Prefix", matched_products=matches, match_count=len(matches))
        self.search_history.append(result)
        return result

    def search_suffix(self, suffix: str) -> SearchResult:
        """
        Search products using suffix-based matching.

        Args:
            suffix: The suffix to match at the end of product names

        Returns:
            SearchResult with matching products
        """
        pattern = re.compile(re.escape(suffix) + r"\b", re.IGNORECASE)
        matches = [p for p in self.products if pattern.search(p.name)]

        result = SearchResult(query=suffix, search_type="Suffix", matched_products=matches, match_count=len(matches))
        self.search_history.append(result)
        return result

    def search_partial(self, keyword: str) -> SearchResult:
        """
        Search products using partial keyword matching.

        Args:
            keyword: The partial keyword to search for anywhere in product names

        Returns:
            SearchResult with matching products
        """
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matches = [p for p in self.products if pattern.search(p.name)]

        result = SearchResult(query=keyword, search_type="Partial", matched_products=matches, match_count=len(matches))
        self.search_history.append(result)
        return result

    def search_case_insensitive(self, keyword: str) -> SearchResult:
        """
        Search products with case-insensitive matching.

        Args:
            keyword: The keyword to search (case-insensitive)

        Returns:
            SearchResult with matching products
        """
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        matches = [p for p in self.products if pattern.search(p.name)]

        result = SearchResult(
            query=keyword,
            search_type="Case-Insensitive",
            matched_products=matches,
            match_count=len(matches),
        )
        self.search_history.append(result)
        return result

    def display_results(self, result: SearchResult) -> str:
        """Display search results in a formatted manner."""
        separator = "=" * 60

        output = f"""
{separator}
Search Type: {result.search_type}
Query: "{result.query}"
Matches Found: {result.match_count}
{separator}
"""
        if result.matched_products:
            output += f"{'ID':<6}{'Product Name':<35}{'Category':<15}{'Price':>8}\n"
            output += "-" * 60 + "\n"
            for product in result.matched_products:
                output += f"{product.id:<6}{product.name:<35}{product.category:<15}${product.price:>7.2f}\n"
        else:
            output += "\n  No products found matching the search criteria.\n"

        return output

    def generate_report(self) -> str:
        """
        Generate a report showing the total number of matching products
        for each search performed.
        """
        if not self.search_history:
            return "\nNo searches performed yet.\n"

        separator = "=" * 60
        report = f"""
{separator}
        SEARCH HISTORY REPORT
        Total Searches Performed: {len(self.search_history)}
{separator}

{"#":<4}{"Search Type":<18}{"Query":<20}{"Matches":>8}
{"-" * 50}
"""
        total_matches = 0
        for i, result in enumerate(self.search_history, 1):
            report += f'{i:<4}{result.search_type:<18}"{result.query}"{result.match_count:>8}\n'
            total_matches += result.match_count

        report += f"{'-' * 50}\n"
        report += f"{'Total Matches Across All Searches:':<42}{total_matches:>8}\n"

        # Summary by search type
        report += f"\n{separator}\n"
        report += "SUMMARY BY SEARCH TYPE\n"
        report += "-" * 40 + "\n"

        type_counts = Counter(r.search_type for r in self.search_history)
        for search_type, count in type_counts.items():
            type_matches = sum(r.match_count for r in self.search_history if r.search_type == search_type)
            report += f"  {search_type:<20}: {count} searches, {type_matches} total matches\n"

        return report


# Sample product catalog
SAMPLE_PRODUCTS = [
    Product(1, "Laptop Pro 15", "Electronics", 1299.99),
    Product(2, "Laptop Stand", "Accessories", 49.99),
    Product(3, "Wireless Mouse", "Accessories", 29.99),
    Product(4, "Gaming Laptop Ultra", "Electronics", 1899.99),
    Product(5, "USB-C Hub", "Accessories", 39.99),
    Product(6, "Monitor 27 inch", "Electronics", 449.99),
    Product(7, "Keyboard Mechanical", "Accessories", 89.99),
    Product(8, "Laptop Bag", "Accessories", 34.99),
    Product(9, "Wireless Keyboard", "Accessories", 59.99),
    Product(10, "Laptop Charger", "Accessories", 24.99),
    Product(11, "Smart Watch Pro", "Wearables", 399.99),
    Product(12, "Wireless Earbuds", "Audio", 149.99),
    Product(13, "Bluetooth Speaker", "Audio", 79.99),
    Product(14, "Gaming Mouse", "Accessories", 69.99),
    Product(15, "Tablet Stand", "Accessories", 24.99),
]


def main():
    """Main function to demonstrate the Product Search System."""
    search_system = ProductSearchSystem(SAMPLE_PRODUCTS)

    print("\n" + "=" * 70)
    print("     PRODUCT SEARCH SYSTEM")
    print("     Using Regular Expressions")
    print("=" * 70)

    # Display all products
    print("\n📋 PRODUCT CATALOG:")
    print("-" * 70)
    print(f"{'ID':<6}{'Product Name':<35}{'Category':<15}{'Price':>8}")
    print("-" * 70)
    for product in SAMPLE_PRODUCTS:
        print(f"{product.id:<6}{product.name:<35}{product.category:<15}${product.price:>7.2f}")

    # Demo 1: Exact Search
    print("\n\n🔍 DEMO 1: EXACT KEYWORD SEARCH")
    result = search_system.search_exact("Laptop")
    print(search_system.display_results(result))

    # Demo 2: Prefix Search
    print("\n🔍 DEMO 2: PREFIX-BASED SEARCH")
    result = search_system.search_prefix("Wireless")
    print(search_system.display_results(result))

    # Demo 3: Suffix Search
    print("\n🔍 DEMO 3: SUFFIX-BASED SEARCH")
    result = search_system.search_suffix("Pro")
    print(search_system.display_results(result))

    # Demo 4: Partial Search
    print("\n🔍 DEMO 4: PARTIAL KEYWORD SEARCH")
    result = search_system.search_partial("lap")
    print(search_system.display_results(result))

    # Demo 5: Case-Insensitive Search
    print("\n🔍 DEMO 5: CASE-INSENSITIVE SEARCH")
    result = search_system.search_case_insensitive("GAMING")
    print(search_system.display_results(result))

    # Demo 6: Additional searches for comprehensive report
    print("\n🔍 DEMO 6: ADDITIONAL SEARCHES")
    result = search_system.search_partial("mouse")
    print(search_system.display_results(result))

    result = search_system.search_prefix("USB")
    print(search_system.display_results(result))

    # Generate and display the report
    print("\n\n" + "=" * 70)
    print("📊 SEARCH HISTORY REPORT")
    print("=" * 70)
    print(search_system.generate_report())

    return search_system


if __name__ == "__main__":
    main()
