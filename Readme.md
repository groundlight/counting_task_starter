# Counting Task Starter

This code is designed to show a minimal working example of running a counting task with groundlight.

# Setup

To set up, you will need to first create a counting detector at dashboard.groundlight.ai and create an api token. Export these as environment variables with:

```bash
export GROUNDLIGHT_API_TOKEN=<your token>
export GROUNDLIGHT_DETECTOR_ID=<your detector id>
```

(Note if you prefere you can also change the values in the demo.py file)

You will also need to install the groundlight python package. If you're using poetry, you can do this from the root of this repository with:

```bash
poetry install
```

If using pip and venv, you can do this with:

```bash
python -m venv venv
activate venv/bin/activate
pip groundlight
```

# Running the code
You can now run the code with:

```bash
python demo.py
```

The demo will show how to submit 3 images to the detector and display their results