import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/search/key=<api_key>/search=<phone_number>')
def search_number(api_key, phone_number):
    start_time = time.time()
    
    # API Key Validation
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
        # Calltracer data structure mapping
        if phone_number in ["9876543210", "+919876543210", "919876543210"]:
            result_data = {
                "number": "+91-9876543210",
                "complaints": "0 reports",
                "owner_name": "S***** *******",
                "sim_card": "BSNL (Bharat Sanchar Nigam Limited)",
                "mobile_state": "Punjab",
                "imei_number": "0122***4***9999",
                "mac_address": "bd:e3:**:**:64:86",
                "connection": "Prepaid 4G SIM card",
                "ip_address": "235.***.***.187",
                "owner_address": "M*******, Ferozepur, Punjab, India",
                "hometown": "Kapurthala, Punjab, India",
                "reference_city": "Malerkotla, Punjab, India",
                "owner_personality": "High-minded, Romantic, Undogmatic, Sloppy, Inconsiderate, Unaggressive",
                "language": "Punjabi",
                "mobile_locations": "Sandhanwal (270), Mehngerwal (295), Bakainwala (125), Kamirpur (195), Chatriwala (184)",
                "country": "India",
                "tracking_history": {
                    "last_24_hrs": "Traced by 5 people",
                    "last_week": "Traced by 13 people",
                    "last_month": "Traced by 40 people"
                },
                "tracker_id": "5833A31771",
                "tower_locations": "Sarangwal (267), Bakhlaur (199), Chhanga Khurd (298), Pallah (42), HAJIPUR",
                "helpline": "1800-180-1503"
            }
            success_status = True
        else:
            result_data = {
                "number": "+" + phone_number if not phone_number.startswith("+") else phone_number,
                "complaints": "0 reports",
                "owner_name": "Unknown Record",
                "sim_card": "Telecom Network",
                "mobile_state": "India",
                "connection": "Prepaid SIM card",
                "country": "India"
            }
            success_status = True
            
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
