# 🌦️ Weather Forecast Web App

Dự án Web dự báo thời tiết hiện đại sử dụng **WeatherAPI**. Giao diện thân thiện, dễ sử dụng, hỗ trợ dự báo thời tiết theo **tên thành phố** hoặc **vị trí hiện tại**, cung cấp thông tin **giờ, 7 ngày**, **cảnh báo thời tiết**, và **bản đồ mưa, gió, nhiệt độ**.

---

## 🚀 Tính năng chính

- 🔍 **Tìm kiếm thời tiết** theo tên thành phố
- 📍 **Định vị thời tiết theo vị trí hiện tại** (sử dụng HTML5 Geolocation)
- ⏳ **Dự báo hàng giờ** chi tiết
- 📅 **Dự báo 7 ngày** chính xác
- 🚨 **Hiển thị cảnh báo thời tiết** nguy hiểm (nếu có)
- 🌬️ **Bản đồ gió**, 🌧️ **mưa**, 🌡️ **nhiệt độ** tương tác trực tiếp (sử dụng WeatherAPI hoặc Mapbox Layer)
- 🌗 Giao diện **responsive**, hỗ trợ cả máy tính và điện thoại
- 🔊 (Tùy chọn) Âm thanh thời tiết tương ứng
-Hình nền thay đổi theo thời tiết
---

## 🧰 Công nghệ sử dụng

- 🌐 **Frontend**: HTML, CSS, JavaScript (dùng thêm Bootstrap,jQuery)
- 🔙 **Backend** (nếu có): ASP.NET 6
- 📡 **Weather API**: [https://www.weatherapi.com](https://www.weatherapi.com/)
- 🗺️ **Bản đồ**: Mapbox / LeafletJS (nếu có hiển thị bản đồ)
- 📍 **Vị trí người dùng**: HTML5 Geolocation API

---

## 📸 Demo (Ảnh/GIF minh hoạ)
demo.docs
## Một số file chạy bên ngoài 
cityAPI.py là file để lấy thành phố yêu thích 
SQLQuery1.sql tạo csdl
chạy file cityAPI.py thì mới có thể thêm thành phố yêu thích 

## 🔧 Cách chạy dự án

### 1. Clone dự án
```bash
git clone https://github.com/heechanh/WeatherForecastWeb.git
cd WeatherForecastWeb
