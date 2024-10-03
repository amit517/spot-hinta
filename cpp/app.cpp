#include "crow.h"
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>
#include <iostream>

using json = nlohmann::json;

// Function to fetch price data from the API
json fetch_price(int hour) {
    std::string url = "https://api.spot-hinta.fi/JustNow?lookForwardHours=" + std::to_string(hour);
    auto response = cpr::Get(cpr::Url{url});

    if (response.status_code == 200) {
        json data = json::parse(response.text);
        return data;
    } else {
        return nullptr;
    }
}

int main() {
    crow::SimpleApp app;

    // Endpoint to get the current and next hour prices
    CROW_ROUTE(app, "/get_prices")([]() {
        json current_price = fetch_price(0); // Fetch current hour price
        json next_hour_price = fetch_price(1); // Fetch next hour price

        json response;
        if (!current_price.is_null() && !next_hour_price.is_null()) {
            response["current"] = {
                {"price", current_price["PriceWithTax"]},
                {"time", current_price["DateTime"]}
            };
            response["next"] = {
                {"price", next_hour_price["PriceWithTax"]},
                {"time", next_hour_price["DateTime"]}
            };
        } else {
            return crow::response(500, "Error fetching data");
        }

        return crow::response(response.dump());
    });

    // Start the server on port 18080
    app.port(18080).multithreaded().run();
}
