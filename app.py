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

ROLE = {
"en": {"choose":"Choose a workspace","hub":"Main concept hub","woman":"Pregnant woman","chw":"Community health worker","clinical":"CSCOM–CSRéf clinical team","pharmacy":"Pharmacy and logistics","leadership":"District–Ministry leadership","role_demo":"Role-specific demonstration","hub_intro":"This main page links five separate interfaces. Each person sees only the information and actions needed for their role.","woman_desc":"Voice-guided questions, simple safety messages, consent and help request.","chw_desc":"Offline screening, referral initiation, transport coordination and follow-up.","clinical_desc":"Clinical review queue, referral acceptance, arrival confirmation and outcome.","pharmacy_desc":"Stock coverage, shortage alerts, transfers and replenishment actions.","leadership_desc":"Aggregated service, safety, equity and supply indicators without patient identities.","concept":"Concept demonstration: final interfaces will be co-designed and validated with users, clinicians, CSRéf teams and Ministry of Health representatives.","checkin":"Simple maternal check-in","checkin_help":"Use voice, pictures and short questions. A community health worker can assist when the woman does not own a phone or cannot read.","contact_now":"Contact a community health worker or midwife now.","continue_care":"No danger sign reported in this short check. Continue scheduled care.","request_help":"Request help","request_sent":"Demo request sent to the assigned community health worker.","clinical_queue":"Clinical review and referral queue","selected_case":"Selected case","accept":"Accept referral","arrival":"Confirm arrival","clinical_rule":"A qualified clinician makes the final clinical decision. The tool only organizes information and flags concerns.","lead_title":"District and Ministry overview","aggregate_note":"Illustrative aggregated values only. Leadership views exclude names, phone numbers and individual medical records."},
"fr": {"choose":"Choisir un espace","hub":"Portail principal","woman":"Femme enceinte","chw":"Agent de santé communautaire","clinical":"Équipe clinique CSCOM–CSRéf","pharmacy":"Pharmacie et logistique","leadership":"Direction du district et ministère","role_demo":"Démonstration par rôle","hub_intro":"Cette page principale relie cinq interfaces distinctes. Chaque personne voit uniquement les renseignements et les actions nécessaires à son rôle.","woman_desc":"Questions guidées par la voix, messages simples de sécurité, consentement et demande d’aide.","chw_desc":"Dépistage hors connexion, lancement de l’orientation, coordination du transport et suivi.","clinical_desc":"File de révision clinique, acceptation de l’orientation, confirmation de l’arrivée et résultat.","pharmacy_desc":"Couverture des stocks, alertes de rupture, transferts et réapprovisionnement.","leadership_desc":"Indicateurs agrégés sur les services, la sécurité, l’équité et les stocks, sans identité des patientes.","concept":"Démonstration conceptuelle : les interfaces finales seront conçues et validées avec les utilisatrices, les cliniciens, les équipes des CSRéf et le ministère de la Santé.","checkin":"Vérification maternelle simple","checkin_help":"Utiliser la voix, des images et des questions courtes. Un agent communautaire peut aider une femme sans téléphone ou qui ne sait pas lire.","contact_now":"Contactez immédiatement un agent de santé communautaire ou une sage-femme.","continue_care":"Aucun signe de danger signalé dans ce contrôle court. Poursuivez les soins prévus.","request_help":"Demander de l’aide","request_sent":"Demande fictive envoyée à l’agent communautaire désigné.","clinical_queue":"File de révision clinique et d’orientation","selected_case":"Cas sélectionné","accept":"Accepter l’orientation","arrival":"Confirmer l’arrivée","clinical_rule":"Un clinicien qualifié prend la décision clinique finale. L’outil organise les renseignements et signale les préoccupations.","lead_title":"Vue du district et du ministère","aggregate_note":"Valeurs agrégées illustratives uniquement. La vue de direction exclut les noms, numéros de téléphone et dossiers médicaux individuels."},
"bm": {"choose":"Baarakɛyɔrɔ sugandi","hub":"Baarakɛyɔrɔba","woman":"Musokɔnɔma","chw":"Dugukolo kɛnɛya baarakɛla","clinical":"CSCOM–CSRéf kɛnɛya baarakɛlaw","pharmacy":"Furaw ni donanw","leadership":"Disitiri ni ministɛri","role_demo":"Baarakɛla kelen kelen bɛɛ ka misali","hub_intro":"Nin yɔrɔba bɛ taa baarakɛyɔrɔ duuru la. Mɔgɔ kelen kelen bɛ a ka baara de kunnafoni ye.","woman_desc":"Kumakan na ɲininkali surunw, lafiya kunnafoni ni dɛmɛ ɲinini.","chw_desc":"Farati lajɛli internɛti kɔfɛ, bolibana labɛn ani kɔlɔsili.","clinical_desc":"Dɔgɔtɔrɔ ka lajɛli, banna sɔnni, se yere dafa ani laban.","pharmacy_desc":"Furaw hakɛ, furaw bannen kunnafoni ani furaw lasegin.","leadership_desc":"Kɛnɛya baara ni furaw jateminɛ, mɔgɔ tɔgɔ tɛ yen.","concept":"Nin ye hakilina misali ye. Baarakɛyɔrɔ laban bɛ dilan ni baarakɛlaw, dɔgɔtɔrɔw, CSRéf ni Kɛnɛya Ministɛri ye.","checkin":"Musokɔnɔma ka lajɛli surun","checkin_help":"Kumakan, ja ni ɲininkali surunw baara kɛ. Kɛnɛya baarakɛla bɛ se ka dɛmɛ kɛ.","contact_now":"Kɛnɛya baarakɛla walima sage-femme wele sisan.","continue_care":"Farati taamasiɲɛ si ma fɔ. I ka taa ɲɛ ni lajɛli dabɔlen ye.","request_help":"Dɛmɛ ɲini","request_sent":"Dɛmɛ ɲinini misali ci la kɛnɛya baarakɛla ma.","clinical_queue":"Dɔgɔtɔrɔ ka lajɛli ni bolibana","selected_case":"Bana sugandilen","accept":"Banna sɔn","arrival":"Se yere dafa","clinical_rule":"Dɔgɔtɔrɔ ka kan ka laban latigɛ. Minɛn bɛ kunnafoniw labɛn ani farati jira.","lead_title":"Disitiri ni ministɛri ka lajɛli","aggregate_note":"Nin jateminɛw ye misali ye. Mɔgɔ tɔgɔ, telefɔni nimɔrɔ ani furakɛ kunnafoni danfaralen tɛ yen."}
}

st.markdown("""<style>
.stApp{background:#f5faf8}.block-container{padding-top:1.5rem}.hero{background:#123f55;color:white;padding:1.5rem 1.8rem;border-radius:18px;margin-bottom:1rem}.hero h1{margin:0;color:white}.hero p{margin:.35rem 0 0;color:#cfe4e8}.risk-red{background:#bd3c35;color:white;padding:1rem;border-radius:14px}.risk-yellow{background:#d89516;color:white;padding:1rem;border-radius:14px}.risk-green{background:#2d7c58;color:white;padding:1rem;border-radius:14px}.small-note{font-size:.88rem;color:#5d6d75}
</style>""", unsafe_allow_html=True)

with st.sidebar:
    language = st.selectbox("Language / Langue / Kan", list(LANGS))
    lang = LANGS[language]
    tr = T[lang]
    role = ROLE.get(lang, ROLE["en"])
    st.info(tr["validation"])
    role_pages = [
        f"🏠 {role['hub']}", f"🤰 {role['woman']}", f"🧑🏾‍⚕️ {role['chw']}",
        f"🏥 {role['clinical']}", f"💊 {role['pharmacy']}", f"📊 {role['leadership']}",
    ]
    page = st.radio(role["choose"], role_pages)

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
    st.subheader(role["role_demo"])
    st.write(role["hub_intro"])
    cards = [
        ("🤰", role["woman"], role["woman_desc"]), ("🧑🏾‍⚕️", role["chw"], role["chw_desc"]),
        ("🏥", role["clinical"], role["clinical_desc"]), ("💊", role["pharmacy"], role["pharmacy_desc"]),
        ("📊", role["leadership"], role["leadership_desc"]),
    ]
    cols = st.columns(2)
    for i, (icon, title, body) in enumerate(cards):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"### {icon} {title}")
                st.write(body)
    st.info(role["concept"])

elif page.startswith("🤰"):
    st.subheader(role["checkin"])
    st.write(role["checkin_help"])
    symptom = st.radio(tr["bleeding"], [tr["yes"], tr["no"]], horizontal=True, key="woman_bleeding")
    pain = st.radio(tr["headache"], [tr["yes"], tr["no"]], horizontal=True, key="woman_headache")
    if symptom == tr["yes"] or pain == tr["yes"]:
        st.error(role["contact_now"])
        message = "Alerte de démonstration. Contactez immédiatement un agent de santé ou une sage-femme."
    else:
        st.success(role["continue_care"])
        message = "Démonstration. Continuez les consultations prénatales prévues."
    if st.button(role["request_help"], type="primary", use_container_width=True):
        st.info(role["request_sent"])
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
    st.subheader(role["clinical_queue"])
    m1, m2, m3 = st.columns(3)
    m1.metric("Urgent reviews / Révisions urgentes", "3")
    m2.metric("In transit / En route", "2")
    m3.metric("Arrival pending / Arrivée à confirmer", "1")
    st.dataframe([
        {"Case / Cas":"014", "From / Origine":"CSCOM rural A", "Status / Statut":"Urgent review", "Travel / Trajet":"45 min"},
        {"Case / Cas":"021", "From / Origine":"Village B", "Status / Statut":"In transit", "Travel / Trajet":"70 min"},
        {"Case / Cas":"008", "From / Origine":"CSCOM C", "Status / Statut":"Arrival pending", "Travel / Trajet":"25 min"},
    ], hide_index=True, use_container_width=True)
    st.subheader(f"{role['selected_case']} : 014")
    st.error("Simulated danger signs: heavy bleeding and blood pressure 166/112.")
    c1, c2 = st.columns(2)
    if c1.button(role["accept"], type="primary", use_container_width=True): st.success(role["accept"])
    if c2.button(role["arrival"], use_container_width=True): st.success(role["arrival"])
    st.caption(role["clinical_rule"])

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
    st.subheader(role["lead_title"])
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Women reached", "126")
    k2.metric("Urgent referrals", "18")
    k3.metric("Completed on time", "83%")
    k4.metric("Reporting completeness", "87%")
    st.caption(role["aggregate_note"])
    st.subheader(tr["sixmonth"])
    phases = [("1–4", "Faisabilité / Feasibility"),("5–8", "Conception conjointe / Co-design"),("9–12", "Prototype hors connexion / Offline prototype"),("4–5", "Essai silencieux / Silent test"),("6", "Pilote limité / Limited pilot")]
    for period, label in phases: st.markdown(f"**{period}** — {label}")
    st.subheader(tr["safeguards"])
    st.markdown("- Human clinical review for urgent or uncertain results\n- Offline and paper fallback\n- No autonomous diagnosis or treatment\n- Safety and equity stopping rules\n- Local language and cultural validation")

st.divider()
st.caption("© 2026 Dr. Ibrahima Coulibaly · Demonstration only / Démonstration uniquement")
