package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

// Struct to parse API response
type PriceData struct {
    PriceWithTax float64 `json:"PriceWithTax"`
    DateTime     string  `json:"DateTime"`
}

// Function to fetch price data from the API
func fetchPrice(hour int) (PriceData, error) {
    var data PriceData
    url := fmt.Sprintf("https://api.spot-hinta.fi/JustNow?lookForwardHours=%d", hour)
    
    // Making the HTTP request
    resp, err := http.Get(url)
    if err != nil {
        return data, err
    }
    defer resp.Body.Close()
    
    // Decoding the JSON response
    err = json.NewDecoder(resp.Body).Decode(&data)
    return data, err
}

// Handler to get current and next-hour price
func getPrices(w http.ResponseWriter, r *http.Request) {
    currentPrice, err := fetchPrice(0)
    if err != nil {
        http.Error(w, "Error fetching current price", http.StatusInternalServerError)
        return
    }

    nextHourPrice, err := fetchPrice(1)
    if err != nil {
        http.Error(w, "Error fetching next hour price", http.StatusInternalServerError)
        return
    }

    // Prepare the response as JSON
    response := map[string]interface{}{
        "current": currentPrice,
        "next":    nextHourPrice,
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(response)
}

func main() {
    // Set up routes
    http.HandleFunc("/get_prices", getPrices)

    // Start the server
    fmt.Println("Starting server at port 8080...")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
