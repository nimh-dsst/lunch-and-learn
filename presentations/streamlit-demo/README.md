# Streamlit DANDI API Dashboard Demo

## Presenter: Josh Lawrimore <josh.lawrimore@nih.gov>

## 10/22/2024

This repository contains a bare-bones demonstration of how [Streamlit](https://streamlit.io/) can be used to create an interactive dashboard using the [DANDI](https://dandiarchive.org/) (Distributed Archives for Neurophysiology Data Integration) brain archive API. The demo showcases data visualizations and insights not readily available on the DANDI website.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project serves as a proof-of-concept, illustrating how Streamlit can be leveraged to build user-friendly web interfaces that interact with scientific APIs. By using the DANDI API as an example, we demonstrate how to create custom visualizations and data presentations that extend beyond what's available on the official DANDI website.

The main goals of this demo are:

1. To show how Streamlit can quickly create interactive web apps
2. To demonstrate integration with external APIs (in this case, DANDI)
3. To showcase custom data processing and visualization of neurophysiology data

## Features

- List the number of Dandisets in the API
- List the number of Dandisets that throw a metadata validation error
- List the number of keywords present in valid dandisets
- Show the counts of each Daniset keyword in DataFrame

Note: This is a minimal implementation intended for demonstration purposes.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/streamlit-dandi-demo.git
   cd streamlit-dandi-demo
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the sidebar to interact with the demo features and explore how Streamlit can present DANDI data in novel ways.

## Dependencies

- streamlit
- dandi
- matplotlib

For a complete list of dependencies, see the `requirements.txt` file.

## Contributing

This demo is intended as a starting point. Contributions that extend its functionality or improve its educational value are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Create a new Pull Request

Please ensure your code adheres to the project's coding standards and includes appropriate comments for educational purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For more information on the DANDI archive, visit [dandiarchive.org](https://dandiarchive.org/).

For Streamlit documentation, visit [docs.streamlit.io](https://docs.streamlit.io/).

Remember, this demo is not affiliated with or endorsed by DANDI. It is an independent project created for educational and demonstration purposes.
