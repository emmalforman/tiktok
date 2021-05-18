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
