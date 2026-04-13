# delivery-time-prediction
Uncover insights into factors influencing delivery efficiency, identify areas for optimization, and explore the impact of various variables on the overall customer experience.

## Setup

### Prerequisites
- Python 3.8 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd delivery-time-prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

### Development
- Run tests: `pytest`
- Format code: `black .`
- Lint code: `ruff check .`

### Developer quick start
To install the project and development tools in one step:
```bash
pip install -e '.[dev]'
```
Then run:
```bash
python -m black --target-version py310 .
python -m ruff check .
pytest
```

## Database

The project uses the **amazon_delivery.csv** dataset located in the `database/` folder. This dataset contains delivery order information with the following columns:

| Colonne | Description |
|---------|-------------|
| **Order_ID** | Unique identifier for each order. |
| **Agent_Age** | Age of the delivery agent. |
| **Agent_Rating** | Rating/performance score of the delivery agent. |
| **Store_Latitude** | Latitude coordinate of the store. |
| **Store_Longitude** | Longitude coordinate of the store. |
| **Drop_Latitude** | Latitude coordinate of the delivery location. |
| **Drop_Longitude** | Longitude coordinate of the delivery location. |
| **Order_Date** | Date when the order was placed. |
| **Order_Time** | Time when the order was placed. |
| **Pickup_Time** | Time when the order was picked up. |
| **Weather** | Weather conditions during delivery (Sunny, Stormy, Sandstorms, etc.). |
| **Traffic** | Traffic conditions (High, Medium, Low, Jam). |
| **Vehicle** | Type of delivery vehicle (motorcycle, scooter, etc.). |
| **Area** | Type of area (Urban, Metropolitan). |
| **Delivery_Time** | Time taken for delivery (in minutes). |
| **Category** | Product category (Clothing, Electronics, Sports, Cosmetics, etc.). |
