from flask import Flask, request, jsonify
import ipaddress

app = Flask(__name__)

@app.route("/check_ip", methods=["GET"])
def check_ip():
    ip = request.args.get("ip")
    try:
        ip_obj = ipaddress.ip_address(ip)
        return jsonify({
            "ip": ip,
            "valid": True,
            "version": ip_obj.version
        })
    except ValueError:
        return jsonify({
            "ip": ip,
            "valid": False
        })

if __name__ == "__main__":
    app.run(debug=True)
