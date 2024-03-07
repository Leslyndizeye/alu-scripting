import urllib.request
import json

def number_of_subscribers(subreddit):
    # Set a custom User-Agent header to avoid any API request issues
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    
    # Construct the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Create a request object with the provided URL and headers
    req = urllib.request.Request(url, headers=headers)
    
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(req) as response:
            # Check if the response is successful (status code 200)
            if response.getcode() == 200:
                # Parse JSON data from the response
                data = json.loads(response.read().decode('utf-8'))
                
                # Extract the number of subscribers from the parsed data
                subscribers = data['data']['subscribers']
                
                return subscribers
            else:
                # If the subreddit is invalid or there's an issue with the request, return 0
                return 0
    except urllib.error.HTTPError as e:
        # If there's an HTTPError (e.g., 404 Not Found), return 0
        return 0

# Example usage:
print(number_of_subscribers("Minecraft"))
