import requests

# Read URLs from a text file
with open('urls.txt', 'r') as url_file:
    urls = url_file.read().splitlines()

# Open two separate files for valid and invalid URLs
with open('valid_urls.txt', 'w') as valid_file, open('invalid_urls.txt', 'w') as invalid_file:
    # Loop through each URL
    for url in urls:
        try:
            # Make a request to the URL
            response = requests.get(url, timeout=10)
            
            # If the response status code is 200-299 (success codes)
            if 200 <= response.status_code < 300:
                valid_file.write(f'{url} - {response.status_code}\n')
                print(f'{url} - {response.status_code} (Valid)')  # Optional: Print the result
            else:
                # If the response code indicates some kind of error
                invalid_file.write(f'{url} - {response.status_code}\n\n')  # Add a blank line after each entry to make it easier to read
                print(f'{url} - {response.status_code} (Invalid)')
        
        except requests.exceptions.RequestException as e:
            # Write URLs that caused an exception (e.g., 404 or connection errors)
            invalid_file.write(f'{url} - Error: {e}\n\n')  # Add a blank line after each entry
            print(f'{url} - Error: {e}')  # Optional: Print the error

# I realise this is basic, it's quick and dirty and I needed it to 'just work'.
