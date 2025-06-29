# import requests
# import json


# class Search:

#     def get_search_results(self):
#         search_term = "the lord of the rings"

#         search_term_formatted = search_term.replace(" ", "+")
#         fields = ["title", "author_name"]
#         # formats the list into a comma separated string
#         # output: "title,author_name"
#         fields_formatted = ",".join(fields)
#         limit = 1

#         URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

#         response = requests.get(URL)
#         return response.content

#     def get_search_results_json(self):
#         search_term = "the lord of the rings"

#         search_term_formatted = search_term.replace(" ", "+")
#         fields = ["title", "author_name"]
#         fields_formatted = ",".join(fields)
#         limit = 1

#         URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
#         print(URL)
#         response = requests.get(URL)
#         return response.json()

#     def get_user_search_results(self, search_term):
#         search_term_formatted = search_term.replace(" ", "+")
#         fields = ["title", "author_name"]
#         fields_formatted = ",".join(fields)
#         limit = 1

#         URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

#         response = requests.get(URL).json()
#         response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
#         return response_formatted


# # results = Search().get_search_results()
# # print(results)

# # results_json = Search().get_search_results_json()
# # print(json.dumps(results_json, indent=1))

# search_term = input("Enter a book title: ")
# result = Search().get_user_search_results(search_term)
# print("Search Result:\n")
# print(result)

import requests
import json


class Search:
    def get_search_results(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        print(URL)  # Helpful for debugging or confirmation
        response = requests.get(URL)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL).json()

        # Safely extract title and author, handle if no results
        if response["docs"]:
            title = response["docs"][0].get("title", "No title found")
            authors = response["docs"][0].get("author_name", ["No author found"])
            author = authors[0] if authors else "No author found"
            response_formatted = f"Title: {title}\nAuthor: {author}"
        else:
            response_formatted = "No results found for your search."
        return response_formatted


if __name__ == "__main__":
    # Example usages:
    # results = Search().get_search_results()
    # print(results)

    # results_json = Search().get_search_results_json()
    # print(json.dumps(results_json, indent=1))

    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("\nSearch Result:\n")
    print(result)
