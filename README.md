# 🚗 Car Price Prediction using Machine Learning

## 📖 Overview

This project is a Machine Learning-powered web application that predicts the selling price of a used car based on various vehicle attributes. The application is built using Streamlit and provides a simple and interactive interface for users to estimate car prices instantly.

The model has been trained on historical car data and uses important features such as car brand, manufacturing year, fuel type, transmission type, mileage, engine capacity, and more to generate predictions.

---

## 🎯 Problem Statement

Determining the fair market value of a used car can be challenging due to the large number of factors that influence its price.

This project aims to solve that problem by using Machine Learning techniques to estimate a car's selling price accurately based on its specifications.

---

## ✨ Features

* Interactive Streamlit web interface
* Real-time price prediction
* Easy-to-use input controls
* Supports multiple vehicle specifications
* Machine Learning based estimation
* Clean and responsive design

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Pickle
* Streamlit

### Development Tools

* VS Code
* Git
* GitHub

---

## 📊 Dataset Information

The dataset contains information about used cars including:

| Feature      | Description               |
| ------------ | ------------------------- |
| Name         | Car Brand                 |
| Year         | Manufacturing Year        |
| Km Driven    | Total Distance Driven     |
| Fuel         | Fuel Type                 |
| Seller Type  | Dealer/Individual         |
| Transmission | Manual/Automatic          |
| Owner        | Number of Previous Owners |
| Mileage      | Fuel Efficiency           |
| Engine       | Engine Capacity           |
| Max Power    | Maximum Power Output      |
| Seats        | Number of Seats           |

---

## 🧠 Machine Learning Workflow

### 1. Data Collection

The dataset was collected and loaded using Pandas.

### 2. Data Cleaning

* Removed unnecessary values
* Handled categorical features
* Processed brand names

### 3. Feature Engineering

* Extracted brand names
* Converted categorical values into numerical representations

### 4. Model Training

The Machine Learning model was trained using Scikit-Learn and saved using Pickle.

### 5. Deployment

The trained model was integrated into a Streamlit application for real-time predictions.

---

## 📂 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── model.pkl
├── Cardetails.csv
├── requirements.txt
├── README.md
└── images/
    └── app_screenshot.png
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Car-Price-Prediction.git
```

### Navigate to Project Folder

```bash
cd Car-Price-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 💻 Application Usage

1. Select Car Brand
2. Choose Manufacturing Year
3. Enter Kilometers Driven
4. Select Fuel Type
5. Choose Seller Type
6. Select Transmission Type
7. Select Owner Type
8. Enter Mileage
9. Enter Engine Capacity
10. Enter Max Power
11. Select Number of Seats
12. Click **Predict Price**

The application will display the estimated selling price of the car.

---

## 📈 Future Improvements

* Improve model accuracy
* Add more vehicle features
* Deploy on Streamlit Cloud
* Add visual analytics dashboard
* Compare multiple cars simultaneously
* Integrate real-time market data

---

## 📸 Screenshots

### Home Page

Add your application screenshot here:

```text
images/app_screenshot.png
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork this repository and submit pull requests.

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

### Swajith Kumar

* B.Tech Student
* Python Developer
* Machine Learning Enthusiast
* Data Science Learner

---

## ⭐ Support

If you found this project helpful, please consider giving it a star on GitHub.
