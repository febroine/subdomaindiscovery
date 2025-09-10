# SubdomainDiscovery 🔍

A simple Python tool to discover subdomains of a given domain using [crt.sh](https://crt.sh/).  
It queries the Certificate Transparency logs to extract known subdomains via public certificates.

## 🌐 Example Usage

```bash
$ python subdomain_discovery.py
Enter the domain for subdomain discovery: example.com
Found Subdomains for example.com:
example.com
www.example.com
mail.example.com
...
```

## 🚀 Features

Uses crt.sh API to retrieve subdomains from certificate transparency logs
Lightweight and minimal (only requires the requests library)
Easy to use – just run and input a domain name

## 📦 Requirements

-Python 3.x

-requests library

Install dependencies with:
```bash
pip install requests
```

## 🛠️ How It Works

The script sends a query to:
```bash
https://crt.sh/?q=%25.example.com&output=json
```

It parses the JSON response and extracts name_value fields that represent subdomains, removing duplicates and filtering by the base domain.

## 🔐 Legal Notice

This tool is for educational and authorized security testing purposes only.

Do not use against systems you do not own or have permission to test.

## 📄 License

This project is licensed under the MIT License.
