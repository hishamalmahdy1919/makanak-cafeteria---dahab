# -*- coding: utf-8 -*-
import os

OUT = "."

# روابط الاتصال والسوشيال ميديا الخاصة بك
SITE_URL = "https://www.planetdivers.com"
EMAIL = "ahmedtahasayed@gmail.com"
WHATSAPP = "+201110111549"
WHATSAPP_LINK = "https://wa.me/201110111549"
FACEBOOK_LINK = "https://www.facebook.com/share/1BmH81bbUH/"
TIKTOK_LINK = "https://www.tiktok.com/@ahmedtaha5222?_r=1&_t=ZS-9883zJjl3cT"
LOCATION_LINK = "https://maps.app.goo.gl/YeLti1DH81tJYVQF9?g_st=aw"
# تم تحديث لينك جوجل هنا 👇
GOOGLE_LINK = "https://share.google/L3e6XGfntB44pETMQ"

# ==================================================================== #
# 1. صور وجمل العرض المتداخلة (Slideshow)
# ==================================================================== #
HERO_SLIDES = [
    {
        "image": "hero-slide1.jpg",
        "text": {
            "en": "Explore the Blue Hole", "ar": "استكشف أعماق البلوهول",
            "ru": "Исследуйте Голубую дыру", "it": "Esplora il Blue Hole",
            "fr": "Explorez le Blue Hole", "de": "Entdecke das Blue Hole",
            "zh": "探索蓝洞", "es": "Explora el Blue Hole"
        }
    },
    {
        "image": "hero-slide2.jpg",
        "text": {
            "en": "Master Your Breath", "ar": "تحكم في أنفاسك",
            "ru": "Овладейте своим дыханием", "it": "Padroneggia il respiro",
            "fr": "Maîtrisez votre souffle", "de": "Meistere deinen Atem",
            "zh": "掌控呼吸", "es": "Domina tu respiración"
        }
    },
    {
        "image": "hero-slide3.jpg",
        "text": {
            "en": "Dive with Professionals", "ar": "غُص مع المحترفين",
            "ru": "Погружайтесь с профи", "it": "Immergiti con i professionisti",
            "fr": "Plongez avec les pros", "de": "Tauche mit Profis",
            "zh": "与专家潜水", "es": "Bucea con profesionales"
        }
    },
    {
        "image": "hero-slide4.jpg",
        "text": {
            "en": "Relax at Our Cafeteria", "ar": "استرخِ في الكافيه الخاص بنا",
            "ru": "Отдохните в нашем кафе", "it": "Rilassati nella nostra caffetteria",
            "fr": "Détendez-vous à notre cafétéria", "de": "Entspannen Sie in unserer Cafeteria",
            "zh": "在我们的咖啡厅放松", "es": "Relájate en nuestra cafetería"
        }
    },
    {
        "image": "hero-slide5.jpg",
        "text": {
            "en": "Discover the Red Sea", "ar": "اكتشف سحر البحر الأحمر",
            "ru": "Откройте для себя Красное море", "it": "Scopri il Mar Rosso",
            "fr": "Découvrez la mer Rouge", "de": "Entdecken Sie das Rote Meer",
            "zh": "探索红海", "es": "Descubre el Mar Rojo"
        }
    },
    {
        "image": "hero-slide6.jpg",
        "text": {
            "en": "Unforgettable Experience", "ar": "تجربة لا تُنسى",
            "ru": "Незабываемый опыт", "it": "Esperienza indimenticabile",
            "fr": "Expérience inoubliable", "de": "Unvergessliches Erlebnis",
            "zh": "难忘的经历", "es": "Experiencia inolvidable"
        }
    },
    {
        "image": "hero-slide7.jpg",
        "text": {
            "en": "Expert Instructors", "ar": "مدربون خبراء",
            "ru": "Опытные инструкторы", "it": "Istruttori esperti",
            "fr": "Instructeurs experts", "de": "Erfahrene Ausbilder",
            "zh": "专家教练", "es": "Instructores expertos"
        }
    },
    {
        "image": "hero-slide8.jpg",
        "text": {
            "en": "Join Our Community", "ar": "انضم إلى مجتمع الغواصين",
            "ru": "Присоединяйтесь к нашему сообществу", "it": "Unisciti alla nostra community",
            "fr": "Rejoignez notre communauté", "de": "Treten Sie unserer Gemeinschaft bei",
            "zh": "加入我们的社区", "es": "Únete a nuestra comunidad"
        }
    }
]

# ==================================================================== #
# 2. الفيديوهات المحلية القصيرة (Shorts) - 14 فيديو
# ==================================================================== #
LOCAL_SHORTS = [
    "short-1.mp4",
    "short-2.mp4",
    "short-3.mp4",
    "short-4.mp4",
    "short-5.mp4",
    "short-6.mp4",

]

SAFARI_IMAGES = ["safari-1.jpg", "safari-2.jpg", "safari-3.jpg"]
YOUTUBE_VIDEOS = []

# ==================================================================== #

COURSES = [
    {"course": "AIDA 1", "days": 2, "price": 200},
    {"course": "AIDA 2", "days": 3, "price": 290},
    {"course": "AIDA 3", "days": 4, "price": 340},
    {"course": "AIDA 4", "days": 5, "price": 450},
]
ACCOM_DEDUCT = [
    {"course": "AIDA 1", "discount": 25},
    {"course": "AIDA 2", "discount": 40},
    {"course": "AIDA 3", "discount": 50},
    {"course": "AIDA 4", "discount": 60},
]
CROSSOVER = [
    {"course": "AIDA 2", "discount": 80},
    {"course": "AIDA 3", "discount": 100},
    {"course": "AIDA 4", "discount": 110},
]

LANGS = ["en", "ar", "ru", "it", "fr", "de", "zh", "es"]
FILENAME = {"en": "index.html", "ar": "ar.html", "ru": "ru.html", "it": "it.html",
            "fr": "fr.html", "de": "de.html", "zh": "zh.html", "es": "es.html"}
HREFLANG = {"en": "en", "ar": "ar", "ru": "ru", "it": "it", "fr": "fr", "de": "de", "zh": "zh-Hans", "es": "es"}

# ----------------- تحديثات الـ SEO (الكلمات المفتاحية) -----------------
T = {
 "en": dict(label="English", dir="ltr",
   nav_home="Home", nav_courses="Courses", nav_includes="What's Included", nav_crossover="Crossover",
   nav_videos="Videos", nav_safari="Safari", nav_contact="Contact",
   page_title="MAKANAK | Freediving Courses",
   meta_desc="Discover MAKANAK in Dahab: Cafe, restaurant, and professional freediving courses. Safari trips, Blue Hole, snorkeling, and Red Sea activities.",
   meta_keywords="Blue Hole, Dahab, Safari, Trips, Red Sea, Travel, Egypt, Sea, Diving, Freediving, Snorkeling, Cafe, Restaurant, Makanak, Abu Galum, Blue Lagoon, Twaylat Mountain, Sharm El Sheikh, Boat trips, Yacht, Dahab protectorates, Dahab restaurants, Dahab outings, Dahab nightlife, Dahab activities",
   why_title="Why Choose Our Courses?", why_items=["Professional instruction", "Small groups", "Safety training", "Equipment included", "Photos/videos", "AIDA certification"],
   courses_title="Courses & Pricing", th_course="Course", th_days="Days", th_price="Price", th_discount="Discount",
   includes_title="What the Course Includes", practical_title="Practical Training", practical_accommodation="Accommodation included",
   practical_items=["5 Open Water Sessions", "2 Pool Sessions", "Training in three different equalization techniques", "Breathing techniques for freediving", "Efficient and comfortable diving methods to reduce physical stress and increase performance", "Safety procedures in open water", "Rescue techniques from depth to the surface"],
   theory_title="Theory Lessons", theory_desc="Comprehensive theory classes covering the essential aspects of freediving, including:", theory_items=["Physiology", "Physics", "Nutrition", "Freediving safety and best practices"],
   additional_title="Additional Benefits", additional_items=["Full use of all freediving equipment", "Underwater photos and videos during the course"],
   excluded_title="Excluded Fees", excluded_intro="The following fees are not included in the course price:", excluded_items=["AIDA Certification Fee: €20 (paid upon successful course completion)", "Blue Hole National Park Entrance Fee: $30"],
   accommodation_note_title="Course without accommodation deduct as follows:", crossover_title="Crossover Programs", crossover_desc="For certified freedivers wishing to transfer from another recognized organization to AIDA at the same certification level, we offer a crossover program with a shorter course duration and reduced pricing.", crossover_discount_title="Crossover Discounts",
   closing_line="Start your freediving journey in Dahab and discover the underwater world with confidence and safety.", shorts_title="FREE DIVING", shorts_empty="Shorts coming soon.",
   safari_title="Safari & Trips", safari_empty="Pictures coming soon.", videos_title="Videos", videos_desc="Training.", videos_empty="Videos coming soon.",
   contact_title="Contact Us", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="en_US"),

 "ar": dict(label="العربية", dir="rtl",
   nav_home="الرئيسية", nav_courses="الكورسات", nav_includes="ما يشمله الكورس", nav_crossover="التحويل",
   nav_videos="فيديوهات", nav_safari="سفاري", nav_contact="اتصل بنا",
   page_title="مكانك | كورسات الغطس الحر",
   meta_desc="اكتشف مكانك في دهب: كافيه، مطعم، وكورسات غطس حر احترافية. رحلات سفاري، بلوهول، سنوركلينج، وأفضل الأنشطة في البحر الأحمر.",
   meta_keywords="بلوهول, دهب, سفاري, رحلات, البحر الاحمر, السفر, مصر, البحر, الغوص, الغوص الحر, سنوركلينج, كافيه, مطعم, مكانك, محميه ابو جالوم, بلو لاجون, جبل الطويلات, شرم الشيخ, رحلات بحريه, يخت, محميات دهب, مطاعم دهب, خروجات دهب, السهر في دهب, الانشطه في دهب",
   why_title="لماذا تختار كورساتنا؟", why_items=["تدريب احترافي", "مجموعات صغيرة", "تدريب أمان", "المعدات متضمنة", "صور/فيديو", "شهادة AIDA"],
   courses_title="الأسعار", th_course="الكورس", th_days="الأيام", th_price="السعر", th_discount="الخصم",
   includes_title="ما يشمله الكورس", practical_title="التدريب العملي", practical_accommodation="الإقامة متضمنة",
   practical_items=["5 جلسات مياه مفتوحة", "جلستان في المسبح", "التدريب على ثلاث تقنيات مختلفة لموازنة الضغط", "تقنيات التنفس للغطس الحر", "أساليب غطس فعّالة ومريحة لتقليل الإجهاد الجسدي وزيادة الأداء", "إجراءات الأمان في المياه المفتوحة", "تقنيات الإنقاذ من العمق إلى السطح"],
   theory_title="الدروس النظرية", theory_desc="محاضرات نظرية شاملة تغطي أهم جوانب الغطس الحر، تشمل:", theory_items=["علم وظائف الأعضاء", "الفيزياء", "التغذية", "أمان الغطس الحر وأفضل الممارسات"],
   additional_title="مزايا إضافية", additional_items=["استخدام كامل لجميع معدات الغطس الحر", "صور وفيديوهات تحت الماء أثناء الكورس"],
   excluded_title="رسوم غير متضمنة", excluded_intro="الرسوم التالية غير متضمنة في سعر الكورس:", excluded_items=["رسوم شهادة AIDA: 20 يورو (تُدفع عند إتمام الكورس بنجاح)", "رسوم دخول محمية البلوهول: 30 دولار"],
   accommodation_note_title="الكورس بدون إقامة يُخصم كالتالي:", crossover_title="برنامج التحويل", crossover_desc="للغطاسين الحاصلين على شهادات من منظمات معتمدة أخرى ويرغبون في التحويل إلى AIDA بنفس المستوى، نقدم برنامج تحويل بمدة أقصر وسعر مخفض.", crossover_discount_title="خصومات التحويل",
   closing_line="ابدأ رحلتك في الغطس الحر بدهب واكتشف عالم ما تحت الماء بثقة وأمان.", shorts_title="الغطس الحر (فيديوهات قصيرة)", shorts_empty="قريباً.",
   safari_title="رحلات وسفاري", safari_empty="قريباً.", videos_title="فيديوهات", videos_desc="تدريبات.", videos_empty="قريباً.",
   contact_title="تواصل معنا", contact_cta="واتساب", contact_email_label="البريد", contact_whatsapp_label="واتساب",
   footer_text="مكانك.", og_locale="ar_EG"),

 "ru": dict(label="Русский", dir="ltr",
   nav_home="Главная", nav_courses="Курсы", nav_includes="Включено", nav_crossover="Кроссовер",
   nav_videos="Видео", nav_safari="Сафари", nav_contact="Контакты",
   page_title="MAKANAK | Фридайвинг", meta_desc="Фридайвинг в Дахабе.", meta_keywords="фридайвинг Дахаб",
   why_title="Почему мы?", why_items=["Профи обучение", "Малые группы", "Безопасность", "Снаряжение", "Фото/видео", "Сертификат AIDA"],
   courses_title="Цены", th_course="Курс", th_days="Дни", th_price="Цена", th_discount="Скидка",
   includes_title="Включено", practical_title="Практика", practical_accommodation="Проживание",
   practical_items=["5 открытая вода", "2 бассейн", "Компенсация", "Дыхание", "Методы", "Безопасность", "Спасение"],
   theory_title="Теория", theory_desc="Включает:", theory_items=["Физиология", "Физика", "Питание", "Безопасность"],
   additional_title="Преимущества", additional_items=["Снаряжение", "Фото/видео"],
   excluded_title="Не включено", excluded_intro="Исключено:", excluded_items=["AIDA: €20", "Блю Хол: $30"],
   accommodation_note_title="Без проживания", crossover_title="Кроссовер", crossover_desc="Переход в AIDA.", crossover_discount_title="Скидки",
   closing_line="Начни сейчас.", shorts_title="ФРИДАЙВИНГ (Shorts)", shorts_empty="Скоро.",
   safari_title="Сафари", safari_empty="Скоро.", videos_title="Видео", videos_desc="Тренировки.", videos_empty="Скоро.",
   contact_title="Свяжитесь с нами", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="ru_RU"),

 "it": dict(label="Italiano", dir="ltr",
   nav_home="Home", nav_courses="Corsi", nav_includes="Incluso", nav_crossover="Crossover",
   nav_videos="Video", nav_safari="Safari", nav_contact="Contatti",
   page_title="MAKANAK | Apnea", meta_desc="Apnea a Dahab.", meta_keywords="apnea Dahab",
   why_title="Perché noi?", why_items=["Istruzione pro", "Piccoli gruppi", "Sicurezza", "Attrezzatura", "Foto/video", "AIDA"],
   courses_title="Prezzi", th_course="Corso", th_days="Giorni", th_price="Prezzo", th_discount="Sconto",
   includes_title="Incluso", practical_title="Pratica", practical_accommodation="Alloggio",
   practical_items=["5 mare", "2 piscina", "Compensazione", "Respirazione", "Tecnica", "Sicurezza", "Soccorso"],
   theory_title="Teoria", theory_desc="Include:", theory_items=["Fisiologia", "Fisica", "Nutrizione", "Sicurezza"],
   additional_title="Vantaggi", additional_items=["Attrezzatura", "Foto/video"],
   excluded_title="Escluso", excluded_intro="Escluso:", excluded_items=["AIDA: €20", "Blue Hole: $30"],
   accommodation_note_title="Senza alloggio", crossover_title="Crossover", crossover_desc="Passaggio AIDA.", crossover_discount_title="Sconti",
   closing_line="Inizia ora.", shorts_title="FREE DIVING", shorts_empty="In arrivo.",
   safari_title="Safari", safari_empty="In arrivo.", videos_title="Video", videos_desc="Allenamento.", videos_empty="In arrivo.",
   contact_title="Contattaci", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="it_IT"),

 "fr": dict(label="Français", dir="ltr",
   nav_home="Accueil", nav_courses="Cours", nav_includes="Inclus", nav_crossover="Crossover",
   nav_videos="Vidéos", nav_safari="Safari", nav_contact="Contact",
   page_title="MAKANAK | Apnée", meta_desc="Apnée à Dahab.", meta_keywords="apnée Dahab",
   why_title="Pourquoi nous ?", why_items=["Pro", "Petits groupes", "Sécurité", "Équipement", "Photos/vidéos", "AIDA"],
   courses_title="Tarifs", th_course="Cours", th_days="Jours", th_price="Prix", th_discount="Réduction",
   includes_title="Inclus", practical_title="Pratique", practical_accommodation="Hébergement",
   practical_items=["5 mer", "2 piscina", "Compensation", "Respiration", "Technique", "Sécurité", "Sauvetage"],
   theory_title="Théorie", theory_desc="Inclus:", theory_items=["Physiologie", "Physique", "Nutrition", "Sécurité"],
   additional_title="Avantages", additional_items=["Équipement", "Photos/vidéos"],
   excluded_title="Exclus", excluded_intro="Exclus:", excluded_items=["AIDA: 20€", "Blue Hole: 30$"],
   accommodation_note_title="Sans hébergement", crossover_title="Crossover", crossover_desc="Passage AIDA.", crossover_discount_title="Réductions",
   closing_line="Commencez.", shorts_title="FREE DIVING", shorts_empty="À venir.",
   safari_title="Safari", safari_empty="À venir.", videos_title="Vidéos", videos_desc="Entrainement.", videos_empty="À venir.",
   contact_title="Contact", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="fr_FR"),

 "de": dict(label="Deutsch", dir="ltr",
   nav_home="Start", nav_courses="Kurse", nav_includes="Inklusive", nav_crossover="Crossover",
   nav_videos="Videos", nav_safari="Safari", nav_contact="Kontakt",
   page_title="MAKANAK | Apnoetauchen", meta_desc="Apnoetauchen in Dahab.", meta_keywords="Apnoetauchen Dahab",
   why_title="Warum wir?", why_items=["Profi", "Kleine Gruppen", "Sicherheit", "Ausrüstung", "Fotos/Videos", "AIDA"],
   courses_title="Preise", th_course="Kurs", th_days="Tage", th_price="Preis", th_discount="Rabatt",
   includes_title="Inklusive", practical_title="Praxis", practical_accommodation="Unterkunft",
   practical_items=["5 Freiwasser", "2 Pool", "Druckausgleich", "Atmung", "Technik", "Sicherheit", "Rettung"],
   theory_title="Theorie", theory_desc="Inhalt:", theory_items=["Physiologie", "Physik", "Ernährung", "Sicherheit"],
   additional_title="Vorteile", additional_items=["Ausrüstung", "Fotos/Videos"],
   excluded_title="Exklusiv", excluded_intro="Nicht enthalten:", excluded_items=["AIDA: 20€", "Blue Hole: 30$"],
   accommodation_note_title="Ohne Unterkunft", crossover_title="Crossover", crossover_desc="Wechsel zu AIDA.", crossover_discount_title="Rabatte",
   closing_line="Starte jetzt.", shorts_title="FREE DIVING", shorts_empty="Bald.",
   safari_title="Safari", safari_empty="Bald.", videos_title="Videos", videos_desc="Training.", videos_empty="Bald.",
   contact_title="Kontakt", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="de_DE"),

 "zh": dict(label="中文", dir="ltr",
   nav_home="首页", nav_courses="课程", nav_includes="包含", nav_crossover="转换",
   nav_videos="视频", nav_safari="游猎", nav_contact="联系",
   page_title="MAKANAK | 自由潜水", meta_desc="达哈布自由潜水.", meta_keywords="达哈布自由潜水",
   why_title="为什么选我们?", why_items=["专业", "小班", "安全", "装备", "照片/视频", "AIDA"],
   courses_title="价格", th_course="课程", th_days="天", th_price="价格", th_discount="折扣",
   includes_title="包含", practical_title="实践", practical_accommodation="含住宿",
   practical_items=["5次海潜", "2次泳池", "耳压", "呼吸", "技巧", "安全", "救援"],
   theory_title="理论", theory_desc="包括:", theory_items=["生理", "物理", "营养", "安全"],
   additional_title="福利", additional_items=["装备", "照片/视频"],
   excluded_title="不含", excluded_intro="不含:", excluded_items=["AIDA: €20", "蓝洞: $30"],
   accommodation_note_title="不含住宿", crossover_title="转换", crossover_desc="转至AIDA.", crossover_discount_title="折扣",
   closing_line="开始吧.", shorts_title="自由潜水", shorts_empty="即将推出.",
   safari_title="游猎", safari_empty="即将推出.", videos_title="视频", videos_desc="训练.", videos_empty="即将推出.",
   contact_title="联系", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="zh_CN"),

 "es": dict(label="Español", dir="ltr",
   nav_home="Inicio", nav_courses="Cursos", nav_includes="Incluido", nav_crossover="Crossover",
   nav_videos="Vídeos", nav_safari="Safari", nav_contact="Contacto",
   page_title="MAKANAK | Apnea", meta_desc="Apnea en Dahab.", meta_keywords="apnea Dahab",
   why_title="¿Por qué nosotros?", why_items=["Pro", "Grupos pequeños", "Seguridad", "Equipo", "Fotos/vídeos", "AIDA"],
   courses_title="Precios", th_course="Curso", th_days="Días", th_price="Precio", th_discount="Descuento",
   includes_title="Incluido", practical_title="Práctica", practical_accommodation="Alojamiento",
   practical_items=["5 mar", "2 piscina", "Compensación", "Respiración", "Técnica", "Seguridad", "Rescate"],
   theory_title="Teoría", theory_desc="Incluye:", theory_items=["Fisiología", "Física", "Nutrición", "Seguridad"],
   additional_title="Beneficios", additional_items=["Equipo", "Fotos/vídeos"],
   excluded_title="Excluido", excluded_intro="Excluido:", excluded_items=["AIDA: 20€", "Blue Hole: 30$"],
   accommodation_note_title="Sin alojamiento", crossover_title="Crossover", crossover_desc="Paso a AIDA.", crossover_discount_title="Descuentos",
   closing_line="Empieza ya.", shorts_title="FREE DIVING", shorts_empty="Pronto.",
   safari_title="Safari", safari_empty="Pronto.", videos_title="Vídeos", videos_desc="Entrenamiento.", videos_empty="Pronto.",
   contact_title="Contacto", contact_cta="WhatsApp", contact_email_label="Email", contact_whatsapp_label="WhatsApp",
   footer_text="MAKANAK.", og_locale="es_ES"),
}

def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def price_table(headers, rows):
    thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="price-table"><thead><tr>{thead}</tr></thead><tbody>{trs}</tbody></table>'

def bullet_list(items):
    return '<ul class="bullets">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"

def why_cards(items):
    cards = "".join(f'<div class="why-card"><span class="check">✓</span><p>{esc(i)}</p></div>' for i in items)
    return f'<div class="why-grid">{cards}</div>'

def hreflang_tags(current):
    tags = [f'<link rel="alternate" hreflang="{HREFLANG[lg]}" href="{SITE_URL}/{FILENAME[lg]}">' for lg in LANGS]
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/index.html">')
    return "".join(tags)

def lang_switcher(current):
    opts = []
    for lg in LANGS:
        active_class = ' class="active"' if lg == current else ''
        opts.append('<a href="' + FILENAME[lg] + '"' + active_class + ' hreflang="' + HREFLANG[lg] + '">' + T[lg]["label"] + '</a>')

    opts_str = "".join(opts)
    btn = '<button class="lang-toggle" aria-label="Language" onclick="document.getElementById(' + "'langMenu'" + ').classList.toggle(' + "'open'" + ')">🌐 ' + T[current]["label"] + '</button>'
    return '<div class="lang-switcher">' + btn + '<div class="lang-menu" id="langMenu">' + opts_str + '</div></div>'

def nav_links(t):
    return f'<a href="#courses">{esc(t["nav_courses"])}</a><a href="#includes">{esc(t["nav_includes"])}</a><a href="#crossover">{esc(t["nav_crossover"])}</a><a href="#shorts">{esc(t["shorts_title"])}</a><a href="#safari">{esc(t["nav_safari"])}</a><a href="#contact">{esc(t["nav_contact"])}</a>'

def shorts_gallery(t):
    if not LOCAL_SHORTS: return f'<p class="videos-empty">{esc(t["shorts_empty"])}</p>'
    cards = []
    for vid in LOCAL_SHORTS:
        cards.append(f'<div class="short-card"><video src="images/{vid}" preload="metadata" controls playsinline></video></div>')
    return f'<div class="shorts-grid">{"".join(cards)}</div>'

def safari_gallery(t):
    if not SAFARI_IMAGES: return f'<p class="videos-empty">{esc(t["safari_empty"])}</p>'
    cards = [f'<div class="safari-card"><img src="images/{img}" alt="Safari"></div>' for img in SAFARI_IMAGES]
    return f'<div class="safari-grid">{"".join(cards)}</div>'

def generate_hero_slides(lang):
    html = ""
    for i, slide in enumerate(HERO_SLIDES):
        active_class = " active" if i == 0 else ""
        img = slide["image"]
        txt = esc(slide["text"].get(lang, slide["text"]["en"]))
        bg_style = "background-image: url('images/" + img + "');"
        html += '<div class="slide slide-' + str(i+1) + active_class + '" style="' + bg_style + '">'
        html += '<div class="slide-text"><h1>' + txt + '</h1></div></div>'
    return html

def build_page(lang):
    t = T[lang]
    courses_rows = [[c["course"], c["days"], str(c["price"])] for c in COURSES]
    accom_rows = [[c["course"], str(c["discount"])] for c in ACCOM_DEDUCT]
    cross_rows = [[c["course"], str(c["discount"])] for c in CROSSOVER]

    btn_mobile = '<button class="mobile-toggle" aria-label="Menu" onclick="document.getElementById(' + "'mobileNav'" + ').classList.toggle(' + "'open'" + ')">☰</button>'

    # ترجمة اللوجو: إذا كانت اللغة عربي، سيظهر "مكانك"، وفي باقي اللغات يظهر "MAKANAK"
    logo_main = "مكانك" if lang == "ar" else "MAKANAK"
    logo_sub = "بلوهول دهب - كافيه وغطس حر" if lang == "ar" else "Blue hole Dahab - Cafeteria & Free Dive"

    html = f"""<!DOCTYPE html>
<html lang="{HREFLANG[lang]}" dir="{t["dir"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(t["page_title"])}</title>
<meta name="description" content="{esc(t["meta_desc"])}">
<meta name="keywords" content="{esc(t["meta_keywords"])}">
<link rel="canonical" href="{SITE_URL}/{FILENAME[lang]}">
{hreflang_tags(lang)}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="logo">
      <img src="images/logo-icon.png" alt="Logo" class="logo-icon">
      <div class="logo-text">
        <span class="logo-main">{logo_main}</span>
        <span class="logo-sub">{logo_sub}</span>
      </div>
    </a>
    <nav class="main-nav">{nav_links(t)}</nav>
    {lang_switcher(lang)}
    {btn_mobile}
  </div>
  <nav class="mobile-nav" id="mobileNav">{nav_links(t)}</nav>
</header>

<main>
  <section class="hero" id="home">
    <div class="social-hero">
      <a href="{FACEBOOK_LINK}" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
      <a href="{TIKTOK_LINK}" target="_blank" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
      <a href="{LOCATION_LINK}" target="_blank" aria-label="Location"><i class="fas fa-map-marker-alt"></i></a>
      <a href="{GOOGLE_LINK}" target="_blank" aria-label="Google"><i class="fab fa-google"></i></a>
      <a href="mailto:{EMAIL}" aria-label="Email"><i class="fas fa-envelope"></i></a>
      <a href="{WHATSAPP_LINK}" target="_blank" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
    </div>

    <div class="hero-slideshow">
      {generate_hero_slides(lang)}
    </div>
  </section>

  <section class="section" id="shorts">
    <h2>{esc(t["shorts_title"])}</h2>
    {shorts_gallery(t)}
  </section>

  <section class="section alt" id="why">
    <h2>{esc(t["why_title"])}</h2>
    <div class="why-container">
       <div class="why-content">
          {why_cards(t["why_items"])}
       </div>
       <div class="why-image-wrapper">
          <img src="images/why-divers.png" alt="Diving Professionals">
       </div>
    </div>
  </section>

  <section class="section" id="courses">
    <h2>{esc(t["courses_title"])}</h2>
    {price_table([t["th_course"], t["th_days"], t["th_price"]], courses_rows)}
    <p class="note-box">(AIDA 1: 1night, AIDA 2: 2nights, AIDA 3: 3nights, AIDA 4: 4nights)</p>
  </section>

  <section class="section alt" id="includes">
    <h2>{esc(t["includes_title"])}</h2>

    <h3>🏊 {esc(t["practical_title"])}</h3>
    {bullet_list(t["practical_items"])}

    <h3>📖 {esc(t["theory_title"])}</h3>
    <p>{esc(t["theory_desc"])}</p>
    {bullet_list(t["theory_items"])}

    <h3>🎁 {esc(t["additional_title"])}</h3>
    {bullet_list(t["additional_items"])}

    <div class="excluded-box">
      <h3>{esc(t["excluded_title"])}</h3>
      <p>{esc(t["excluded_intro"])}</p>
      {bullet_list(t["excluded_items"])}
    </div>

    <h3>{esc(t["accommodation_note_title"])}</h3>
    {price_table([t["th_course"], t["th_discount"]], accom_rows)}
  </section>

  <section class="section" id="safari">
    <h2>{esc(t["safari_title"])}</h2>
    {safari_gallery(t)}
  </section>

  <section class="section alt" id="crossover">
    <h2>{esc(t["crossover_title"])}</h2>
    <p class="center-text">{esc(t["crossover_desc"])}</p>
    {price_table([t["th_course"], t["th_discount"]], cross_rows)}
    <p class="closing-line">{esc(t["closing_line"])}</p>
  </section>

  <section class="section contact" id="contact">
    <h2>{esc(t["contact_title"])}</h2>
    <div class="contact-grid">
      <a class="contact-chip" href="mailto:{EMAIL}">
        <span class="chip-label">{esc(t["contact_email_label"])}</span>
        <span class="chip-value">{EMAIL}</span>
      </a>
      <a class="contact-chip" href="{WHATSAPP_LINK}" target="_blank">
        <span class="chip-label">{esc(t["contact_whatsapp_label"])}</span>
        <span class="chip-value">{WHATSAPP}</span>
      </a>
    </div>
    <a class="btn-cta" href="{WHATSAPP_LINK}" target="_blank">{esc(t["contact_cta"])}</a>
  </section>
</main>

<footer class="site-footer">
  <p>{esc(t["footer_text"])}</p>
  <p class="copyright">© <span id="year"></span> {logo_main}</p>
</footer>

<audio id="bgMusic" src="images/bg-music.mp3" loop preload="auto"></audio>

<script src="js/script.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {{
      var audio = document.getElementById("bgMusic");
      if(audio) {{
          audio.volume = 0.15; // الصوت منخفض بنسبة 15%
          var playPromise = audio.play();
          if (playPromise !== undefined) {{
              playPromise.catch(function(error) {{
                  // إذا المتصفح منع التشغيل التلقائي، تشتغل بمجرد ضغطة الزائر
                  var startAudio = function() {{
                      audio.play();
                      document.removeEventListener('click', startAudio);
                      document.removeEventListener('scroll', startAudio);
                      document.removeEventListener('touchstart', startAudio);
                  }};
                  document.addEventListener('click', startAudio);
                  document.addEventListener('scroll', startAudio);
                  document.addEventListener('touchstart', startAudio);
              }});
          }}
      }}
  }});
</script>

</body>
</html>
"""
    return html

os.makedirs(os.path.join(OUT, "images"), exist_ok=True)
os.makedirs(os.path.join(OUT, "css"), exist_ok=True)
os.makedirs(os.path.join(OUT, "js"), exist_ok=True)

for lg in LANGS:
    path = os.path.join(OUT, FILENAME[lg])
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_page(lg))
    print("تم تحديث الصفحة:", path)