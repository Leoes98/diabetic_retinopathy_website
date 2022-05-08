# Diabetic Retinopathy Classification Website

## Table of Contents

- [DESCRIPTION](#description)
- [LINKS](#links)
- [RESOURCES](#resources)

## DESCRIPTION

This project deployed the AI model from [diabetic_retinopathy_DL](https://github.com/Leoes98/diabetic_retinopathy_DL) repository on a website using Heroku.


This platform is meant to reduce the gap between AI and medicine. This AI DR assistant is an accessible online system to support medical professionals during the diagnosis. The physician uploads a retina image to be classified by the AI model.


The prediction will show one of these outputs:

- 0: No DR.
- 1: Mild DR.
- 2: Severe DR.

### Update
The previous version used an API to get the predictions. However, it was deployed on GCP and currently the license is no available. The current version directly uses the TFLite model.

## LINKS

🌟 [Web app URL](https://spiffy-mermaid-49dc45.netlify.app/)


## RESOURCES

This platform was made deployed:
- [Heroku](https://www.heroku.com/)
- [Streamlit](https://streamlit.io/)
