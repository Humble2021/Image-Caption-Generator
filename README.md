# Image Caption Generator

This Image Caption Generator is a web application built using Streamlit, a Python library for creating interactive web applications. It leverages Google's Generative AI API to generate captions for images. The application provides users with the flexibility to generate captions for images with customizable lengths and supports different platforms such as Instagram.

## Features

- Upload an image and generate a caption for it.
- Customize the length of the generated caption.
- Generate captions specifically tailored for Instagram.

## Installation

To run the Image Caption Generator locally, follow these steps:

1. Clone the repository containing the code.
2. Navigate to the project directory.
3. Create a Python virtual environment:
    ```
    python -m venv venv
    ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies using pip:
    ```
    pip install -r Requirements.txt
    ```
6. Create a `.env` file in the project directory and add your Google Generative AI API key to it. For example:
    ```
    GENAI_API_KEY=YOUR_GENERATIVE_AI_API_KEY
    ```

## Usage

To run the Image Caption Generator, execute the following command in your terminal:

```
streamlit run app.py
```

This will start a local web server hosting the application. You can access it by opening a web browser and navigating to `http://localhost:8501`.

### Generating Captions

1. Upload an image by clicking on the "Choose an image..." button.
2. Use the slider to select the desired length of the generated caption.
3. Click the "Identify image" button to generate a caption.
4. Optionally, you can click the "Insta Caption" button to generate a caption specifically tailored for Instagram.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

## License

This project is licensed under the terms of the [MIT License](LICENSE), © 2024 @Humble2021.
