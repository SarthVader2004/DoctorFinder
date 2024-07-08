# Doctor Finder

![Doctor Finder](images/doctor-finder.png)

## Overview
Doctor Finder is a user-friendly application designed to help users quickly locate doctors based on their specialty. By selecting the type of doctor they need, users can initiate a search that opens their browser with results for nearby doctors. This project leverages Flet for the front-end interface and integrates seamlessly with web browsers for search functionality.

## Features
- **Specialty Selection**: Allows users to select from a list of doctor types.
- **Quick Search**: Initiates a Google search for the selected type of doctor near the user.
- **User-Friendly Interface**: Clean and intuitive design for easy interaction.

## Technologies Used
- **Programming Language**: Python
- **Library**: 
  - [Flet](https://flet.dev/): For creating the interactive web application interface.
  - [webbrowser](https://docs.python.org/3/library/webbrowser.html): For opening the browser and conducting the search.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/doctor-finder.git
    cd doctor-finder
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python app.py
    ```

2. **Access the Web Interface**:
   The application will open automatically in your default web browser.

## Project Structure
- `app.py`: Main application script.
- `requirements.txt`: List of dependencies.

## Code Explanation
The code for Doctor Finder is simple and straightforward:
- **Doctor Types**: A list of doctor specialties is defined.
- **Dropdown Menu**: A dropdown menu allows users to select the type of doctor they are looking for.
- **Search Function**: When the search button is clicked, the selected doctor type is used to perform a Google search for nearby doctors.
