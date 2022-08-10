# NASA'S PICTURE OF THE DAY

This script retrieves the daily pic published by NASA on their website. It uses the APOD API to do so, storing the image in a directory. If you run he script daily through your prefered IDE, you'll have a new picture every day. Also, stay tuned to the command line, and you will see a description of the image and its context.

Before running, you need to install the required modules (I'd recommend using a virtual environment) using this command:

```
pip install requirements.txt
```

Note that the script won't run correctly until you get an API KEY from https://api.nasa.gov/. When you do have it, copy and paste it as the value of the environment variable API_KEY, at the start of the script.

Example of image retrieved running the script on 08/03/2022:

![image](https://user-images.githubusercontent.com/102031726/182588025-841de43b-f1e6-4040-8967-1450eaee8c24.png)

To avoid running the script manually, follow these steps:

1. Delete this line on main.py:
    ```python
    todays_image()
    ```

2. Add the following lines at the end of the code:
    ```python
    import schedule

    schedule.every(24).hours.do(todays_image)
    while 1:
    schedule.run_pending()
    ```

3. Change the extension of main.py to main.pyw, to run the program in the background.

4. Run the script on a Linux server that doesn't shuts down when your pc does so.


