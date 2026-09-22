import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mali Santé Rurale", page_icon="🩺", layout="wide")

LANGS = {
    "Français": "fr", "English": "en", "Bamanankan": "bm",
    "Fulfulde": "ff", "Songhay": "son", "Soninké": "snk", "Tamasheq": "tmh"
}

T = {
"fr": {"title":"Projet pilote de santé rurale au Mali","subtitle":"Orientation maternelle et gestion des médicaments essentiels","maternal":"Orientation maternelle","stock":"Stock de médicaments","pilot":"Plan du projet pilote","notice":"Prototype de formation utilisant uniquement des données fictives. Il ne pose aucun diagnostic et ne remplace pas un professionnel de santé.","case":"Cas fictif : Aminata, 28 ans, grossesse de 31 semaines","bleeding":"Saignement abondant en ce moment ?","headache":"Fort mal de tête ou vision trouble ?","yes":"Oui","no":"Non","bp":"Tension artérielle","travel":"Durée du trajet vers le CSRéf","under30":"Moins de 30 minutes","30to60":"30 à 60 minutes","over60":"Plus de 60 minutes","assess":"Évaluer le risque","urgent":"Orientation urgente","review":"Révision clinique rapide","routine":"Suivi courant","urgent_reason":"Saignement abondant ou tension artérielle très élevée signalé.","review_reason":"Les symptômes ou la tension élevée exigent une révision par une sage-femme.","routine_reason":"Aucun signe de danger actuel dans cette démonstration.","steps":"Prochaines étapes","step1":"Appeler immédiatement la sage-femme désignée.","step2":"Alerter le centre d’accueil et confirmer sa capacité.","step3":"Mobiliser le transport et confirmer l’arrivée.","offline":"Enregistrer hors connexion","saved":"Dossier fictif enregistré localement.","product":"Produit","coverage":"Couverture","forecast":"Prévision","action":"Action recommandée","risk":"Risque élevé","monitor":"Surveiller","adequate":"Adéquat","sixmonth":"Projet pilote de six mois","safeguards":"Mesures de protection","validation":"Les traductions dans les langues maliennes sont préliminaires et doivent être validées localement avant toute utilisation."},
"en": {"title":"Mali Rural Health Pilot","subtitle":"Maternal referral and essential medicine management","maternal":"Maternal referral","stock":"Medicine supply","pilot":"Pilot plan","notice":"Training prototype using simulated data only. It does not diagnose or replace a health professional.","case":"Simulated case: Aminata, age 28, 31 weeks pregnant","bleeding":"Heavy bleeding now?","headache":"Severe headache or blurred vision?","yes":"Yes","no":"No","bp":"Blood pressure","travel":"Travel time to referral facility","under30":"Under 30 minutes","30to60":"30 to 60 minutes","over60":"More than 60 minutes","assess":"Assess risk","urgent":"Urgent referral","review":"Prompt clinical review","routine":"Routine follow-up","urgent_reason":"Heavy bleeding or severe-range blood pressure reported.","review_reason":"Symptoms or elevated blood pressure require midwife review.","routine_reason":"No current danger sign identified in this demonstration.","steps":"Next steps","step1":"Call the designated midwife immediately.","step2":"Alert the receiving facility and confirm capacity.","step3":"Activate transport and confirm arrival.","offline":"Save offline","saved":"Simulated record saved locally.","product":"Product","coverage":"Coverage","forecast":"Forecast","action":"Recommended action","risk":"High risk","monitor":"Monitor","adequate":"Adequate","sixmonth":"Six-month pilot","safeguards":"Safeguards","validation":"Translations in Malian languages are preliminary and require local validation before use."},
"bm": {"title":"Mali dugu kɔnɔ kɛnɛya porozɛ","subtitle":"Musow ka kɛnɛya ni furaw mara","maternal":"Musow ka kɛnɛya","stock":"Furaw mara","pilot":"Porozɛ taabolo","notice":"Nin ye kalan misali ye. A bɛ baara kɛ ni kunnafoni lafiyabaliw ye. A tɛ dɔgɔtɔrɔ nɔ bɔ.","case":"Misali: Aminata, san 28, kɔnɔmaya kalo 7 ni tila","bleeding":"Joli caman bɛ bɔ sisan wa?","headache":"Kun dimi jugu walima nyɛ finnen don wa?","yes":"Ɔwɔ","no":"Ayi","bp":"Joli teliya","travel":"Tuma min bɛ kɛ ka taa CSRéf la","under30":"Dɔgɔkun 30 duguma","30to60":"Dɔgɔkun 30 ka taa 60","over60":"Dɔgɔkun 60 sanfɛ","assess":"Farati lajɛ","urgent":"Ka taa furakɛyɔrɔ la joona","review":"Sage-femme ka lajɛ joona","routine":"Lajɛli kɔrɔlen","urgent_reason":"Joli caman walima joli teliya ka bon.","review_reason":"Taamasiɲɛw bɛ a jira ko sage-femme ka a lajɛ.","routine_reason":"Farati taamasiɲɛ si ma ye nin misali la.","steps":"Baaraw minnu ka kan ka kɛ","step1":"Sage-femme wele joona.","step2":"Furakɛyɔrɔ kunnafoniya.","step3":"Bolibana labɛn ani se yere dafa.","offline":"A mara internɛti kɔfɛ","saved":"Misali kunnafoni marala masin kan.","product":"Fura","coverage":"Don hakɛ","forecast":"Jateminɛ","action":"Baarakɛcogo","risk":"Farati ka bon","monitor":"A lajɛ","adequate":"A bɛ se","sixmonth":"Kalo wɔɔrɔ porozɛ","safeguards":"Lafiyabaliw","validation":"Mali kanw bamanankan na bayɛlɛmali nin bɛ fɔlɔfɔlɔ ye. Kanmɔgɔw ni kɛnɛya baarakɛlaw ka a lajɛ sani baara kɛ."},
}

# Preliminary interface translations. Clinical deployment requires professional review.
for code, name in [("ff","Fulfulde"),("son","Songhay"),("snk","Soninké"),("tmh","Tamasheq")]:
    T[code] = dict(T[fr"en"])
    T[code].update({"title":f"Mali Rural Health Pilot — {name}", "validation":f"{name} translation is a preliminary interface placeholder. Local linguistic and clinical validation is required."})

st.markdown("""<style>
.stApp{background:#f5faf8}.block-container{padding-top:1.5rem}.hero{background:#123f55;color:white;padding:1.5rem 1.8rem;border-radius:18px;margin-bottom:1rem}.hero h1{margin:0;color:white}.hero p{margin:.35rem 0 0;color:#cfe4e8}.risk-red{background:#bd3c35;color:white;padding:1rem;border-radius:14px}.risk-yellow{background:#d89516;color:white;padding:1rem;border-radius:14px}.risk-green{background:#2d7c58;color:white;padding:1rem;border-radius:14px}.small-note{font-size:.88rem;color:#5d6d75}
</style>""", unsafe_allow_html=True)

with st.sidebar:
    language = st.selectbox("Language / Langue / Kan", list(LANGS))
    lang = LANGS[language]
    tr = T[lang]
    st.info(tr["validation"])
    role_pages = [
        "🏠 Main concept hub / Portail principal",
        "🤰 Pregnant woman / Femme enceinte",
        "🧑🏾‍⚕️ Community health worker / Agent communautaire",
        "🏥 CSCOM–CSRéf clinical team / Équipe clinique",
        "💊 Pharmacy and logistics / Pharmacie et logistique",
        "📊 District–Ministry leadership / Direction et ministère",
    ]
    page = st.radio("Choose a workspace / Choisir un espace", role_pages)

st.markdown(f'<div class="hero"><h1>{tr["title"]}</h1><p>{tr["subtitle"]}</p></div>', unsafe_allow_html=True)
st.warning(tr["notice"])

def voice_guidance(text, button_label):
    payload = json.dumps(text)
    label = json.dumps(button_label)
    components.html(f"""
    <button onclick='speak()' style='width:100%;padding:13px 16px;border:1px solid #d7e0e3;border-radius:12px;background:white;color:#123f55;font:700 17px system-ui;cursor:pointer'>▶ <span id='label'></span></button>
    <script>
      document.getElementById('label').textContent = {label};
      function speak() {{
        if (!('speechSynthesis' in window)) {{ alert('Audio guidance is not supported by this browser.'); return; }}
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance({payload});
        utterance.lang = 'fr-FR';
        utterance.rate = 0.88;
        window.speechSynthesis.speak(utterance);
      }}
    </script>""", height=58)

if page.startswith("🏠"):
    st.subheader("Role-specific demonstration / Démonstration par rôle")
    st.write("This main page links five separate interfaces. Each person sees only the information and actions needed for their role.")
    st.write("Cette page principale relie cinq interfaces distinctes. Chaque personne voit uniquement les renseignements et les actions nécessaires à son rôle.")
    cards = [
        ("🤰", "Pregnant woman", "Voice-guided questions, simple safety messages, consent and help request."),
        ("🧑🏾‍⚕️", "Community health worker", "Offline screening, referral initiation, transport coordination and follow-up."),
        ("🏥", "CSCOM–CSRéf clinical team", "Clinical review queue, referral acceptance, arrival confirmation and outcome."),
        ("💊", "Pharmacy and logistics", "Stock coverage, shortage alerts, transfers and replenishment actions."),
        ("📊", "District–Ministry leadership", "Aggregated service, safety, equity and supply indicators without patient identities."),
    ]
    cols = st.columns(2)
    for i, (icon, title, body) in enumerate(cards):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### {icon} {title}")
                st.write(body)
    st.info("Concept demonstration: the final interfaces will be co-designed and validated with users, clinicians, CSRéf teams and Ministry of Health representatives.")

elif page.startswith("🤰"):
    st.subheader("Simple maternal check-in / Vérification maternelle simple")
    st.write("Use voice, pictures and short questions. A community health worker can assist when the woman does not own a phone or cannot read.")
    symptom = st.radio(tr["bleeding"], [tr["yes"], tr["no"]], horizontal=True, key="woman_bleeding")
    pain = st.radio(tr["headache"], [tr["yes"], tr["no"]], horizontal=True, key="woman_headache")
    if symptom == tr["yes"] or pain == tr["yes"]:
        st.error("Contact a community health worker or midwife now. / Contactez immédiatement un agent de santé ou une sage-femme.")
        message = "Alerte de démonstration. Contactez immédiatement un agent de santé ou une sage-femme."
    else:
        st.success("No danger sign reported in this short check. Continue scheduled care. / Aucun signe de danger signalé dans ce contrôle court.")
        message = "Démonstration. Continuez les consultations prénatales prévues."
    if st.button("Request help / Demander de l’aide", type="primary", use_container_width=True):
        st.info("Demo request sent to the assigned community health worker. / Demande fictive envoyée à l’agent communautaire.")
    voice_guidance(message, "Écouter les consignes / Listen to guidance")

elif page.startswith("🧑🏾‍⚕️"):
    st.subheader(tr["case"])
    left, right = st.columns([1.4, 1])
    with left:
        bleeding = st.radio(tr["bleeding"], [tr["yes"], tr["no"]], horizontal=True)
        headache = st.radio(tr["headache"], [tr["yes"], tr["no"]], horizontal=True)
        c1, c2 = st.columns(2)
        systolic = c1.number_input(f'{tr["bp"]} — systolique', 70, 240, 166)
        diastolic = c2.number_input(f'{tr["bp"]} — diastolique', 40, 160, 112)
        travel = st.selectbox(tr["travel"], [tr["under30"], tr["30to60"], tr["over60"]], index=1)
        assess = st.button(tr["assess"], type="primary", use_container_width=True)
        if st.button(tr["offline"], use_container_width=True): st.success(tr["saved"])
    with right:
        urgent = bleeding == tr["yes"] or systolic >= 160 or diastolic >= 110
        prompt = headache == tr["yes"] or systolic >= 140 or diastolic >= 90
        if urgent: level, reason, css = tr["urgent"], tr["urgent_reason"], "risk-red"
        elif prompt: level, reason, css = tr["review"], tr["review_reason"], "risk-yellow"
        else: level, reason, css = tr["routine"], tr["routine_reason"], "risk-green"
        st.markdown(f'<div class="{css}"><h2>{level}</h2><p>{reason}</p></div>', unsafe_allow_html=True)
        st.subheader(tr["steps"])
        for i, key in enumerate(["step1","step2","step3"],1): st.write(f"**{i}.** {tr[key]}")
        voice_choice = st.selectbox(
            "Langue du guide vocal / Voice guidance language",
            ["Français", "English", "Bamanankan"],
            key="voice_language",
        )
        voice_messages = {
            "Français": "Alerte de démonstration. Contactez la sage-femme. Préparez le transport vers le centre de référence." if urgent else "Démonstration. Contactez la sage-femme pour vérifier la situation.",
            "English": "Demonstration alert. Contact the midwife. Prepare transport to the referral facility." if urgent else "Demonstration. Contact the midwife to review the situation.",
            "Bamanankan": "Misali ye. Aw ye musokɛla dɔgɔtɔrɔ wele. Aw ye bolibana labɛn ka taa furakɛyɔrɔ la." if urgent else "Misali ye. Aw ye kɛnɛya baarakɛla wele ka ko lajɛ.",
        }
        voice_guidance(voice_messages[voice_choice], "Lire les consignes / Read guidance")

elif page.startswith("🏥"):
    st.subheader("Clinical review and referral queue / Révision clinique et orientations")
    m1, m2, m3 = st.columns(3)
    m1.metric("Urgent reviews / Révisions urgentes", "3")
    m2.metric("In transit / En route", "2")
    m3.metric("Arrival pending / Arrivée à confirmer", "1")
    st.dataframe([
        {"Case / Cas":"014", "From / Origine":"CSCOM rural A", "Status / Statut":"Urgent review", "Travel / Trajet":"45 min"},
        {"Case / Cas":"021", "From / Origine":"Village B", "Status / Statut":"In transit", "Travel / Trajet":"70 min"},
        {"Case / Cas":"008", "From / Origine":"CSCOM C", "Status / Statut":"Arrival pending", "Travel / Trajet":"25 min"},
    ], hide_index=True, use_container_width=True)
    st.subheader("Selected case / Cas sélectionné : 014")
    st.error("Simulated danger signs: heavy bleeding and blood pressure 166/112.")
    c1, c2 = st.columns(2)
    if c1.button("Accept referral / Accepter", type="primary", use_container_width=True): st.success("Referral accepted for demonstration.")
    if c2.button("Confirm arrival / Confirmer l’arrivée", use_container_width=True): st.success("Arrival recorded for demonstration.")
    st.caption("A qualified clinician makes the final clinical decision. The tool only organizes information and flags concerns.")

elif page.startswith("💊"):
    st.subheader(tr["stock"])
    rows = [
        ["Ocytocine / Oxytocin", "12", tr["risk"], "30 unités / units"],
        ["Sulfate de magnésium", "18", tr["monitor"], "Commander / Order"],
        ["TDR paludisme / Malaria RDT", "14", tr["risk"], "100 tests"],
        ["Amoxicilline / Amoxicillin", "31", tr["adequate"], "Routine"],
        ["Artéméther-luméfantrine", "38", tr["adequate"], "Aucune / None"],
    ]
    st.dataframe(rows, column_config={0:tr["product"],1:tr["coverage"],2:tr["forecast"],3:tr["action"]}, hide_index=True, use_container_width=True)
    st.caption("Données illustratives / Illustrative data")

else:
    st.subheader("District and Ministry overview / Vue du district et du ministère")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Women reached", "126")
    k2.metric("Urgent referrals", "18")
    k3.metric("Completed on time", "83%")
    k4.metric("Reporting completeness", "87%")
    st.caption("Illustrative aggregated values only. Leadership views exclude names, phone numbers and individual medical records.")
    st.subheader(tr["sixmonth"])
    phases = [("1–4", "Faisabilité / Feasibility"),("5–8", "Conception conjointe / Co-design"),("9–12", "Prototype hors connexion / Offline prototype"),("4–5", "Essai silencieux / Silent test"),("6", "Pilote limité / Limited pilot")]
    for period, label in phases: st.markdown(f"**{period}** — {label}")
    st.subheader(tr["safeguards"])
    st.markdown("- Human clinical review for urgent or uncertain results\n- Offline and paper fallback\n- No autonomous diagnosis or treatment\n- Safety and equity stopping rules\n- Local language and cultural validation")

st.divider()
st.caption("© 2026 Dr. Ibrahima Coulibaly · Demonstration only / Démonstration uniquement")
