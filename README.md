# TikTok App (Python)

Sends you a customized email every morning, with information of interest, such as the upcoming weather forecast for your zip code.



## Installation

Fork navigate there from the command-line:

```sh
cd ~/Desktop/tiktok-py/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "briefings-env":

```sh
conda create -n tiktok-env python=3.8
conda activate tiktok-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install TikTokApi
python -m playwright install
```

## Configuration

Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API key (i.e. `SENDGRID_API_KEY`).

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"


```

## Usage

Printing trending TikTok's:

```sh
python -m app.tiktok

## Testing

Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```


## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server and schedule the server to send you the weather forecast email every day.

## [License](/LICENSE.md)
