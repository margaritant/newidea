import random

class QuoteGenerator:
    def __init__(self, quotes=None):
        self.quotes = quotes or []

    def load_quotes_from_file(self, file_path):
        with open(file_path, 'r') as file:
            self.quotes.extend(file.readlines())

    def get_random_quote(self):
        if not self.quotes:
            return "No quotes available."
        return random.choice(self.quotes).strip()

    def get_quotes_by_type(self, keyword):
        matching_quotes = [quote for quote in self.quotes if keyword.lower() in quote.lower()]
        if not matching_quotes:
            return f"No quotes containing '{keyword}' available."
        return matching_quotes

if __name__ == "__main__":
    # Example usage
    quote_generator = QuoteGenerator()
    quote_generator.load_quotes_from_file("quotes.txt")

    print("Random Quote:")
    print(quote_generator.get_random_quote())

    keyword = input("Enter a keyword to search for in quotes: ")
    matching_quotes = quote_generator.get_quotes_by_type(keyword)
    print(f"Quotes containing '{keyword}':")
    for quote in matching_quotes:
        print(quote.strip())
