## Overview
This project is designed to fetch, normalize, deduplicate, and save data from multiple vendors into a MongoDB database. It implements an API that handles data fetching from different vendors, normalization of data to a unified model, deduplication, and saving the data to MongoDB. The solution is built with modularity in mind to ensure ease of testing, debugging, and future enhancements.

## Features
- **Data Fetching**: Fetches data from different vendors using asynchronous API calls.
- **Data Normalization**: Normalizes raw data into a unified format using vendor-specific models.
- **Data Deduplication**: Deduplicates the normalized data using custom strategies.
- **MongoDB Integration**: Saves deduplicated data to MongoDB in a scalable manner.
- **API Rate Throttling**: Ensures that API calls are throttled appropriately to prevent overload.

## Project Structure
- **app/models**: Defines Pydantic models for the vendors.
- **app/services**: Contains logic for data processing, including fetching, normalizing, deduplicating, and saving.
- **app/core**: Contains core functionalities like MongoDB integration and settings.

## Setup

1. Clone the repository:
    \`\`\`bash
    git clone <https://github.com/VicThorVic/Armis.git>
    cd <Armis>
    \`\`\`

2. Install dependencies using Poetry:
    \`\`\`bash
    poetry install
    \`\`\`

3. Set up your MongoDB database and ensure it’s running.

4. **With Docker (Optional)**:
    - To bring up the containers:
      \`\`\`bash
      docker-compose up --build
      \`\`\`
    - To bring down the containers:
      \`\`\`bash
      docker-compose down
      \`\`\`

5. Run the application (without Docker):
    \`\`\`bash
    poetry run uvicorn app.main:app --reload
    \`\`\`

    The application will be available at \`http://127.0.0.1:8000\`.

## Endpoints
- **GET /fetch-data**: Fetches data for a specific vendor (VendorA or VendorB) and processes it.
    - **vendor_name**: The name of the vendor (\`VendorA\` or \`VendorB\`).
    - **limit**: The number of records to fetch per page (default: 100).
    - **batch_size**: The size of each batch for processing (default: 50).
