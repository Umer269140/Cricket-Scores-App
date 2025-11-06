 # Cricket Scores App        

  A simple Flask web application that displays live cricket scores, provides score predictions, and allows users │
  to submit their own predictions.                                                                               │
                                                                                                                │
 ## Features   
 │
**Live Scores:** Fetches and displays live cricket scores from an RSS feed.       
│
**Score Predictions:** Provides a fun, randomized prediction for each match.     
│
**User Predictions:** Allows users to select a team they think will win.       
│
**Responsive Design:** A clean and modern user interface with a dark yellow theme.       
│
**About Page:** Provides information about the application.                                                │
                                                                                                           │
 ## File Structure                                                                                              │
                                                                                                             │
 The project is structured as follows:                                                                          │
                                                                                                              │
                                                                                                         │
 cricket_scores_app/                    
 app.py                           
 templates/                                                                                                 │
   '-- index.html                                                                                             │
   `-- about.html                                                                                             │
    `-- README.md                                                                                                  │
                                                                                                     │
 ## Code Explained                                                                                              │
                                                                                                 │
 **`app.py`**: This is the main Flask application file.                                                     │
  It uses the `requests` library to fetch live cricket scores from an RSS feed.                          │
  `BeautifulSoup` is used to parse the XML data from the feed.                                           │
   *   It defines two routes:                                                                                 │
        *   `/`: The home page, which displays the live scores.                                                │
       *   `/about`: The about page.                                                                          │
  *   It processes the data, extracts team names and flags, and generates a random score prediction for each │
     match.                                                                                                         │
                                                                                                             │
*   **`templates/index.html`**: This is the main page of the application.                                      │
   *   It uses Jinja2 templating to dynamically display the score data passed from the Flask application.     │
   *   The page is styled with CSS to create a modern and visually appealing layout.                          │
  *   It includes a section for score predictions and a form for users to submit their own predictions.      │
                                                                                                           │
 *   **`templates/about.html`**: This page provides information about the application.                          │
   *   It is styled consistently with the main page.                                                          │
                                                                                                              │
## How to Run                                                                                                  │
                                                                                                               │
 **Install dependencies:**                                                                                  │
    ```bash                                                                                                    │
     pip install 
     Flask requests beautifulsoup4                                                                  │
                                                                                               │
  **Run the application:**                                                                                   │
   ```bash                                                                                                    │
    python app.py                                                                                              │

Open your web browser and go to `http://127.0.0.1:5000/`.           
