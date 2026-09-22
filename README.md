# Mali Rural Health Pilot — Streamlit

Multilingual demonstration of a rural maternal-referral and essential-medicine forecasting workflow for Mali.

## Languages

- French
- English
- Bamanankan
- Fulfulde
- Songhay
- Soninké
- Tamasheq

French, English, and Bamanankan include translated interface content. Fulfulde, Songhay, Soninké, and Tamasheq currently use clearly marked preliminary placeholders and require review by local speakers and health professionals before field use.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. Sign in at https://share.streamlit.io.
3. Select the repository, branch, and `app.py`.
4. Choose **Deploy**.

## Safety

This application uses simulated data. It is not a medical device and must not diagnose, prescribe, or replace clinical judgment. Local clinical governance, ethics review, linguistic validation, and security review are required before any pilot involving real people or data.
