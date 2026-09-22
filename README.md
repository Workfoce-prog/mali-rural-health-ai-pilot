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

The maternal-referral screen includes browser-based spoken guidance in French, English, and Bamanankan. Audio availability and voice quality depend on the browser and device.

## Role-specific workspaces

The main concept hub links to five separate demonstration interfaces:

1. Pregnant woman: short, voice-guided questions and a help request.
2. Community health worker: offline screening, referral initiation and transport follow-up.
3. CSCOM–CSRéf clinical team: clinical review, referral acceptance and arrival confirmation.
4. Pharmacy and logistics: medicine coverage, shortage warnings and replenishment actions.
5. District and Ministry leadership: aggregated service, safety, equity and supply indicators without patient identities.

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
