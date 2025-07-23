#!/usr/bin/env python3
import requests
import re
import sys

def check_image_url(url):
    """Check if an image URL is accessible"""
    try:
        response = requests.head(url, timeout=10, allow_redirects=True)
        return response.status_code == 200
    except Exception as e:
        return False

def extract_urls_from_html(file_path):
    """Extract Unsplash URLs from the HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all Unsplash URLs
    urls = re.findall(r'https://images\.unsplash\.com/[^"]+', content)
    return urls

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_images.py <html_file>")
        sys.exit(1)
    
    html_file = sys.argv[1]
    
    print("Extracting image URLs from HTML file...")
    urls = extract_urls_from_html(html_file)
    
    print(f"Found {len(urls)} Unsplash URLs. Checking accessibility...")
    print("-" * 80)
    
    working_urls = []
    broken_urls = []
    
    for i, url in enumerate(urls, 1):
        print(f"Checking {i}/{len(urls)}: {url[:60]}...")
        if check_image_url(url):
            working_urls.append(url)
            print("✅ Working")
        else:
            broken_urls.append(url)
            print("❌ Broken (404 or error)")
        print()
    
    print("-" * 80)
    print(f"SUMMARY:")
    print(f"Total URLs checked: {len(urls)}")
    print(f"Working URLs: {len(working_urls)}")
    print(f"Broken URLs: {len(broken_urls)}")
    
    if broken_urls:
        print(f"\nBROKEN URLs:")
        for url in broken_urls:
            print(f"  - {url}")
    else:
        print("\n🎉 All URLs are working!")

if __name__ == "__main__":
    main()
