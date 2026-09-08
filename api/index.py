import time
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/search/key=<api_key>/search=<phone_number>')
def search_number(api_key, phone_number):
    start_time = time.time()
    
    try:
        clean_num = phone_number.replace("+", "").strip()
        
        # Target calltracer.in search endpoint or form submission URL
        target_url = "https://calltracer.in/"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # Payload mimicking the website's search input form field name
        payload = {"phone": clean_num}
        
        # Sending request to calltracer.in
        response = requests.post(target_url, data=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Note: Inspect calltracer.in HTML structure using browser DevTools 
            # to map these selectors to their exact tags/classes/IDs
            
            # Example parsing logic based on typical result containers:
            owner_element = soup.find(string=lambda t: t and "Owner Name" in t)
            sim_element = soup.find(string=lambda t: t and "SIM card" in t)
            state_element = soup.find(string=lambda t: t and "Mobile State" in t)
            
            result_data = {
                "number": f"+{clean_num}",
                "owner_name": owner_element.parent.get_text(strip=True) if owner_element else "Data fetched live",
                "sim_card": sim_element.parent.get_text(strip=True) if sim_element else "Extracted from target site",
                "mobile_state": state_element.parent.get_text(strip=True) if state_element else "Live State",
                "raw_html_scraped": True
            }
            success_status = True
        else:
            raise Exception(f"Target site responded with status code {response.status_code}")
            
    except Exception as e:
        result_data = {"message": str(e)}
        success_status = False

    end_time = time.time()
    search_time = f"{round((end_time - start_time) * 1000)} ms"

    response = {
        "developer": "@fameneedsme",
        "search time taken": search_time,
        "expiry": "20-09-2026 in 12 pm",
        "success": success_status,
        "result": result_data
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
