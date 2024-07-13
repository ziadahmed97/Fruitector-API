# Intelligent Fruit Quality Grading System (Backend)
The Intelligent Fruit Quality Grading System backend is responsible for processing fruit images, classifying them using the YOLOv8 model, and sending the results back to the Flutter mobile application. Here are the key features:

# Features:
Fruit Classification: The backend hosts a pre-trained YOLOv8 model capable of identifying and classifying fruits, including apples, bananas, and oranges.
Multi-Fruit Detection: It can handle images containing multiple fruits, providing accurate classifications for each fruit present.
Integration with Flutter: The backend communicates seamlessly with the Flutter app, allowing users to capture fruit images, send requests, and receive quality grading results.
# Technologies Used:
Flask: The lightweight Python web framework powers the backend, handling HTTP requests and orchestrating the classification process.
YOLOv8: The deep learning model, trained on fruit images, enables real-time fruit detection and classification.
# Setting Up the Environment:
- 1.Create a Virtual Environment:
    - Open a terminal or command prompt.
    - Navigate to your project directory.
    - Run the following commands:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- 2.Install Required Libraries:
    - While the virtual environment is active, install the necessary Python libraries using pip. For example:
```
pip install flask
```

- 3.Run the Backend:
    - Start the Flask server that hosts your YOLOv8 model.
    - Ensure the Flutter app communicates with the correct API endpoints.
