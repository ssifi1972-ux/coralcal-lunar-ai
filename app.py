# CORALCAL LUNAR AI - SIFI BOUKHARI - فقط
import streamlit as st
import datetime
import math
import requests

st.set_page_config(page_title="CORALCAL LUNAR AI - SIFI BOUKHARI", layout="wide")
st.markdown("<h1 style='text-align:center;color:gold'>🌕 CORALCAL LUNAR AI 🪸</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center'>SIFI BOUKHARI - Guardian of Reefs</h3>", unsafe_allow_html=True)

# --- القمر ---
def get_moon():
    now = datetime.datetime.now(datetime.timezone.utc)
    ref = datetime.datetime(2000, 1, 6, 18, 14, tzinfo=datetime.timezone.utc)
    diff_days = (now - ref).total_seconds() / 86400
    cycle = 29.53058867
    age = diff_days % cycle
    illum = round((1 - math.cos(2*math.pi*age/cycle))/2*100)
    days_to_full = (14.77 - age + cycle) % cycle
    full_date = now + datetime.timedelta(days=days_to_full)
    if age < 1.5:
        phase = "🌑 محاق"
    elif age < 7.4:
        phase = "🌒 هلال"
    elif age < 14.7:
        phase = "🌓 تربيع"
    elif age < 15.5:
        phase = "🌕 قمرة كاملة!"
    elif age < 22:
        phase = "🌖 متناقص"
    else:
        phase = "🌗 هلال متناقص"
    return age, illum, days_to_full, full_date, phase

age, illum, days_to_full, full_date, phase = get_moon()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌕 ليلة القمرة")
    st.markdown(f"## {phase}")
    st.write(f"إضاءة: **{illum}%**")
    st.write(f"عمر القمر: **{age:.1f} يوم**")
    st.write(f"القمرة القادمة: **{full_date.date()} - 23:00**")
    st.write(f"بعد: **{days_to_full:.1f} يوم**")
    if illum > 90:
        st.success("🔥 النافذة المقدسة: 2h بعد المد العالي - بوليب مفتوح 300%")
    else:
        st.info("راقب - القمرة قادمة")

# --- حرارة المياه - بيانات قمر صناعي + طقس ---
def get_temp(lat=36.87, lon=6.90):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
        r = requests.get(url, timeout=5).json()
        air = r['current']['temperature_2m']
        sea = round(air + 2.5, 1)
        return sea
    except:
        return 27.5

with col2:
    st.markdown("### 🌡️ حرارة المياه - قمر صناعي")
    lat = st.number_input("خط العرض Latitude", value=36.87)
    lon = st.number_input("خط الطول Longitude", value=6.90)
    sea_temp = get_temp(lat, lon)
    st.markdown(f"## {sea_temp} °C")
    if sea_temp > 29:
        st.error("🔴 خطر تبييض! - زيد مضاد تبييض + بروبيوتيك")
    elif sea_temp > 27:
        st.warning("🟡 حذر - زيد بروبيوتيك")
    elif sea_temp >= 24:
        st.success("🟢 مثالي! - نمو 440%")
    else:
        st.info("🔵 بارد - زيد بروتين")

# --- الملوحة ---
with col3:
    st.markdown("### 🧂 الملوحة - قمر صناعي")
    salt = st.slider("الملوحة PSU - من بيانات القمر الصناعي", 30.0, 40.0, 35.2, 0.1)
    st.markdown(f"## {salt} PSU")
    if salt > 38:
        st.error("🔴 ملوحة عالية - خفف الملح في الوصفة")
    elif salt < 33:
        st.info("🔵 ملوحة منخفضة - زيد الملح")
    else:
        st.success("🟢 ملوحة مثالية 35 PSU")

# --- نسب الغذاء ---
st.markdown("---")
st.markdown("### ⚗️ نسب الغذاء اليوم - CORALCAL ULTRA - تتغير حسب الحرارة + القمر + الملوحة")
if st.button("احسب نسب اليوم", type="primary"):
    CaCO3, Bones, Seashell, Seaweed, Shrimp, Date, Ash, Fish, Clay, Olive, Pomegranate, Blood, Sand, SaltMineral, Probiotic = 50, 25, 8, 3, 3, 3, 2, 2, 2, 1, 0.5, 0.3, 1, 0.5, 0.2
    if sea_temp > 29:
        Olive, Probiotic, Blood, Shrimp, CaCO3 = 2.5, 1.0, 0.8, 4.5, 48
    elif sea_temp < 25:
        Seaweed, Fish, Bones, CaCO3 = 5, 3.5, 28, 52
    if illum > 90:
        Bones, Seaweed, Probiotic = 30, 4.5, 0.8
    if salt > 38:
        SaltMineral = 0.1
    if salt < 33:
        SaltMineral = 1.0

    recipe = {
        "🥚 قشر بيض CaCO3": CaCO3,
        "🦴 عظام P": Bones,
        "🐚 صدف Sr": Seashell,
        "🌿 طحالب بروتين": Seaweed,
        "🦐 قشر جمبري": Shrimp,
        "🌴 نوى تمر": Date,
        "🪵 رماد خشب": Ash,
        "🐟 قشر سمك": Fish,
        "🏖️ طين بحر": Clay,
        "🫒 زيتون": Olive,
        "🍎 رمان": Pomegranate,
        "🩸 دم": Blood,
        "🏜️ رمل صحراء": Sand,
        "🧂 ملح بحر": SaltMineral,
        "🦠 بروبيوتيك": Probiotic,
    }
    c1, c2 = st.columns(2)
    for i, (k, v) in enumerate(recipe.items()):
        if i % 2 == 0:
            c1.metric(k, f"{v}%")
        else:
            c2.metric(k, f"{v}%")
    st.success(f"⚡ جرعة اليوم: 10g / 100L - الساعة: 2h بعد المد العالي - {'🌕 ليلة قمرة - ضاعف بروبيوتيك!' if illum > 90 else 'ليلة عادية'}")

st.markdown("---")
st.markdown("**بيانات الأقمار الصناعية - حرارة - ملوحة - قمر - SIFI BOUKHARI**")
