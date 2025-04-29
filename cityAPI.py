from flask import Flask, request, jsonify
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Kết nối SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-BLD518M\\SQLEXPRESS;DATABASE=WeatherCity;UID=sa;PWD=utc123;Trusted_Connection=yes'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# API: Lấy danh sách thành phố yêu thích
@app.route("/api/favorites", methods=["GET"])
def get_favorites():
    cursor.execute("SELECT * FROM tblFavoriteCity")
    rows = cursor.fetchall()
    cities = [{"id": row.Id, "city": row.CityName} for row in rows]
    return jsonify(cities)

# API: Thêm thành phố mới
@app.route("/api/favorites", methods=["POST"])
def add_favorite():
    data = request.get_json()
    city = data.get("city")

    if not city:
        return jsonify({"error": "Thiếu tên thành phố"}), 400

    cursor.execute("INSERT INTO tblFavoriteCity (CityName) VALUES (?)", (city,))
    conn.commit()
    return jsonify({"message": f"Đã thêm thành phố: {city}"}), 201

# API: Xóa thành phố yêu thích
@app.route("/api/favorites", methods=["DELETE"])
def delete_favorite():
    data = request.get_json()
    city_id = data.get("id")

    if not city_id:
        return jsonify({"error": "Thiếu ID thành phố"}), 400

    cursor.execute("DELETE FROM tblFavoriteCity WHERE Id = ?", (city_id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "Không tìm thấy thành phố để xóa"}), 404

    return jsonify({"message": f"Đã xóa thành phố với ID: {city_id}"}), 200
if __name__ == "__main__":
    app.run(debug=True)
