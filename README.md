# Hotel Booking Analytics API

This project provides an API for querying hotel booking data and accessing precomputed analytics such as revenue trends, cancellations, and room distribution. It uses Flask for the API and scikit-learn for search functionality.

## Project Structure

- **app.py**: Flask API implementation.
- **cleaned_hotel_bookings.csv**: Cleaned dataset of hotel bookings.
- **revenue_trends.csv**: Precomputed revenue trends.
- **cancellations.csv**: Precomputed cancellations data.
- **room_distribution.csv**: Precomputed room distribution data.
- **requirements.txt**: Python dependencies.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hotel-booking-analytics.git
   cd hotel-booking-analytics
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask API:
   ```bash
   python app.py
   ```

4. Access the API at `http://127.0.0.1:5000`:
   - `GET /search?query={query}`: Search bookings.
   - `GET /analytics/revenue_trends`: Get revenue trends.
   - `GET /analytics/cancellations`: Get booking cancellations.
   - `GET /analytics/room_distribution`: Get room distribution data.

## Usage

To search bookings, send a GET request to `/search` with a query parameter. Example:

```bash
curl "http://127.0.0.1:5000/search?query=resort hotel portugal"
```

## License

This project is licensed under the MIT License.
