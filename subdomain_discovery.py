import requests

def subdomain_discovery(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if the HTTP request fails
        subdomains = set()  # Use a set to store unique subdomains
        
        certificates = response.json()
        for certificate in certificates:
            subdomain = certificate.get('name_value', '')
            if subdomain:
                # Get only the part of the subdomain that matches the main domain
                subdomain = subdomain.strip().lower()
                if subdomain.endswith(domain):
                    subdomains.add(subdomain)
        
        if subdomains:
            print(f"Found Subdomains for {domain}:")
            for subdomain in sorted(subdomains):
                print(subdomain)
        else:
            print(f"No subdomains found for: {domain}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain for subdomain discovery: ")
    subdomain_discovery(domain)
