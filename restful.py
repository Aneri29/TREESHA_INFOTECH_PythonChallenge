#!/usr/bin/env python3

import argparse
import json
import csv
import requests

class RestClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args()

    def create_parser(self):
        parser = argparse.ArgumentParser(description="Simple command-line REST client for JSONPlaceholder.")
        parser.add_argument("method", choices=["get", "post"], help="HTTP method (get or post)")
        parser.add_argument("endpoint", help="API endpoint (e.g., /posts/1)")
        parser.add_argument("-o", "--output", help="Output file for response (JSON or CSV)")
        return parser

    def execute_request(self):
        url = f"{self.BASE_URL}{self.args.endpoint}"
        headers = {"Content-Type": "application/json"}

        try:
            if self.args.method == "get":
                response = requests.get(url)
            elif self.args.method == "post":
                response = requests.post(url, json={}, headers=headers)  

            response.raise_for_status()

            if self.args.output:
                self.save_response(response)
            else:
                self.display_response(response)

        except requests.RequestException as e:
            print(f"Error: {e}")
            exit(1)

    def save_response(self, response):
        if self.args.output.endswith(".json"):
            with open(self.args.output, "w") as json_file:
                json.dump(response.json(), json_file, indent=2)
            print(f"Response saved to {self.args.output}")
        elif self.args.output.endswith(".csv"):
            self.save_csv(response)
        else:
            print("Unsupported output format. Please use .json or .csv.")

    def save_csv(self, response):
        data = response.json()
        if isinstance(data, list) and data:
            keys = data[0].keys()
            with open(self.args.output, "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            print(f"Response saved to {self.args.output}")
        else:
            print("Invalid data format for CSV.")

    def display_response(self, response):
        print(f"HTTP Status Code: {response.status_code}")
        print("Response:")
        print(response.json())

if __name__ == "__main__":
    client = RestClient()
    client.execute_request()
