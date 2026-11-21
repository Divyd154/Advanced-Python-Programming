import logging

# Save log messages to app.log and show them on the screen
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    logging.debug("Calculated result: %s", result)
    print("Result:", result)

except ValueError:
    logging.exception("Invalid input: please enter a number")
    print("Please enter a valid number.")

except ZeroDivisionError:
    logging.exception("Cannot divide by zero")
    print("The number cannot be zero.")

finally:
    logging.info("Program finished")