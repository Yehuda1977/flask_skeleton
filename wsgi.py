from webapp import create_app
import config

app = create_app(config.current_config)


# This should be in create_app (you can create a function in a function.)
@app.shell_context_processor
def inject_variables_to_shell():
    """
    Return a dictionary of variables to inject ({variable_name: variable_value})
    Those variables will be accessible in the flask shell (without having to import them)
    """
    return {
        # Your variables here
        "my_var": "value",
    }



if __name__ == "__main__":
    app.run(port=5000, debug=True)


