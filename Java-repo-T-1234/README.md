# Java E-commerce Application

This repository contains a Java-based e-commerce application with a Spring Boot backend and a frontend (not specified in the current structure).

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Running the Application](#running-the-application)
5. [API Documentation](#api-documentation)
6. [Testing](#testing)
7. [Docker](#docker)
8. [Contributing](#contributing)
9. [License](#license)

## Project Structure

The project follows a standard Maven structure with additional directories for Docker and database scripts:

```
/app/Java-repo-T-1234
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/victorgarciarubio/ecommerce/
│   │   │       ├── config/
│   │   │       ├── dao/
│   │   │       └── entity/
│   │   └── resources/
│   └── test/
│       └── java/
├── bin/
│   ├── build-docker.sh
│   └── db-scripts/
├── tests/
│   ├── integration/
│   └── unit/
├── Dockerfile.web
├── docker-compose.yml
├── pom.xml
├── README.md
└── ...
```

## Prerequisites

- Java JDK 11 or later
- Maven 3.6 or later
- Docker (for containerization)
- MySQL (for local development)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Java-repo-T-1234.git
   cd Java-repo-T-1234
   ```

2. Set up the database:
   - Create a MySQL database named `full-stack-ecommerce`
   - Run the SQL scripts in the `bin/db-scripts/` directory in the following order:
     1. `01-create-user.sql`
     2. `02-create-products.sql`
     3. `03-refresh-database-with-100-products.sql`
     4. `04-countries-and-states.sql`

3. Configure application properties:
   - Open `src/main/resources/application.properties`
   - Update the database connection details if necessary

## Running the Application

1. Build the project:
   ```
   ./mvnw clean package
   ```

2. Run the application:
   ```
   ./mvnw spring-boot:run
   ```

The application should now be running on `http://localhost:8080`.

## API Documentation

API documentation is available via Swagger UI. Once the application is running, you can access it at:

```
http://localhost:8080/swagger-ui.html
```

## Testing

To run the tests:

```
./mvnw test
```

This will run both unit and integration tests.

## Docker

To build and run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t ecommerce-app -f Dockerfile.web .
   ```

2. Run the container:
   ```
   docker-compose up
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.