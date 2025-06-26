from blueprintapp.app import create_app

# call the factory function to create and configure Flask application instance
flask_app = create_app()

# check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # start the Flask development server on port 5571 with debug mode enabled
    flask_app.run(port=5571, debug=True)