import time
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/search/key=<api_key>/search=<phone_number>')
def search_number(api_key, phone_number):
    start_time = time.time()
    
    # API Key validation (മാറ്റണമെങ്കിൽ മാറ്റാം)
    if api_key != "demo":
        end_time = time.time()
        search_time = f"{round((end_time - start_time) * 1000)} ms"
        return jsonify({
            "developer": "@fameneedsme",
            "search time taken": search_time,
            "expiry": "20-09-2026 in 12 pm",
            "success": False,
            "error": "Invalid API Key"
        }), 403

    try:
        # calltracer.in സൈറ്റിലേക്ക് റിക്വസ്റ്റ് അയക്കുന്നു
        # (സൈറ്റിന്റെ സെർച്ച് URL ഘടനയ്ക്ക് അനുസരിച്ച് ഇത് മാറ്റേണ്ടി വരാം)
        target_url = f"https://calltracer.in/"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        
        # ഒരു POST അല്ലെങ്കിൽ GET റിക്വസ്റ്റ് വഴി നമ്പര്‍ പാസ്സ് ചെയ്യാം
        payload = {"phone": phone_number}
        response = requests.post(target_url, data=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # ഇവിടം മുതല്‍ calltracer.in വെബ്‌സൈറ്റിലെ HTML ടാഗുകൾ അനുസരിച്ച് ഡാറ്റ എക്സ്ട്രാക്റ്റ് ചെയ്യാം
            # ഉദാഹരണത്തിന്:
            # owner_name = soup.find('div', class_='owner-class-name').text.strip()
            
            result_data = {
                "phone": phone_number,
                "status": "Connected to calltracer.in successfully",
                "note": "Parse HTML elements here using BeautifulSoup based on calltracer.in DOM structure"
            }
            success_status = True
        else:
            raise Exception(f"Failed to connect. Status code: {response.status_code}")
            
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
