#Objective 4: Application Health Checker
import requests
import logging

# Set up logging
logging.basicConfig(filename='application_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Application URL
APP_URL = 'http://example.com'

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info('Application is UP')
            return 'UP'
        else:
            logging.warning(f'Application is DOWN. Status code: {response.status_code}')
            return 'DOWN'
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is DOWN. Error: {e}')
        return 'DOWN'

if __name__ == "__main__":
    status = check_application_status(APP_URL)
    print(f'Application status: {status}')
