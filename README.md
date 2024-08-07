
<h1>Project Overview</h1>
    <p>This project predicts house prices in Bangalore using data processing, model training, and a web interface. It utilizes Flask for the backend, Streamlit for an interactive UI, and HTML, CSS, and JavaScript for the frontend.</p>

<h2>Project Structure</h2>
<ul>
    <li><strong>server.py:</strong> Main Flask server file.</li>
    <li><strong>util.py:</strong> Functions for data processing and model predictions.</li>
    <li><strong>app.html:</strong> HTML structure of the web page.</li>
    <li><strong>app.css:</strong> CSS styling for the web page.</li>
    <li><strong>app.js:</strong> JavaScript for handling user interactions and API requests.</li>
</ul>

<h2>server.py</h2>
<p>Handles HTTP requests using Flask.</p>
<ul>
    <li><strong>Imports:</strong> Flask, request, jsonify, CORS, Streamlit.</li>
    <li><strong>Routes:</strong> 
        <ul>
            <li><code>/hello:</code> Checks server status.</li>
            <li><code>/get_location_name:</code> Returns location names.</li>
            <li><code>/predict_home_price:</code> Returns estimated house price based on input parameters.</li>
        </ul>
    </li>
</ul>

<h2>util.py</h2>
<p>Helper functions for data processing and predictions.</p>
<ul>
    <li><strong>Functions:</strong> 
        <ul>
            <li><code>get_locations_name():</code> Loads location names.</li>
            <li><code>predict_price(location, sqft, bath, bhk):</code> Predicts house price.</li>
            <li><code>load_save():</code> Loads data and model into global variables.</li>
        </ul>
    </li>
</ul>

<h2>app.html</h2>
<p>Provides the web page structure with forms for user input and sections to display results.</p>

<h2>app.css</h2>
<p>CSS styling for a clean, user-friendly web page.</p>

<h2>app.js</h2>
<p>Handles user interactions and makes API requests.</p>
<ul>
    <li><code>getBathValue()</code> and <code>getBHKValue()</code>: Retrieve selected values.</li>
    <li><code>onClickedEstimatePrice()</code>: Sends POST request and displays result.</li>
    <li><code>onPageLoad()</code>: Fetches and populates location dropdown.</li>
</ul>

<h2>Data Processing and Model</h2>
<p>Involves data cleaning, feature selection, model training, and saving the model for predictions.</p>

<h2>Usage</h2>
<ol>
    <li>Run <code>server.py</code> to start the Flask server.</li>
    <li>Open <code>app.html</code> in a browser.</li>
    <li>Enter details and click "Estimate Price".</li>
    <li>View the estimated price on the page.</li>
</ol>

<p>This project combines data science and web development for predicting house prices with a user-friendly interface.</p>
<h1>Explanation of Project.ipynb</h1>
<ol>
    <li>
        <h2>Importing Libraries</h2>
        <p><strong>Libraries Imported:</strong> <code>numpy</code>, <code>pandas</code>, and <code>matplotlib.pyplot</code> are imported for numerical operations, data manipulation, and visualization respectively.</p>
    </li>
    <li>
        <h2>Loading Data</h2>
        <p><strong>Loading Data:</strong> The dataset <code>bengaluru_house_prices.csv</code> is loaded into a DataFrame named <code>data</code>.</p>
    </li>
    <li>
        <h2>Data Cleaning</h2>
        <p><strong>Removing Unnecessary Columns:</strong> The columns <code>area_type</code>, <code>availability</code>, <code>society</code>, and <code>balcony</code> are dropped from the dataset.</p>
        <p><strong>Handling Missing Values:</strong> The missing values in the <code>location</code> and <code>size</code> columns are dropped. The missing values in the <code>bath</code> column are filled with the median value of that column.</p>
    </li>
    <li>
        <h2>Feature Engineering</h2>
        <p><strong>Creating BHK Column:</strong> The <code>size</code> column, which contains strings like "2 BHK" or "3 Bedroom", is converted into a numerical <code>bhk</code> column by extracting the first integer.</p>
        <p><strong>Handling <code>total_sqft</code> Anomalies:</strong> The <code>total_sqft</code> column contains a mix of numeric values and ranges (e.g., "1000-1200"). A helper function converts these ranges into their average values.</p>
        <p><strong>Location Data:</strong> The locations with fewer than 10 data points are categorized under a new label "other".</p>
    </li>
    <li>
        <h2>Removing Outliers</h2>
        <p><strong>Price per Square Foot:</strong> A new column <code>price_per_sqft</code> is created to identify and remove outliers where the total square feet divided by the number of bedrooms (<code>bhk</code>) is less than 300.</p>
    </li>
    <li>
        <h2>Model Training</h2>
        <p><strong>Preparing Data for Modeling:</strong> The categorical <code>location</code> column is one-hot encoded. The features <code>total_sqft</code>, <code>bath</code>, <code>bhk</code>, and the one-hot encoded location columns are used to train the model.</p>
        <p><strong>Training the Model:</strong> A linear regression model is trained on the data using <code>scikit-learn</code>.</p>
    </li>
    <li>
        <h2>Saving the Model</h2>
        <p><strong>Saving the Model and Columns:</strong> The trained model and the column information are saved using <code>pickle</code> and <code>json</code>.</p>
    </li>
    <li>
        <h2>Model Prediction</h2>
        <p><strong>Prediction Function:</strong> A function is created to predict the house price given the input features (<code>location</code>, <code>total_sqft</code>, <code>bath</code>, <code>bhk</code>).</p>
    </li>
</ol>
<h2>Major Steps:</h2>
<ul>
    <li><strong>Data Cleaning:</strong> Removing irrelevant columns and handling missing values.</li>
    <li><strong>Feature Engineering:</strong> Converting categorical and mixed-type columns into numerical columns.</li>
    <li><strong>Outlier Removal:</strong> Identifying and removing anomalies based on domain knowledge.</li>
    <li><strong>Model Training:</strong> Training a linear regression model with the processed data.</li>
    <li><strong>Model Saving:</strong> Storing the trained model and essential data columns for future use.</li>
    <li><strong>Prediction:</strong> Implementing a function to make predictions with the saved model.</li>
</ul>
