import groundlight
import os

gl = groundlight.GroundLight()
det = os.environ.get('GROUNDLIGHT_DETECTOR_ID')

print(gl) # verify that you are logged in correctly

# submits two images to groundlight. The results you get back may differ depending on the maturity of the model
iq = gl.submit_image_query(det, "images/4_people.jpg")
print(f"In the first image, we see {iq.result.label} people") # Note: for the time being, label is a string. Stay tuned for updates to our SDK

gl.submit_image_query(det, "images/crowd.jpg")
print(f"In the first image, we see {iq.result.label} people")