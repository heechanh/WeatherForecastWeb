using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using WeatherApp.Models;

namespace WeatherApp.Controllers
{
    public class WeatherController : Controller
    {
        private readonly IHttpClientFactory _httpClientFactory;

        private readonly IConfiguration _configuration;
        public WeatherController(IHttpClientFactory httpClientFactory, IConfiguration configuration)
        {
            _httpClientFactory = httpClientFactory;
            _configuration = configuration;
        }

        public async Task<IActionResult> Index(string city = "LonDon")
        {
            //string apiKey = "67e03cccead54c02b9242900250304";
            string apiKey = _configuration["WeatherApi:Key"];
            string apiUrl = $"http://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}";

            var httpClient = _httpClientFactory.CreateClient();
            var response = await httpClient.GetAsync(apiUrl);




            if (response.IsSuccessStatusCode)
            {
                var jsonResponse = await response.Content.ReadAsStringAsync();
                // Ánh xạ dữ liệu JSON sang model
                var options = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
                var weatherData = JsonSerializer.Deserialize<WeatherData>(jsonResponse, options);

                if (weatherData == null || weatherData.Location == null)
                {
                    ViewBag.Error = "Dữ liệu thời tiết không khả dụng.";
                    return View(null);
                }

                return View(weatherData);
            }
            else
            {
                ViewBag.Error = "Không thể lấy thông tin thời tiết. Vui lòng thử lại!";
                return View();
            }
        }
    }
}