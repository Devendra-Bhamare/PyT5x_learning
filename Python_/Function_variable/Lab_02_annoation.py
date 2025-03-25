
def add_before_Ui_after_Ui(function):
    def wrapper():
        print("before the running the Ui")
        print("Start the browser")
        function()
        print("Ending the running Ui TC")
        print("Quit the browser")
    return wrapper()



@add_before_Ui_after_Ui
def test_Ui():
    print("I will Test the Ui")