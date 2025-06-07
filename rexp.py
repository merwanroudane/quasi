import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from PIL import Image
import io
import base64

# تعيين الاتجاه للعربية
st.markdown("""
<style>
    html, body, [class*="css"] {
        direction: rtl;
        text-align: right;
    }
    h1, h2, h3, h4, h5, h6 {
        text-align: right;
    }
    .stButton button {
        float: right;
    }
    .st-bx {
        float: right;
    }
</style>
""", unsafe_allow_html=True)

# الألوان المستخدمة
primary_color = "#8884FF"
secondary_color = "#4CAF50"
accent_color = "#FF5722"
info_color = "#2196F3"
warning_color = "#FFC107"

# CSS للعناصر المهمة
st.markdown("""
<style>
    .highlight-box {
        background-color: #f6f6f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0px;
        border-right: 5px solid """ + primary_color + """;
    }
    .important-concept {
        color: """ + accent_color + """;
        font-weight: bold;
    }
    .definition {
        color: """ + primary_color + """;
        font-weight: bold;
        font-size: 1.1em;
    }
    .warning {
        color: """ + warning_color + """;
        font-weight: bold;
    }
    .info {
        color: """ + info_color + """;
    }
    .success {
        color: """ + secondary_color + """;
        font-weight: bold;
    }
    .section-header {
        background-color: """ + primary_color + """;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin: 20px 0px 10px 0px;
    }
    .subsection-header {
        background-color: #e0e0ff;
        color: #333;
        padding: 8px;
        border-radius: 5px;
        margin: 15px 0px 10px 0px;
    }
</style>
""", unsafe_allow_html=True)

# عنوان التطبيق
st.title("المنهج التجريبي وشبه التجريبي في القياس الاقتصادي")
st.markdown('<p class="success">دليل شامل للمبتدئين</p>', unsafe_allow_html=True)

# القائمة الجانبية
st.sidebar.title("المحتويات")
sections = {
    "مقدمة": "intro",
    "مفهوم المنهج التجريبي": "experimental_concept",
    "البيانات التجريبية والرصدية": "data_types",
    "التجارب العشوائية المحكومة": "rct",
    "المنهج شبه التجريبي": "quasi",
    "طرق التقييم والتحليل": "evaluation",
    "الفرضيات الأساسية": "assumptions",
    "التطبيقات في الاقتصاد": "applications",
    "خطة التعلم الشاملة": "learning_plan",
    "الموارد والمراجع": "resources"
}

selection = st.sidebar.radio("اختر القسم:", list(sections.keys()))
current_section = sections[selection]


# دالة لإنشاء مخطط Mermaid
def create_mermaid_chart(code):
    graphbyte = code.encode("utf8")
    base64_bytes = base64.b64encode(graphbyte)
    base64_string = base64_bytes.decode("ascii")
    return f'<img src="https://mermaid.ink/img/{base64_string}">'


# القسم المختار
if current_section == "intro":
    st.markdown('<div class="section-header"><h2>مقدمة في المنهج التجريبي والقياس الاقتصادي</h2></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    في عالم الاقتصاد والسياسات العامة، يسعى الباحثون دائمًا إلى إيجاد إجابات لأسئلة مهمة:
    <ul>
        <li>هل يؤدي رفع الحد الأدنى للأجور إلى زيادة البطالة؟</li>
        <li>هل تؤدي برامج التدريب المهني إلى زيادة الدخل؟</li>
        <li>ما هو تأثير برنامج دعم معين على مستويات الفقر؟</li>
    </ul>

    للإجابة على هذه الأسئلة، نحتاج إلى <span class="important-concept">تحديد العلاقات السببية</span> وليس مجرد الارتباطات بين المتغيرات.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### لماذا نحتاج إلى المنهج التجريبي؟

    المنهج التجريبي يساعدنا على تجاوز المشكلة الأساسية في تحليل البيانات الاقتصادية: <span class="warning">مشكلة الاندوجينية (الداخلية)</span> أو التحيز في الاختيار.
    """, unsafe_allow_html=True)

    # إنشاء تمثيل بياني للفرق بين الارتباط والسببية
    df = pd.DataFrame({
        'السنة': range(2000, 2020),
        'استهلاك الآيس كريم (طن)': np.random.normal(500, 50, 20) + np.linspace(0, 100, 20),
        'حوادث الغرق': np.random.normal(100, 10, 20) + np.linspace(0, 20, 20)
    })

    fig = px.scatter(df, x='استهلاك الآيس كريم (طن)', y='حوادث الغرق',
                     trendline="ols", title="مثال على الارتباط غير السببي")
    fig.update_layout(
        xaxis_title="استهلاك الآيس كريم (طن)",
        yaxis_title="حوادث الغرق",
        font=dict(size=14)
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class="info">
    <b>ملاحظة:</b> في المثال أعلاه، يوجد ارتباط إيجابي بين استهلاك الآيس كريم وحوادث الغرق، لكن العلاقة ليست سببية. المتغير الثالث (درجة الحرارة في الصيف) هو ما يسبب زيادة كلاهما.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### الفرق بين المناهج البحثية:

    1. <span class="definition">المنهج الوصفي:</span> يصف الظواهر دون تحديد العلاقات السببية
    2. <span class="definition">المنهج الارتباطي:</span> يحدد العلاقات بين المتغيرات دون إثبات السببية
    3. <span class="definition">المنهج التجريبي:</span> يستخدم تجارب منضبطة لتحديد العلاقات السببية
    4. <span class="definition">المنهج شبه التجريبي:</span> يحاول تحديد العلاقات السببية في حالات لا يمكن فيها إجراء تجارب كاملة
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>ما ستتعلمه في هذا الدليل</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    - مفاهيم المنهج التجريبي والفرق بينه وبين المنهج شبه التجريبي
    - أنواع البيانات المستخدمة في الاقتصاد التجريبي
    - تصميم وتنفيذ التجارب العشوائية المحكومة
    - طرق شبه تجريبية للتغلب على مشكلات الاندوجينية
    - الفرضيات الأساسية اللازمة لتحديد العلاقات السببية
    - تطبيقات عملية في مجال الاقتصاد والسياسات العامة
    """, unsafe_allow_html=True)

elif current_section == "experimental_concept":
    st.markdown('<div class="section-header"><h2>مفهوم المنهج التجريبي</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="definition">المنهج التجريبي (Experimental Method):</span> هو منهجية بحثية تستخدم التجارب المصممة بعناية لتحديد العلاقات السببية بين المتغيرات.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### المفاهيم الأساسية

    <span class="important-concept">1. السببية (Causality):</span>
    """, unsafe_allow_html=True)

    st.latex(r"Y_i(1) - Y_i(0) = \text{الأثر السببي}")

    st.markdown("""
    حيث:
    - $Y_i(1)$ = النتيجة عند تطبيق المعالجة
    - $Y_i(0)$ = النتيجة عند عدم تطبيق المعالجة

    <span class="warning">المشكلة الأساسية:</span> لا يمكننا ملاحظة كلاهما لنفس الوحدة في نفس الوقت (المشكلة الأساسية للاستدلال السببي).
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">2. المعالجة (Treatment):</span> المتغير المستقل الذي يتم التلاعب به بشكل متعمد للدراسة.

    <span class="important-concept">3. مجموعة المعالجة (Treatment Group):</span> المجموعة التي تخضع للمعالجة.

    <span class="important-concept">4. مجموعة الضبط/المقارنة (Control Group):</span> المجموعة التي لا تخضع للمعالجة وتستخدم للمقارنة.

    <span class="important-concept">5. التعيين العشوائي (Randomization):</span> توزيع المشاركين عشوائياً بين مجموعات المعالجة والضبط.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الفرق بين الارتباط والسببية</h3></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <span class="definition">الارتباط (Correlation):</span>
        - يشير إلى وجود علاقة إحصائية بين متغيرين
        - لا يخبرنا عن اتجاه العلاقة أو سببها
        - يمكن أن يكون بسبب متغير ثالث غير ملحوظ
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <span class="definition">السببية (Causality):</span>
        - تشير إلى أن تغيير في متغير X يؤدي إلى تغيير في متغير Y
        - تحدد اتجاه العلاقة (من السبب إلى النتيجة)
        - لا تتأثر بالمتغيرات الخارجية (في التجارب المثالية)
        """, unsafe_allow_html=True)

    # مخطط لمشكلة الارتباط والسببية
    mermaid_code = """
    graph LR
        A[المتغير X] -->|ارتباط| B[المتغير Y]
        C[متغير ثالث Z] --> A
        C --> B
        D[المتغير X] -->|سببية| E[المتغير Y]
    """

    st.markdown('<div class="subsection-header"><h3>أنواع التجارب في المنهج التجريبي</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. التجارب المعملية (Laboratory Experiments):</span>
    - تُجرى في بيئة محكومة
    - تسمح بالتحكم الدقيق في المتغيرات
    - <span class="warning">المحدودية:</span> قد تفتقر إلى الواقعية وصعوبة تعميم النتائج

    <span class="definition">2. التجارب الميدانية (Field Experiments):</span>
    - تُجرى في البيئة الطبيعية للظاهرة المدروسة
    - تقدم نتائج أكثر واقعية وقابلية للتعميم
    - <span class="warning">المحدودية:</span> صعوبة التحكم في جميع المتغيرات الخارجية

    <span class="definition">3. التجارب العشوائية المحكومة (Randomized Controlled Trials - RCTs):</span>
    - المعيار الذهبي في البحث التجريبي
    - تعتمد على التعيين العشوائي للمشاركين بين مجموعات المعالجة والضبط
    - <span class="success">المميزات:</span> تقلل من التحيز وتسمح بالاستدلال السببي
    """, unsafe_allow_html=True)

    # رسم بياني لتوضيح مفهوم RCT
    st.markdown('<div class="subsection-header"><h3>مخطط التجربة العشوائية المحكومة (RCT)</h3></div>',
                unsafe_allow_html=True)

    df_rct = pd.DataFrame({
        'المرحلة': ['البداية', 'التعيين العشوائي', 'المعالجة', 'القياس'],
        'مجموعة المعالجة': [100, 50, 'تطبيق المعالجة', 'قياس النتائج Y₁'],
        'مجموعة الضبط': [100, 50, 'لا معالجة', 'قياس النتائج Y₀']
    })

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df_rct.columns),
                    fill_color=primary_color,
                    align='center',
                    font=dict(color='white', size=14)),
        cells=dict(values=[df_rct['المرحلة'], df_rct['مجموعة المعالجة'], df_rct['مجموعة الضبط']],
                   fill_color='lavender',
                   align='center'))
    ])

    fig.update_layout(width=700, height=300)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <div class="info">
    <b>الأثر السببي للمعالجة = </b> متوسط النتائج في مجموعة المعالجة - متوسط النتائج في مجموعة الضبط
    </div>
    """, unsafe_allow_html=True)

    st.latex(r"\text{ATE} = E[Y(1) - Y(0)] = E[Y|T=1] - E[Y|T=0]")

    st.markdown("""
    حيث:
    - ATE = متوسط أثر المعالجة (Average Treatment Effect)
    - T = متغير ثنائي يشير إلى المعالجة (1 = معالجة، 0 = ضبط)
    """, unsafe_allow_html=True)

elif current_section == "data_types":
    st.markdown('<div class="section-header"><h2>البيانات التجريبية والرصدية</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    فهم أنواع البيانات المستخدمة في البحوث الاقتصادية أمر أساسي لاختيار المنهجية المناسبة وتفسير النتائج بشكل صحيح.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>البيانات التجريبية (Experimental Data)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">البيانات التجريبية:</span> هي البيانات التي يتم جمعها من خلال تجارب مصممة، حيث يتم التحكم في المتغيرات المستقلة بشكل متعمد.

    <span class="important-concept">الخصائص الرئيسية:</span>
    1. التحكم في المتغيرات المستقلة (المعالجة)
    2. التعيين العشوائي للمشاركين في مجموعات المعالجة والضبط
    3. إمكانية استنتاج العلاقات السببية

    <span class="success">مميزات البيانات التجريبية:</span>
    - تقليل مشكلة الاندوجينية (Endogeneity)
    - التحكم في المتغيرات الخارجية
    - إمكانية تحديد الأثر السببي بشكل دقيق

    <span class="warning">تحديات البيانات التجريبية:</span>
    - تكلفة عالية للتنفيذ
    - قيود أخلاقية وعملية
    - مشكلة التعميم (External Validity)
    - تأثير هوثورن (Hawthorne Effect) - تغير سلوك المشاركين لمجرد علمهم بأنهم تحت المراقبة
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>البيانات الرصدية (Observational Data)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">البيانات الرصدية:</span> هي البيانات التي يتم جمعها من خلال ملاحظة الظواهر في بيئتها الطبيعية دون تدخل متعمد من الباحث.

    <span class="important-concept">الخصائص الرئيسية:</span>
    1. عدم التحكم في المتغيرات المستقلة
    2. عدم وجود تعيين عشوائي
    3. صعوبة استنتاج العلاقات السببية

    <span class="success">مميزات البيانات الرصدية:</span>
    - توفر بيانات عن ظواهر يصعب دراستها تجريبياً
    - عينات أكبر وأكثر تمثيلاً للمجتمع
    - تكلفة أقل في الجمع والتحليل
    - إمكانية دراسة التغيرات على المدى الطويل

    <span class="warning">تحديات البيانات الرصدية:</span>
    - مشكلة الاندوجينية والمتغيرات المحذوفة
    - التحيز في الاختيار (Selection Bias)
    - صعوبة عزل تأثير متغير معين
    """, unsafe_allow_html=True)

    # جدول مقارنة بين البيانات التجريبية والرصدية
    comparison_data = pd.DataFrame({
        'معيار المقارنة': ['التحكم بالمتغيرات', 'التعيين العشوائي', 'استنتاج السببية', 'حجم العينة', 'التكلفة',
                           'التمثيل الواقعي'],
        'البيانات التجريبية': ['عالي', 'نعم', 'ممكن بدرجة عالية', 'محدود غالباً', 'مرتفعة', 'محدود أحياناً'],
        'البيانات الرصدية': ['منخفض/معدوم', 'لا', 'صعب (يحتاج لطرق خاصة)', 'كبير غالباً', 'منخفضة', 'عالي']
    })

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(comparison_data.columns),
                    fill_color=primary_color,
                    align='center',
                    font=dict(color='white', size=14)),
        cells=dict(values=[comparison_data['معيار المقارنة'],
                           comparison_data['البيانات التجريبية'],
                           comparison_data['البيانات الرصدية']],
                   fill_color='lavender',
                   align='center'))
    ])

    fig.update_layout(width=700, height=300)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="subsection-header"><h3>أنواع البيانات من حيث البنية</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. البيانات المقطعية (Cross-sectional Data):</span>
    - بيانات لعدة وحدات (أفراد، شركات، دول) في نقطة زمنية واحدة
    - <span class="info">مثال:</span> مسح للدخل والإنفاق لعينة من الأسر في سنة 2023

    <span class="definition">2. بيانات السلاسل الزمنية (Time Series Data):</span>
    - بيانات لوحدة واحدة عبر فترات زمنية متعددة
    - <span class="info">مثال:</span> معدل البطالة في مصر من 2000 إلى 2023

    <span class="definition">3. بيانات البانل (Panel Data):</span>
    - بيانات لعدة وحدات عبر فترات زمنية متعددة
    - <span class="info">مثال:</span> نمو الناتج المحلي الإجمالي لـ 20 دولة على مدى 15 سنة
    - تسمح بالتحكم في الخصائص غير الملحوظة الثابتة مع الزمن (Fixed Effects)
    """, unsafe_allow_html=True)

    # رسم توضيحي لأنواع البيانات
    data_structures = {
        'النوع': ['بيانات مقطعية', 'سلاسل زمنية', 'بيانات بانل'],
        'البعد الأول': ['وحدات متعددة', 'وحدة واحدة', 'وحدات متعددة'],
        'البعد الثاني': ['زمن واحد', 'أزمنة متعددة', 'أزمنة متعددة'],
        'الشكل التمثيلي': ['جدول أفقي', 'جدول رأسي', 'مصفوفة ثلاثية الأبعاد']
    }

    df_structure = pd.DataFrame(data_structures)

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df_structure.columns),
                    fill_color=primary_color,
                    align='center',
                    font=dict(color='white', size=14)),
        cells=dict(values=[df_structure[col] for col in df_structure.columns],
                   fill_color='lavender',
                   align='center'))
    ])

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="subsection-header"><h3>تحويل البيانات الرصدية إلى شبه تجريبية</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    عند عدم إمكانية إجراء تجارب حقيقية، يمكن استخدام طرق إحصائية متقدمة لمحاكاة الظروف التجريبية باستخدام البيانات الرصدية:

    1. <span class="important-concept">طريقة المتغيرات الأداتية (Instrumental Variables)</span>
    2. <span class="important-concept">طريقة الانحدار المتقطع (Regression Discontinuity Design)</span>
    3. <span class="important-concept">طريقة الفروق في الفروق (Difference-in-Differences)</span>
    4. <span class="important-concept">طريقة المطابقة (Matching Methods)</span>

    سنتناول هذه الطرق بالتفصيل في قسم المنهج شبه التجريبي.
    """, unsafe_allow_html=True)

elif current_section == "rct":
    st.markdown('<div class="section-header"><h2>التجارب العشوائية المحكومة (RCTs)</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="definition">التجارب العشوائية المحكومة (Randomized Controlled Trials):</span> هي النموذج الذهبي للبحث التجريبي، حيث يتم تعيين المشاركين عشوائياً إلى مجموعات مختلفة (معالجة وضبط) لقياس أثر تدخل معين.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المبادئ الأساسية للـ RCTs</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">1. التعيين العشوائي (Randomization):</span>

    التعيين العشوائي هو حجر الأساس في التجارب العشوائية المحكومة، ويضمن:
    - توزيع متوازن للخصائص الملحوظة وغير الملحوظة بين المجموعات
    - تقليل التحيز في الاختيار (Selection Bias)
    - إمكانية استنتاج العلاقة السببية
    """, unsafe_allow_html=True)

    st.latex(r"\text{توازن الخصائص:} \quad E[X_i|T_i=1] = E[X_i|T_i=0]")

    st.markdown("""
    <span class="important-concept">2. مجموعة الضبط (Control Group):</span>

    مجموعة المقارنة التي لا تتلقى المعالجة، وتوفر:
    - خط الأساس للمقارنة (Counterfactual)
    - تقدير لما كان سيحدث لمجموعة المعالجة لو لم تتلق المعالجة

    <span class="important-concept">3. المعالجة (Treatment):</span>

    التدخل أو البرنامج الذي نريد قياس تأثيره، ويجب أن يكون:
    - محدداً بوضوح
    - قابلاً للتطبيق بشكل موحد
    - معزولاً عن التأثيرات الأخرى
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>خطوات تصميم وتنفيذ التجارب العشوائية المحكومة</h3></div>',
                unsafe_allow_html=True)

    steps = [
        "تحديد السؤال البحثي والفرضيات",
        "تصميم المعالجة والتدخل",
        "تحديد حجم العينة المطلوب",
        "اختيار العينة وآلية التعيين العشوائي",
        "جمع البيانات الأولية (Baseline Data)",
        "تطبيق المعالجة",
        "جمع بيانات النتائج",
        "تحليل البيانات وتقدير الأثر",
        "تفسير النتائج ونشرها"
    ]

    # رسم مخطط خطوات RCT
    phases = ['التخطيط', 'التصميم', 'التنفيذ', 'التحليل']
    steps_per_phase = [[steps[0], steps[1]], [steps[2], steps[3], steps[4]], [steps[5], steps[6]], [steps[7], steps[8]]]

    fig = go.Figure()

    colors = [primary_color, secondary_color, accent_color, info_color]

    for i, phase in enumerate(phases):
        for step in steps_per_phase[i]:
            fig.add_trace(go.Bar(
                x=[step],
                y=[1],
                name=phase,
                marker_color=colors[i],
                text=step,
                textposition='inside',
                orientation='v',
                showlegend=i == 0 or phase != phases[i - 1]
            ))

    fig.update_layout(
        title="مراحل تنفيذ التجربة العشوائية المحكومة",
        xaxis=dict(title="الخطوات"),
        yaxis=dict(showticklabels=False),
        barmode='stack',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="subsection-header"><h3>طرق التعيين العشوائي</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. التعيين العشوائي البسيط (Simple Randomization):</span>
    - كل وحدة لها فرصة متساوية للتعيين في أي مجموعة
    - مناسب للعينات الكبيرة
    - <span class="warning">المحدودية:</span> قد لا يضمن التوازن في العينات الصغيرة

    <span class="definition">2. التعيين العشوائي الطبقي (Stratified Randomization):</span>
    - تقسيم العينة إلى طبقات متجانسة ثم إجراء التعيين العشوائي داخل كل طبقة
    - يضمن توازن الخصائص المهمة بين المجموعات
    - <span class="info">مثال:</span> التقسيم حسب الجنس، العمر، الدخل قبل التعيين العشوائي

    <span class="definition">3. التعيين العشوائي المجموعي (Cluster Randomization):</span>
    - تعيين مجموعات كاملة (مدارس، قرى، مناطق) بدلاً من الأفراد
    - يستخدم عندما تكون المعالجة على مستوى المجموعة أو لتجنب انتشار المعالجة
    - <span class="warning">المحدودية:</span> يتطلب حجم عينة أكبر ويقلل القوة الإحصائية
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>تقدير الأثر في التجارب العشوائية</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">متوسط الأثر العام للمعالجة (Average Treatment Effect - ATE):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{ATE} = E[Y_i(1) - Y_i(0)]")

    st.markdown("""
    في التجارب العشوائية المحكومة، يمكن تقدير ATE ببساطة من خلال:
    """, unsafe_allow_html=True)

    st.latex(r"\hat{\text{ATE}} = \bar{Y}_{\text{treatment}} - \bar{Y}_{\text{control}}")

    st.markdown("""
    <span class="important-concept">متوسط الأثر على المعالجين (Average Treatment Effect on the Treated - ATT):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{ATT} = E[Y_i(1) - Y_i(0) | T_i = 1]")

    st.markdown("""
    <span class="info">ملاحظة:</span> في التجارب العشوائية المحكومة، يكون ATE = ATT بسبب التعيين العشوائي.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>التحديات والمشكلات في التجارب العشوائية</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="warning">1. عدم الامتثال (Non-compliance):</span>
    - بعض المشاركين قد لا يلتزمون بالمعالجة المخصصة لهم
    - <span class="info">الحل:</span> تحليل النية للمعالجة (Intent-to-Treat, ITT) أو تقدير أثر المعالجة على الملتزمين (LATE)

    <span class="warning">2. التسرب (Attrition):</span>
    - فقدان بعض المشاركين أثناء الدراسة
    - <span class="info">الحل:</span> تحليل حساسية النتائج للتسرب ومتابعة المتسربين

    <span class="warning">3. انتشار المعالجة (Spillovers):</span>
    - تأثر مجموعة الضبط بالمعالجة بشكل غير مباشر
    - <span class="info">الحل:</span> التصميم المجموعي أو عزل المجموعات جغرافياً

    <span class="warning">4. تأثير هوثورن (Hawthorne Effect):</span>
    - تغير سلوك المشاركين لمجرد علمهم بأنهم تحت المراقبة
    - <span class="info">الحل:</span> استخدام المعالجة الوهمية (Placebo) أو التعمية المزدوجة

    <span class="warning">5. التعميم الخارجي (External Validity):</span>
    - صعوبة تعميم النتائج خارج عينة الدراسة
    - <span class="info">الحل:</span> اختيار عينة ممثلة وتكرار الدراسة في سياقات مختلفة
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>أمثلة على التجارب العشوائية المحكومة في الاقتصاد</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. تجارب التحويلات النقدية المشروطة:</span>
    - برنامج PROGRESA في المكسيك
    - قياس تأثير التحويلات النقدية على التعليم والصحة والفقر

    <span class="definition">2. تجارب التمويل الصغير:</span>
    - دراسات Banerjee و Duflo في الهند
    - قياس تأثير القروض الصغيرة على الفقر وريادة الأعمال

    <span class="definition">3. تجارب سياسات سوق العمل:</span>
    - برامج التدريب المهني والتوظيف
    - قياس تأثير التدريب على فرص العمل والدخل
    """, unsafe_allow_html=True)

elif current_section == "quasi":
    st.markdown('<div class="section-header"><h2>المنهج شبه التجريبي</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="definition">المنهج شبه التجريبي (Quasi-Experimental Method):</span> هو منهجية بحثية تهدف إلى تحديد العلاقات السببية في الحالات التي لا يمكن فيها إجراء تجارب عشوائية محكومة، من خلال استغلال مصادر تباين خارجية أو طبيعية في البيانات.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### متى نستخدم المنهج شبه التجريبي؟

    1. عندما تكون التجارب العشوائية المحكومة <span class="warning">غير ممكنة أخلاقياً</span> (مثل دراسة تأثير التدخين)
    2. عندما تكون التجارب العشوائية <span class="warning">غير ممكنة عملياً</span> (مثل دراسة السياسات على مستوى الدولة)
    3. عندما تكون التجارب العشوائية <span class="warning">مكلفة جداً</span> أو تستغرق وقتاً طويلاً
    4. لدراسة <span class="warning">آثار الأحداث الطبيعية</span> أو التغيرات السياسية غير المخططة
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الطرق الرئيسية في المنهج شبه التجريبي</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. طريقة الفروق في الفروق (Difference-in-Differences - DiD)</span>
    """, unsafe_allow_html=True)

    # إنشاء بيانات توضيحية لـ DiD
    np.random.seed(42)
    periods = np.array([0, 1])
    treatment = np.array([0, 1])

    control_before = 10 + np.random.normal(0, 1, 20)
    control_after = 11 + np.random.normal(0, 1, 20)
    treatment_before = 10.5 + np.random.normal(0, 1, 20)
    treatment_after = 13.5 + np.random.normal(0, 1, 20)

    df_did = pd.DataFrame({
        'المجموعة': ['ضبط'] * 40 + ['معالجة'] * 40,
        'الفترة': ['قبل'] * 20 + ['بعد'] * 20 + ['قبل'] * 20 + ['بعد'] * 20,
        'النتيجة': np.concatenate([control_before, control_after, treatment_before, treatment_after])
    })

    fig = px.box(df_did, x='الفترة', y='النتيجة', color='المجموعة',
                 title='توضيح طريقة الفروق في الفروق (DiD)',
                 color_discrete_map={'ضبط': primary_color, 'معالجة': accent_color})

    fig.update_layout(
        annotations=[
            dict(
                x=0.5,
                y=13,
                xref="x",
                yref="y",
                text="أثر المعالجة = (Y₁ₜ - Y₀ₜ) - (Y₁ₚ - Y₀ₚ)",
                showarrow=True,
                arrowhead=1,
                ax=0,
                ay=-40
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <span class="important-concept">فكرة الطريقة:</span> مقارنة التغير في النتائج بين مجموعة المعالجة ومجموعة الضبط قبل وبعد المعالجة.

    <span class="important-concept">المعادلة الأساسية:</span>
    """, unsafe_allow_html=True)

    st.latex(
        r"\text{أثر المعالجة} = (Y_{\text{treatment,after}} - Y_{\text{treatment,before}}) - (Y_{\text{control,after}} - Y_{\text{control,before}})")

    st.markdown("""
    <span class="important-concept">الفرضية الأساسية:</span> الاتجاهات المتوازية (Parallel Trends) - لولا المعالجة، لكانت مجموعة المعالجة تتبع نفس اتجاه مجموعة الضبط.

    <span class="success">مجالات الاستخدام:</span> تقييم تأثير سياسات عامة، تغييرات قانونية، برامج اقتصادية على مستوى المناطق أو الدول.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">2. طريقة الانحدار المتقطع (Regression Discontinuity Design - RDD)</span>
    """, unsafe_allow_html=True)

    # إنشاء بيانات توضيحية لـ RDD
    np.random.seed(42)
    x = np.random.uniform(-10, 10, 200)

    # عتبة عند x=0
    threshold = 0

    # إنشاء متغير المعالجة
    treatment = (x >= threshold).astype(int)

    # إنشاء النتيجة مع تأثير المعالجة
    y = 2 + 0.5 * x + 2 * treatment + np.random.normal(0, 1, 200)

    df_rdd = pd.DataFrame({'X': x, 'Y': y, 'Treatment': treatment})

    # ترتيب البيانات حسب X
    df_rdd = df_rdd.sort_values('X')

    fig = px.scatter(df_rdd, x='X', y='Y', color='Treatment',
                     title='توضيح طريقة الانحدار المتقطع (RDD)',
                     color_discrete_map={0: primary_color, 1: accent_color})

    # إضافة خط العتبة
    fig.add_vline(x=threshold, line_dash="dash", line_color="red")

    # إضافة خطوط انحدار لكل جانب
    x_left = df_rdd[df_rdd['X'] < threshold]['X']
    y_left = df_rdd[df_rdd['X'] < threshold]['Y']
    x_right = df_rdd[df_rdd['X'] >= threshold]['X']
    y_right = df_rdd[df_rdd['X'] >= threshold]['Y']

    fig.add_trace(
        go.Scatter(x=x_left, y=2 + 0.5 * x_left, mode='lines', name='انحدار يسار', line=dict(color=primary_color)))
    fig.add_trace(
        go.Scatter(x=x_right, y=4 + 0.5 * x_right, mode='lines', name='انحدار يمين', line=dict(color=accent_color)))

    fig.update_layout(
        annotations=[
            dict(
                x=threshold,
                y=4,
                xref="x",
                yref="y",
                text="العتبة",
                showarrow=True,
                arrowhead=1,
                ax=0,
                ay=-40
            ),
            dict(
                x=threshold,
                y=6,
                xref="x",
                yref="y",
                text="أثر المعالجة = الفرق عند العتبة",
                showarrow=True,
                arrowhead=1,
                ax=0,
                ay=-40
            )
        ]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <span class="important-concept">فكرة الطريقة:</span> استغلال عتبة معينة تحدد من يتلقى المعالجة ومن لا يتلقاها، ومقارنة النتائج للوحدات القريبة من العتبة من الجانبين.

    <span class="important-concept">المعادلة الأساسية:</span>
    """, unsafe_allow_html=True)

    st.latex(r"Y_i = \alpha + \beta \cdot T_i + f(X_i - c) + \varepsilon_i")

    st.markdown("""
    حيث:
    - $T_i$ = مؤشر المعالجة (1 إذا $X_i \geq c$، 0 خلاف ذلك)
    - $X_i$ = متغير التعيين (Running Variable)
    - $c$ = العتبة (Threshold)
    - $f(X_i - c)$ = دالة مرنة للمسافة من العتبة

    <span class="important-concept">الفرضية الأساسية:</span> الوحدات على جانبي العتبة مباشرة متشابهة في كل شيء باستثناء المعالجة.

    <span class="success">مجالات الاستخدام:</span> تقييم برامج المنح الدراسية، الدعم للأسر منخفضة الدخل، التأهل للخدمات الصحية.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">3. طريقة المتغيرات الأداتية (Instrumental Variables - IV)</span>
    """, unsafe_allow_html=True)

    # مخطط توضيحي للمتغيرات الأداتية
    mermaid_code = """
    graph LR
        Z[المتغير الأداتي Z] -->|المرحلة الأولى| T[متغير المعالجة T]
        T -->|المرحلة الثانية| Y[النتيجة Y]
        U[المتغيرات غير الملحوظة U] --> T
        U --> Y
        Z -.->|لا توجد علاقة مباشرة| Y
    """

    st.markdown("""
    <span class="important-concept">فكرة الطريقة:</span> استخدام متغير ثالث (المتغير الأداتي) يؤثر على متغير المعالجة ولا يؤثر على النتيجة إلا من خلال تأثيره على المعالجة.

    <span class="important-concept">المعادلات الأساسية:</span>
    """, unsafe_allow_html=True)

    st.latex(
        r"\begin{align} \text{المرحلة الأولى:} \quad T_i &= \gamma_0 + \gamma_1 Z_i + \eta_i \\ \text{المرحلة الثانية:} \quad Y_i &= \beta_0 + \beta_1 \hat{T}_i + \varepsilon_i \end{align}")

    st.markdown("""
    <span class="important-concept">شروط المتغير الأداتي الصالح:</span>
    1. <span class="info">الارتباط (Relevance):</span> ارتباط قوي مع متغير المعالجة
    2. <span class="info">الاستقلالية (Independence):</span> لا يتأثر بالمتغيرات غير الملحوظة
    3. <span class="info">القيد الاستبعادي (Exclusion Restriction):</span> لا يؤثر على النتيجة إلا من خلال المعالجة

    <span class="success">مجالات الاستخدام:</span> دراسة تأثير التعليم على الدخل، تأثير الهجرة على سوق العمل، تأثير الخصخصة على الكفاءة.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">4. طريقة المطابقة (Matching Methods)</span>
    """, unsafe_allow_html=True)

    # بيانات توضيحية للمطابقة
    np.random.seed(42)
    n = 100

    # متغيرات الخصائص
    x1 = np.random.normal(0, 1, n)
    x2 = np.random.normal(0, 1, n)

    # احتمالية المعالجة تعتمد على x1 و x2
    p = 1 / (1 + np.exp(-(0.5 * x1 + 0.5 * x2)))
    treatment = (np.random.uniform(0, 1, n) < p).astype(int)

    # النتيجة تتأثر بالمعالجة و x1 و x2
    y = 1 + 2 * treatment + 0.5 * x1 + 0.5 * x2 + np.random.normal(0, 1, n)

    df_match = pd.DataFrame({'X1': x1, 'X2': x2, 'Treatment': treatment, 'Y': y, 'p': p})

    fig = px.scatter(df_match, x='X1', y='X2', color='Treatment', size='p',
                     title='توضيح طريقة المطابقة - مطابقة وحدات متشابهة في الخصائص',
                     color_discrete_map={0: primary_color, 1: accent_color})

    # إضافة خطوط توصيل بين الوحدات المتشابهة
    matches = []
    for i in range(10):  # اختيار 10 وحدات فقط للتوضيح
        if df_match.iloc[i]['Treatment'] == 1:
            # إيجاد أقرب وحدة في مجموعة الضبط
            control_units = df_match[df_match['Treatment'] == 0]
            distances = np.sqrt((control_units['X1'] - df_match.iloc[i]['X1']) ** 2 +
                                (control_units['X2'] - df_match.iloc[i]['X2']) ** 2)
            closest_idx = distances.idxmin()

            matches.append((i, closest_idx))

    for match in matches:
        fig.add_trace(go.Scatter(
            x=[df_match.iloc[match[0]]['X1'], df_match.iloc[match[1]]['X1']],
            y=[df_match.iloc[match[0]]['X2'], df_match.iloc[match[1]]['X2']],
            mode='lines',
            line=dict(width=1, color='black', dash='dash'),
            showlegend=False
        ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    <span class="important-concept">فكرة الطريقة:</span> مطابقة كل وحدة في مجموعة المعالجة مع وحدة (أو أكثر) في مجموعة الضبط بناءً على خصائص متشابهة.

    <span class="important-concept">أنواع المطابقة:</span>
    1. <span class="info">المطابقة المباشرة (Exact Matching):</span> مطابقة دقيقة على جميع الخصائص
    2. <span class="info">مطابقة درجة الميل (Propensity Score Matching):</span> مطابقة على احتمالية المعالجة
    3. <span class="info">مطابقة المسافة (Distance Matching):</span> مطابقة على المسافة الإقليدية أو مسافة ماهالانوبيس

    <span class="important-concept">الفرضية الأساسية:</span> بعد المطابقة على الخصائص الملحوظة، لا توجد فروق منهجية غير ملحوظة بين المجموعات.

    <span class="success">مجالات الاستخدام:</span> تقييم برامج التوظيف، تأثير الاستثمار الأجنبي المباشر، دراسة آثار الانضمام للاتحادات التجارية.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>مقارنة بين طرق المنهج شبه التجريبي</h3></div>',
                unsafe_allow_html=True)

    comparison_data = pd.DataFrame({
        'الطريقة': ['الفروق في الفروق (DiD)', 'الانحدار المتقطع (RDD)', 'المتغيرات الأداتية (IV)',
                    'المطابقة (Matching)'],
        'الفرضية الأساسية': ['اتجاهات متوازية', 'تشابه الوحدات حول العتبة', 'شروط المتغير الأداتي',
                             'غياب التحيز بعد المطابقة'],
        'متى تستخدم': ['تغير في السياسة يؤثر على مجموعة معينة', 'وجود عتبة واضحة لتلقي المعالجة',
                       'وجود متغير أداتي مناسب', 'توفر بيانات غنية عن الخصائص'],
        'القيود': ['صعوبة التحقق من الاتجاهات المتوازية', 'قابلية التعميم محدودة حول العتبة', 'صعوبة إيجاد أدوات صالحة',
                   'حساسية لمتغيرات غير ملحوظة']
    })

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(comparison_data.columns),
                    fill_color=primary_color,
                    align='center',
                    font=dict(color='white', size=14)),
        cells=dict(values=[comparison_data[col] for col in comparison_data.columns],
                   fill_color='lavender',
                   align='center'))
    ])

    fig.update_layout(width=700, height=300)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="subsection-header"><h3>اختيار الطريقة المناسبة</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">عوامل اختيار الطريقة المناسبة:</span>

    1. <span class="info">طبيعة البيانات المتاحة:</span>
       - هل لديك بيانات قبل وبعد التدخل؟ (مناسب لـ DiD)
       - هل هناك عتبة واضحة لتلقي المعالجة؟ (مناسب لـ RDD)
       - هل لديك متغير يمكن استخدامه كأداة؟ (مناسب لـ IV)
       - هل لديك بيانات غنية عن خصائص المشاركين؟ (مناسب للمطابقة)

    2. <span class="info">طبيعة المعالجة:</span>
       - هل المعالجة على مستوى المجموعة أم الفرد؟
       - هل هي معالجة مستمرة أم ثنائية؟

    3. <span class="info">السؤال البحثي:</span>
       - هل تهتم بالأثر العام أم بأثر المعالجة على المعالجين؟
       - هل تهتم بالأثر عند نقطة معينة أم على مدى واسع؟

    4. <span class="info">قابلية تحقق الفرضيات:</span>
       - أي طريقة فرضياتها أكثر معقولية في سياقك البحثي؟
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="success">نصيحة:</span> لا تعتمد على طريقة واحدة فقط! استخدم مجموعة من الطرق للتحقق من متانة النتائج (Robustness Checks).
    </div>
    """, unsafe_allow_html=True)

elif current_section == "evaluation":
    st.markdown('<div class="section-header"><h2>طرق التقييم والتحليل</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    بعد جمع البيانات من التجارب أو المصادر الرصدية، نحتاج إلى تحليلها بطرق مناسبة لاستخلاص النتائج وتقييم الآثار السببية بشكل دقيق.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>تقدير الأثر السببي</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">مقاييس الأثر الرئيسية:</span>
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">1. متوسط الأثر العام (Average Treatment Effect - ATE):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{ATE} = E[Y_i(1) - Y_i(0)]")

    st.markdown("""
    <span class="info">التفسير:</span> متوسط الأثر على جميع الوحدات في العينة لو تم معالجة الجميع مقارنة بعدم معالجة أحد.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">2. متوسط الأثر على المعالجين (Average Treatment Effect on the Treated - ATT):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{ATT} = E[Y_i(1) - Y_i(0) | T_i = 1]")

    st.markdown("""
    <span class="info">التفسير:</span> متوسط الأثر على الوحدات التي تلقت المعالجة فقط.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">3. متوسط الأثر على غير المعالجين (Average Treatment Effect on the Untreated - ATU):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{ATU} = E[Y_i(1) - Y_i(0) | T_i = 0]")

    st.markdown("""
    <span class="info">التفسير:</span> متوسط الأثر المتوقع لو تم معالجة الوحدات التي لم تتلق المعالجة.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">4. الأثر الحدي للمعالجة (Marginal Treatment Effect - MTE):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{MTE}(x, u_D) = E[Y_1 - Y_0 | X = x, U_D = u_D]")

    st.markdown("""
    <span class="info">التفسير:</span> الأثر على الوحدات الهامشية (الذين هم على حافة القرار).
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">5. الأثر المحلي المتوسط للمعالجة (Local Average Treatment Effect - LATE):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{LATE} = E[Y_i(1) - Y_i(0) | \text{compliers}]")

    st.markdown("""
    <span class="info">التفسير:</span> الأثر على الوحدات التي تغير سلوكها استجابة للمتغير الأداتي (compliers).
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>نماذج الانحدار للتقييم</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. نموذج الانحدار البسيط:</span>
    """, unsafe_allow_html=True)

    st.latex(r"Y_i = \alpha + \beta T_i + \varepsilon_i")

    st.markdown("""
    <span class="info">الاستخدام:</span> في التجارب العشوائية المحكومة البسيطة.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">2. نموذج الانحدار مع متغيرات ضبط:</span>
    """, unsafe_allow_html=True)

    st.latex(r"Y_i = \alpha + \beta T_i + \gamma X_i + \varepsilon_i")

    st.markdown("""
    <span class="info">الاستخدام:</span> لزيادة الدقة أو التحكم في عدم التوازن في الخصائص.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">3. نموذج الفروق في الفروق (DiD):</span>
    """, unsafe_allow_html=True)

    st.latex(
        r"Y_{it} = \alpha + \beta \cdot \text{Treatment}_i + \gamma \cdot \text{Post}_t + \delta \cdot (\text{Treatment}_i \times \text{Post}_t) + \varepsilon_{it}")

    st.markdown("""
    <span class="info">الاستخدام:</span> لتقييم آثار سياسات أو برامج تم تطبيقها على مجموعة معينة في وقت معين.
    <br><span class="important-concept">المعامل المهم:</span> $\delta$ (معامل التفاعل) يمثل تقدير أثر المعالجة.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">4. نموذج الانحدار المتقطع (RDD):</span>
    """, unsafe_allow_html=True)

    st.latex(r"Y_i = \alpha + \beta T_i + \gamma_1 (X_i - c) + \gamma_2 T_i \cdot (X_i - c) + \varepsilon_i")

    st.markdown("""
    <span class="info">الاستخدام:</span> عندما يتم تحديد المعالجة بناءً على عتبة.
    <br><span class="important-concept">المعامل المهم:</span> $\beta$ يمثل تقدير أثر المعالجة عند العتبة.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">5. نموذج المتغيرات الأداتية (IV) - مرحلتين:</span>
    """, unsafe_allow_html=True)

    st.latex(
        r"\begin{align} \text{المرحلة الأولى:} \quad T_i &= \pi_0 + \pi_1 Z_i + \pi_2 X_i + \eta_i \\ \text{المرحلة الثانية:} \quad Y_i &= \beta_0 + \beta_1 \hat{T}_i + \beta_2 X_i + \varepsilon_i \end{align}")

    st.markdown("""
    <span class="info">الاستخدام:</span> عندما يكون هناك مشكلة اندوجينية في متغير المعالجة.
    <br><span class="important-concept">المعامل المهم:</span> $\beta_1$ في المرحلة الثانية يمثل تقدير أثر المعالجة.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اختبارات إحصائية وفحوص متانة النتائج</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. اختبارات الدلالة الإحصائية:</span>

    <span class="important-concept">اختبار t للمعاملات:</span>
    """, unsafe_allow_html=True)

    st.latex(r"t = \frac{\hat{\beta}}{\text{SE}(\hat{\beta})}")

    st.markdown("""
    <span class="info">التفسير:</span> إذا كانت |t| > 1.96 (للمستوى 5%)، فإن المعامل دال إحصائياً.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">القيمة الاحتمالية (p-value):</span>
    """, unsafe_allow_html=True)

    st.latex(r"p = \Pr(|T| > |t|)")

    st.markdown("""
    <span class="info">التفسير:</span> إذا كانت p < 0.05، فإن النتيجة دالة إحصائياً عند مستوى 5%.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">2. فترات الثقة (Confidence Intervals):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{CI}_{95\%} = \hat{\beta} \pm 1.96 \times \text{SE}(\hat{\beta})")

    st.markdown("""
    <span class="info">التفسير:</span> نتوقع أن القيمة الحقيقية للمعامل تقع ضمن هذا المدى بثقة 95%.
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">3. فحوص المتانة (Robustness Checks):</span>

    <span class="important-concept">تغيير مواصفات النموذج:</span>
    - إضافة أو إزالة متغيرات ضبط
    - تغيير الشكل الوظيفي (خطي، لوغاريتمي، تربيعي)
    - استخدام طرق تقدير مختلفة

    <span class="important-concept">تحليل العينات الفرعية:</span>
    - تقسيم العينة حسب خصائص مهمة (الجنس، العمر، المنطقة)
    - تحليل كل مجموعة على حدة للتحقق من تجانس الأثر

    <span class="important-concept">اختبارات الحساسية:</span>
    - تحليل حساسية النتائج للقيم المتطرفة (Outliers)
    - تحليل حساسية النتائج للافتراضات الأساسية
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>تحليل التباين في الآثار (Heterogeneous Effects)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تعريف:</span> دراسة كيف يختلف أثر المعالجة باختلاف خصائص الوحدات أو السياق.

    <span class="important-concept">أهمية تحليل التباين في الآثار:</span>
    - فهم من يستفيد أكثر من التدخل
    - تحديد الظروف المثلى لتطبيق البرنامج
    - تحسين تصميم السياسات المستقبلية

    <span class="important-concept">طرق تحليل التباين في الآثار:</span>

    1. <span class="info">تفاعلات في النموذج:</span>
    """, unsafe_allow_html=True)

    st.latex(r"Y_i = \alpha + \beta_1 T_i + \beta_2 X_i + \beta_3 (T_i \times X_i) + \varepsilon_i")

    st.markdown("""
    <span class="info">التفسير:</span> $\beta_3$ يقيس كيف يختلف أثر المعالجة مع تغير X.

    2. <span class="info">تقسيم العينة (Subgroup Analysis):</span>
    - تقدير النموذج بشكل منفصل لكل مجموعة فرعية
    - مقارنة معاملات المعالجة بين المجموعات

    3. <span class="info">تحليل التأثيرات الكمية (Quantile Treatment Effects):</span>
    - تقدير أثر المعالجة عند مستويات مختلفة من توزيع النتيجة
    - يساعد في فهم كيف يختلف الأثر باختلاف مستوى النتيجة
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>تقييم التكلفة والعائد (Cost-Benefit Analysis)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تعريف:</span> مقارنة التكاليف الاقتصادية للتدخل مع الفوائد المتوقعة منه.

    <span class="important-concept">خطوات تحليل التكلفة والعائد:</span>

    1. <span class="info">تحديد وقياس جميع التكاليف:</span>
    - التكاليف المباشرة (تنفيذ البرنامج)
    - التكاليف غير المباشرة (تكلفة الفرصة البديلة)

    2. <span class="info">تحديد وقياس جميع الفوائد:</span>
    - الفوائد المباشرة (زيادة الدخل، تحسن الصحة)
    - الفوائد غير المباشرة (الآثار الخارجية الإيجابية)

    3. <span class="info">تحويل الفوائد والتكاليف إلى قيم نقدية:</span>
    - استخدام تقنيات التقييم الاقتصادي
    - خصم القيم المستقبلية (Discounting)

    4. <span class="info">حساب مؤشرات الجدوى:</span>
    """, unsafe_allow_html=True)

    st.latex(
        r"\text{صافي القيمة الحالية (NPV)} = \sum_{t=0}^{T} \frac{\text{الفوائد}_t - \text{التكاليف}_t}{(1 + r)^t}")

    st.latex(
        r"\text{نسبة الفوائد إلى التكاليف (BCR)} = \frac{\sum_{t=0}^{T} \frac{\text{الفوائد}_t}{(1 + r)^t}}{\sum_{t=0}^{T} \frac{\text{التكاليف}_t}{(1 + r)^t}}")

    st.markdown("""
    <span class="info">التفسير:</span>
    - إذا كان NPV > 0 أو BCR > 1، فإن التدخل مجدي اقتصادياً
    - كلما زادت قيمة NPV أو BCR، كلما كان التدخل أكثر كفاءة
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تحليل فعالية التكلفة (Cost-Effectiveness Analysis):</span>
    """, unsafe_allow_html=True)

    st.latex(r"\text{نسبة فعالية التكلفة} = \frac{\text{التكلفة الإجمالية}}{\text{وحدات الأثر}}")

    st.markdown("""
    <span class="info">التفسير:</span> تكلفة تحقيق وحدة واحدة من النتيجة المرغوبة (مثل: تكلفة إنقاذ حياة واحدة، تكلفة زيادة الدخل بدولار واحد).

    <span class="important-concept">استخدامات تحليل التكلفة والعائد:</span>
    - المقارنة بين تدخلات بديلة
    - تحديد الحجم الأمثل للتدخل
    - تبرير الاستثمار في برامج معينة
    """, unsafe_allow_html=True)

elif current_section == "assumptions":
    st.markdown('<div class="section-header"><h2>الفرضيات الأساسية</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    لتحديد العلاقات السببية بشكل صحيح، يجب أن تستوفي أساليب البحث مجموعة من الفرضيات الأساسية. فهم هذه الفرضيات أمر بالغ الأهمية للتطبيق السليم والتفسير الصحيح للنتائج.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المشكلة الأساسية للاستدلال السببي</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">المشكلة الأساسية للاستدلال السببي (Fundamental Problem of Causal Inference):</span>

    لا يمكننا ملاحظة النتائج المحتملة البديلة للوحدة نفسها في نفس الوقت.
    """, unsafe_allow_html=True)

    st.latex(r"Y_i = \begin{cases} Y_i(1) & \text{إذا } T_i = 1 \\ Y_i(0) & \text{إذا } T_i = 0 \end{cases}")

    st.markdown("""
    <span class="warning">لا يمكننا ملاحظة $Y_i(1)$ و $Y_i(0)$ معاً لنفس الوحدة $i$.</span>

    <span class="important-concept">المنظور الإحصائي:</span> نحتاج إلى تقدير النتيجة المضادة للواقع (Counterfactual) التي لا نستطيع ملاحظتها.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>فرضيات التجارب العشوائية المحكومة</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. الاستقلال الإحصائي (Statistical Independence):</span>

    التعيين العشوائي يضمن استقلالية المعالجة عن النتائج المحتملة.
    """, unsafe_allow_html=True)

    st.latex(r"\{Y_i(0), Y_i(1)\} \perp\!\!\!\perp T_i")

    st.markdown("""
    <span class="info">ما يعنيه:</span> التعيين العشوائي يجعل مجموعات المعالجة والضبط متشابهة في المتوسط في جميع الخصائص الملحوظة وغير الملحوظة.

    <span class="definition">2. الثبات المؤقت (Temporal Stability):</span>

    النتائج المحتملة للوحدة لا تتأثر بمعالجة الوحدات الأخرى.
    """, unsafe_allow_html=True)

    st.latex(r"Y_i(t) = Y_i(t'; t_{-i})")

    st.markdown("""
    <span class="info">ما يعنيه:</span> عدم وجود آثار انتشار (Spillover Effects) أو تلوث (Contamination) بين الوحدات.

    <span class="definition">3. الالتزام بالمعالجة (Compliance):</span>

    المشاركون يلتزمون بالمعالجة المخصصة لهم.
    """, unsafe_allow_html=True)

    st.latex(r"T_i = Z_i")

    st.markdown("""
    <span class="info">ما يعنيه:</span> عدم وجود عدم امتثال (Non-compliance) أو انتقال بين المجموعات.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>فرضيات المنهج شبه التجريبي</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. فرضيات طريقة الفروق في الفروق (DiD):</span>

    <span class="important-concept">فرضية الاتجاهات المتوازية (Parallel Trends):</span>

    لولا المعالجة، لكانت مجموعة المعالجة تتبع نفس اتجاه مجموعة الضبط مع مرور الوقت.
    """, unsafe_allow_html=True)

    st.latex(r"E[Y_{it}(0) - Y_{it'}(0) | T_i = 1] = E[Y_{it}(0) - Y_{it'}(0) | T_i = 0]")

    st.markdown("""
    <span class="info">كيفية الاختبار:</span> فحص الاتجاهات قبل المعالجة (Pre-treatment Trends).

    <span class="warning">المشكلات المحتملة:</span> أحداث متزامنة، صدمات غير متماثلة، تغيير تكوين المجموعات مع الوقت.

    <span class="definition">2. فرضيات طريقة الانحدار المتقطع (RDD):</span>

    <span class="important-concept">فرضية الاستمرارية (Continuity Assumption):</span>

    النتائج المحتملة تتغير بشكل مستمر مع متغير التعيين حول العتبة.
    """, unsafe_allow_html=True)

    st.latex(r"E[Y_i(0)|X_i = x] \text{ و } E[Y_i(1)|X_i = x] \text{ دوال مستمرة في } x \text{ عند } x = c")

    st.markdown("""
    <span class="info">كيفية الاختبار:</span> فحص استمرارية المتغيرات المتحكمة حول العتبة، فحص تراكم غير طبيعي للوحدات حول العتبة.

    <span class="warning">المشكلات المحتملة:</span> التلاعب بمتغير التعيين، عتبات متعددة متداخلة.

    <span class="definition">3. فرضيات طريقة المتغيرات الأداتية (IV):</span>

    <span class="important-concept">فرضية الارتباط (Relevance):</span>

    المتغير الأداتي يرتبط بشكل قوي مع متغير المعالجة.
    """, unsafe_allow_html=True)

    st.latex(r"Corr(Z_i, T_i) \neq 0")

    st.markdown("""
    <span class="info">كيفية الاختبار:</span> المرحلة الأولى من التقدير، اختبار F للأدوات.

    <span class="important-concept">فرضية القيد الاستبعادي (Exclusion Restriction):</span>

    المتغير الأداتي لا يؤثر على النتيجة إلا من خلال تأثيره على المعالجة.
    """, unsafe_allow_html=True)

    st.latex(r"Z_i \perp\!\!\!\perp Y_i | T_i")

    st.markdown("""
    <span class="info">كيفية الاختبار:</span> لا يمكن اختبارها إحصائياً، تعتمد على النظرية والمعرفة بالموضوع.

    <span class="important-concept">فرضية الاستقلالية (Independence):</span>

    المتغير الأداتي مستقل عن المتغيرات غير الملحوظة التي تؤثر على النتيجة.
    """, unsafe_allow_html=True)

    st.latex(r"Z_i \perp\!\!\!\perp \varepsilon_i")

    st.markdown("""
    <span class="info">كيفية الاختبار:</span> لا يمكن اختبارها مباشرة، اختبار التوازن في الخصائص الملحوظة.

    <span class="definition">4. فرضيات طريقة المطابقة (Matching):</span>

    <span class="important-concept">فرضية الاستقلالية الشرطية (Conditional Independence Assumption):</span>

    بعد التحكم في المتغيرات الملحوظة، تصبح المعالجة مستقلة عن النتائج المحتملة.
    """, unsafe_allow_html=True)

    st.latex(r"\{Y_i(0), Y_i(1)\} \perp\!\!\!\perp T_i | X_i")

    st.markdown("""
    <span class="info">ما يعنيه:</span> لا توجد متغيرات غير ملحوظة تؤثر على كل من المعالجة والنتائج (عدم وجود تحيز متبقي).

    <span class="important-concept">فرضية الدعم المشترك (Common Support):</span>

    لكل مجموعة من قيم X، هناك احتمال إيجابي للمعالجة وعدم المعالجة.
    """, unsafe_allow_html=True)

    st.latex(r"0 < P(T_i = 1 | X_i = x) < 1 \quad \forall x")

    st.markdown("""
    <span class="info">ما يعنيه:</span> يمكن إيجاد وحدات متشابهة في مجموعتي المعالجة والضبط لجميع قيم X.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اختبار الفرضيات وتحليل الحساسية</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">1. اختبار التوازن (Balance Tests):</span>

    مقارنة الخصائص الملحوظة بين مجموعات المعالجة والضبط.
    """, unsafe_allow_html=True)

    st.latex(r"\text{فرق المتوسطات} = E[X_i | T_i = 1] - E[X_i | T_i = 0]")

    st.markdown("""
    <span class="info">التفسير:</span> الفروق الصغيرة وغير الدالة إحصائياً تشير إلى توازن جيد.

    <span class="definition">2. اختبارات التصريف (Placebo Tests):</span>

    <span class="important-concept">اختبارات التصريف الزمنية:</span> استخدام فترات زمنية قبل المعالجة للتحقق من عدم وجود آثار وهمية.

    <span class="important-concept">اختبارات التصريف المكانية:</span> استخدام مناطق لم تتأثر بالمعالجة للتحقق من عدم وجود آثار وهمية.

    <span class="important-concept">اختبارات النتائج غير المرتبطة:</span> استخدام متغيرات نتيجة لا يُتوقع أن تتأثر بالمعالجة.

    <span class="definition">3. تحليل الحساسية للفرضيات غير القابلة للاختبار:</span>

    <span class="important-concept">حدود روزنباوم (Rosenbaum Bounds):</span> تقدير مدى حساسية النتائج للمتغيرات غير الملحوظة.

    <span class="important-concept">تحليل التحيز المتبقي:</span> تقدير حجم التحيز المطلوب لإلغاء النتائج.

    <span class="important-concept">تقديرات Oster للتحيز المحدود (Oster's Bounded Estimates):</span> تقدير حساسية النتائج للمتغيرات غير الملحوظة بناءً على المتغيرات الملحوظة.
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الصلاحية الداخلية والخارجية</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">الصلاحية الداخلية (Internal Validity):</span>

    مدى صحة استنتاج العلاقة السببية في العينة المدروسة.

    <span class="important-concept">عوامل تهدد الصلاحية الداخلية:</span>
    - التحيز في الاختيار (Selection Bias)
    - التاريخ (History) - أحداث خارجية متزامنة مع المعالجة
    - النضج (Maturation) - تغيرات طبيعية مع مرور الوقت
    - الانحدار نحو المتوسط (Regression to the Mean)
    - التسرب الانتقائي (Selective Attrition)
    - عدم الامتثال (Non-compliance)

    <span class="definition">الصلاحية الخارجية (External Validity):</span>

    مدى إمكانية تعميم النتائج خارج العينة المدروسة.

    <span class="important-concept">عوامل تهدد الصلاحية الخارجية:</span>
    - التفاعل بين الاختيار والمعالجة
    - التفاعل بين الإعداد والمعالجة
    - التفاعل بين التاريخ والمعالجة
    - تأثيرات هوثورن والتجريب
    - الآثار غير الخطية والآثار غير المتجانسة
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="success">نصيحة:</span> يجب دائماً مناقشة مدى تحقق الفرضيات في دراستك، وإجراء اختبارات لتقييم صحتها حيثما أمكن، وتوضيح القيود والتحذيرات المناسبة عند تفسير النتائج.
    </div>
    """, unsafe_allow_html=True)

elif current_section == "applications":
    st.markdown('<div class="section-header"><h2>التطبيقات في الاقتصاد</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    المنهج التجريبي وشبه التجريبي يستخدم على نطاق واسع في مختلف مجالات الاقتصاد لتقييم السياسات وفهم السلوك الاقتصادي واختبار النظريات.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اقتصاديات التنمية (Development Economics)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج التجريبي:</span>

    <span class="important-concept">1. برامج التحويلات النقدية:</span>
    - تقييم أثر التحويلات النقدية المشروطة وغير المشروطة على الفقر والتعليم والصحة
    - مثال: برنامج PROGRESA/Oportunidades في المكسيك

    <span class="important-concept">2. التمويل الصغير والادخار:</span>
    - تقييم أثر القروض الصغيرة وبرامج الادخار على الاستثمار وريادة الأعمال
    - مثال: دراسات Banerjee وDuflo وCrepon في الهند والمغرب

    <span class="important-concept">3. الزراعة:</span>
    - تقييم أثر التكنولوجيا الزراعية والتأمين على الإنتاجية والمخاطر
    - مثال: دراسات التأمين على أساس المؤشر في غانا والهند
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج شبه التجريبي:</span>

    <span class="important-concept">1. الهجرة والتحويلات:</span>
    - استخدام الكوارث الطبيعية أو الصدمات الاقتصادية كمتغيرات أداتية
    - مثال: دراسة تأثير تحويلات المغتربين على التنمية المحلية

    <span class="important-concept">2. البنية التحتية:</span>
    - استخدام الفروق في الفروق لتقييم تأثير مشاريع البنية التحتية
    - مثال: تأثير بناء الطرق أو شبكات الاتصالات على التنمية الاقتصادية
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اقتصاديات العمل (Labor Economics)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج التجريبي:</span>

    <span class="important-concept">1. برامج التدريب والتوظيف:</span>
    - تقييم أثر برامج التدريب المهني على فرص العمل والأجور
    - مثال: تجارب Job Training Partnership Act في الولايات المتحدة

    <span class="important-concept">2. تجارب سوق العمل:</span>
    - دراسة التمييز والتحيز في التوظيف
    - مثال: دراسات إرسال سير ذاتية متماثلة بأسماء مختلفة

    <span class="important-concept">3. حوافز العمل:</span>
    - تقييم أثر الحوافز المالية على الإنتاجية والجهد
    - مثال: تجارب دفع الأجور بالقطعة مقابل الأجر الثابت
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج شبه التجريبي:</span>

    <span class="important-concept">1. الحد الأدنى للأجور:</span>
    - استخدام الفروق في الفروق لمقارنة المناطق التي طبقت تغييرات في الحد الأدنى للأجور
    - مثال: دراسة Card و Krueger لتأثير زيادة الحد الأدنى للأجور على التوظيف

    <span class="important-concept">2. التعليم والعوائد:</span>
    - استخدام المتغيرات الأداتية مثل قوانين التعليم الإلزامي لتقدير عوائد التعليم
    - مثال: دراسة Angrist و Krueger (1991) لتأثير التعليم على الأجور

    <span class="important-concept">3. برامج التأمين ضد البطالة:</span>
    - استخدام الانحدار المتقطع لتقييم أثر مدة استحقاق إعانات البطالة
    - مثال: دراسة تأثير زيادة مدة إعانات البطالة على فترة البحث عن عمل
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اقتصاديات التعليم (Economics of Education)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج التجريبي:</span>

    <span class="important-concept">1. الحوافز التعليمية:</span>
    - تقييم أثر المكافآت المالية للطلاب والمعلمين على الأداء التعليمي
    - مثال: تجارب Fryer في المدارس الأمريكية

    <span class="important-concept">2. تدخلات جودة التعليم:</span>
    - تقييم أثر تقليل حجم الفصل، الكتب المدرسية، التكنولوجيا التعليمية
    - مثال: تجربة STAR في تينيسي لتقليل حجم الفصل

    <span class="important-concept">3. التعليم في مرحلة الطفولة المبكرة:</span>
    - تقييم أثر برامج ما قبل المدرسة على النتائج التعليمية طويلة المدى
    - مثال: تجارب برنامج Head Start
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج شبه التجريبي:</span>

    <span class="important-concept">1. اختيار المدرسة والكفاءة:</span>
    - استخدام اليانصيب المدرسي كتجربة طبيعية لتقييم تأثير نوع المدرسة
    - مثال: دراسات المدارس المستقلة (Charter Schools) في الولايات المتحدة

    <span class="important-concept">2. جودة المعلم:</span>
    - استخدام التعيين العشوائي للمعلمين لتقدير تأثير جودة المعلم
    - مثال: دراسة Chetty وFriedman وRockoff لتأثير المعلمين على النتائج طويلة المدى

    <span class="important-concept">3. الإصلاحات التعليمية:</span>
    - استخدام الفروق في الفروق لتقييم تأثير الإصلاحات التعليمية على نطاق واسع
    - مثال: تقييم قانون "عدم ترك أي طفل" (No Child Left Behind) في الولايات المتحدة
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الاقتصاد السلوكي (Behavioral Economics)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج التجريبي:</span>

    <span class="important-concept">1. التحيزات السلوكية والقرارات الاقتصادية:</span>
    - دراسة تأثير التحيزات المعرفية على القرارات المالية والاستهلاكية
    - مثال: تجارب حول التحيز للحاضر (Present Bias) والإيثار والثقة

    <span class="important-concept">2. التلكزات (Nudges):</span>
    - تقييم أثر التدخلات السلوكية البسيطة على القرارات الاقتصادية
    - مثال: تجارب زيادة معدلات الادخار من خلال الاشتراك التلقائي

    <span class="important-concept">3. التفضيلات الاجتماعية:</span>
    - دراسة الإيثار والعدالة والتعاون في السلوك الاقتصادي
    - مثال: ألعاب المختبر مثل لعبة الإنذار ولعبة الثقة
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج شبه التجريبي:</span>

    <span class="important-concept">1. التأثيرات الاجتماعية:</span>
    - استخدام التغيرات الخارجية في شبكات الأقران لدراسة تأثير الأقران
    - مثال: دراسة تأثير الأقران على سلوكيات الادخار والاستهلاك

    <span class="important-concept">2. تصميم الأسواق والسياسات:</span>
    - تقييم أثر تغييرات التصميم في الأسواق والسياسات على السلوك
    - مثال: دراسة تأثير تغيير طريقة عرض المعلومات على قرارات المستهلكين
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اقتصاديات الصحة (Health Economics)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج التجريبي:</span>

    <span class="important-concept">1. التأمين الصحي:</span>
    - تقييم أثر التأمين الصحي على استخدام الخدمات الصحية والنتائج الصحية
    - مثال: تجربة Oregon Health Insurance Experiment

    <span class="important-concept">2. الوقاية والسلوكيات الصحية:</span>
    - دراسة فعالية تدخلات تغيير السلوكيات الصحية
    - مثال: تجارب الحوافز المالية للإقلاع عن التدخين أو فقدان الوزن

    <span class="important-concept">3. جودة الرعاية الصحية:</span>
    - تقييم تدخلات تحسين جودة الخدمات الصحية
    - مثال: تجارب الحوافز للأطباء ومقدمي الرعاية الصحية
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج شبه التجريبي:</span>

    <span class="important-concept">1. إصلاحات نظم الرعاية الصحية:</span>
    - استخدام الفروق في الفروق لتقييم أثر إصلاحات الرعاية الصحية
    - مثال: تقييم أثر قانون الرعاية الميسرة (Affordable Care Act) في الولايات المتحدة

    <span class="important-concept">2. تأثير الصحة على الإنتاجية والدخل:</span>
    - استخدام المتغيرات الأداتية مثل تفشي الأمراض لتقدير تأثير الصحة على النتائج الاقتصادية
    - مثال: دراسة تأثير التدخلات الصحية في الطفولة المبكرة على النتائج الاقتصادية في مرحلة البلوغ
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>اقتصاديات البيئة (Environmental Economics)</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج التجريبي:</span>

    <span class="important-concept">1. السلوكيات البيئية:</span>
    - دراسة فعالية التدخلات لتشجيع السلوكيات الصديقة للبيئة
    - مثال: تجارب حول تأثير المعلومات والحوافز على استهلاك الطاقة

    <span class="important-concept">2. حقوق الملكية والموارد المشتركة:</span>
    - دراسة تأثير ترتيبات حقوق الملكية على إدارة الموارد الطبيعية
    - مثال: تجارب حول إدارة الموارد المائية أو الغابات
    """, unsafe_allow_html=True)

    st.markdown("""
    <span class="definition">تطبيقات المنهج شبه التجريبي:</span>

    <span class="important-concept">1. تلوث الهواء والصحة:</span>
    - استخدام التغيرات الخارجية في التلوث لتقدير تأثيره على الصحة
    - مثال: دراسة تأثير سياسات خفض التلوث على النتائج الصحية

    <span class="important-concept">2. تغير المناخ والاقتصاد:</span>
    - استخدام التغيرات المناخية كصدمات خارجية لتقدير تأثيرها الاقتصادي
    - مثال: دراسة تأثير الظواهر المناخية المتطرفة على الإنتاجية الزراعية

    <span class="important-concept">3. سياسات الطاقة:</span>
    - استخدام الفروق في الفروق لتقييم أثر سياسات الطاقة المتجددة
    - مثال: تقييم أثر دعم الطاقة الشمسية أو الرياح على انبعاثات الكربون والنمو الاقتصادي
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="success">ملاحظة مهمة:</span> التطبيقات المذكورة أعلاه تمثل جزءًا صغيرًا فقط من استخدامات المنهج التجريبي وشبه التجريبي في الاقتصاد. مع تطور الأدوات والبيانات، تتسع مجالات التطبيق باستمرار، مما يسمح للباحثين بمعالجة أسئلة أكثر تعقيدًا وأهمية.
    </div>
    """, unsafe_allow_html=True)

elif current_section == "learning_plan":
    st.markdown('<div class="section-header"><h2>خطة التعلم الشاملة</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    إليك خطة تعلم متكاملة لإتقان المنهج التجريبي وشبه التجريبي في القياس الاقتصادي، مقسمة إلى مراحل متدرجة تناسب المبتدئين.
    </div>
    """, unsafe_allow_html=True)

    # تصميم مخطط لخطة التعلم
    stages = ["المرحلة التمهيدية", "المرحلة الأساسية", "المرحلة المتوسطة", "المرحلة المتقدمة", "التطبيق العملي"]
    durations = ["4-6 أسابيع", "8-10 أسابيع", "8-10 أسابيع", "8-12 أسبوع", "مستمر"]

    df_plan = pd.DataFrame({
        'المرحلة': stages,
        'المدة التقريبية': durations
    })

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df_plan.columns),
                    fill_color=primary_color,
                    align='center',
                    font=dict(color='white', size=14)),
        cells=dict(values=[df_plan['المرحلة'], df_plan['المدة التقريبية']],
                   fill_color='lavender',
                   align='center'))
    ])

    fig.update_layout(width=700, height=250)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="subsection-header"><h3>المرحلة التمهيدية: الأساسيات والمفاهيم</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">الأهداف التعليمية:</span>
    - فهم أساسيات الإحصاء والاحتمالات
    - التعرف على المفاهيم الأساسية للسببية والارتباط
    - فهم أنواع البيانات الاقتصادية
    - تعلم أساسيات برمجة بايثون للتحليل الإحصائي

    <span class="definition">المواضيع الرئيسية:</span>
    1. <span class="info">أساسيات الإحصاء:</span> المتوسطات، التشتت، الارتباط، الانحدار البسيط
    2. <span class="info">الاحتمالات الأساسية:</span> التوزيعات الاحتمالية، العينات العشوائية
    3. <span class="info">مفاهيم السببية:</span> الفرق بين الارتباط والسببية، المشكلة الأساسية للاستدلال السببي
    4. <span class="info">أنواع البيانات:</span> البيانات المقطعية، السلاسل الزمنية، بيانات البانل
    5. <span class="info">أساسيات البرمجة:</span> بايثون، Pandas، NumPy، Matplotlib

    <span class="success">الموارد المقترحة:</span>
    - كتاب: "مقدمة في الإحصاء للاقتصاد" - Stock & Watson (الفصول الأولى)
    - دورة عبر الإنترنت: "الإحصاء والاحتمالات للاقتصاد" على Coursera أو edX
    - دورة برمجة: "Python for Data Science" على DataCamp

    <span class="warning">المهارات المتوقعة بنهاية المرحلة:</span>
    - القدرة على فهم المفاهيم الإحصائية الأساسية
    - القدرة على التمييز بين الارتباط والسببية
    - القدرة على استخدام بايثون في التحليل الإحصائي البسيط
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المرحلة الأساسية: المنهج التجريبي</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">الأهداف التعليمية:</span>
    - فهم أسس التجارب العشوائية المحكومة
    - تعلم طرق تصميم وتنفيذ التجارب
    - فهم طرق تقدير الأثر السببي
    - تعلم تحليل نتائج التجارب

    <span class="definition">المواضيع الرئيسية:</span>
    1. <span class="info">التجارب العشوائية المحكومة:</span> المبادئ، التصميم، التنفيذ
    2. <span class="info">التعيين العشوائي:</span> طرق التعيين، حساب حجم العينة، التوازن
    3. <span class="info">قياس الأثر:</span> متوسط الأثر العام (ATE)، متوسط الأثر على المعالجين (ATT)
    4. <span class="info">تحليل البيانات التجريبية:</span> نماذج الانحدار، اختبارات الدلالة، فترات الثقة
    5. <span class="info">مشاكل التنفيذ:</span> عدم الامتثال، التسرب، انتشار المعالجة

    <span class="success">الموارد المقترحة:</span>
    - كتاب: "Mastering 'Metrics" - Angrist & Pischke
    - كتاب: "Field Experiments" - Gerber & Green
    - دورة: "Evaluating Social Programs" من J-PAL على edX

    <span class="warning">المهارات المتوقعة بنهاية المرحلة:</span>
    - القدرة على تصميم تجربة عشوائية بسيطة
    - القدرة على تحليل نتائج التجارب وتقدير الأثر السببي
    - القدرة على تحديد المشاكل المحتملة في التجارب وكيفية معالجتها
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المرحلة المتوسطة: المنهج شبه التجريبي</h3></div>',
                unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">الأهداف التعليمية:</span>
    - فهم طرق المنهج شبه التجريبي المختلفة
    - تعلم كيفية اختيار الطريقة المناسبة
    - فهم الفرضيات الأساسية لكل طريقة
    - تعلم تنفيذ وتحليل الطرق شبه التجريبية

    <span class="definition">المواضيع الرئيسية:</span>
    1. <span class="info">طريقة الفروق في الفروق (DiD):</span> المبادئ، التطبيق، الاختبارات
    2. <span class="info">طريقة الانحدار المتقطع (RDD):</span> المبادئ، أنواع RDD، التنفيذ
    3. <span class="info">طريقة المتغيرات الأداتية (IV):</span> المبادئ، شروط الصلاحية، التقدير
    4. <span class="info">طريقة المطابقة (Matching):</span> أنواع المطابقة، درجة الميل، التنفيذ
    5. <span class="info">اختبارات الفرضيات:</span> اختبارات التوازن، اختبارات التصريف، تحليل الحساسية

    <span class="success">الموارد المقترحة:</span>
    - كتاب: "Mostly Harmless Econometrics" - Angrist & Pischke
    - كتاب: "Causal Inference: The Mixtape" - Cunningham
<span class="warning">المهارات المتوقعة بنهاية المرحلة:</span>
    - القدرة على اختيار الطريقة شبه التجريبية المناسبة للمشكلة البحثية
    - القدرة على تنفيذ الطرق شبه التجريبية باستخدام البرمجة
    - القدرة على تقييم صحة الفرضيات وتفسير النتائج بشكل صحيح
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المرحلة المتقدمة: تقنيات متقدمة والقضايا المعاصرة</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">الأهداف التعليمية:</span>
    - فهم التقنيات المتقدمة في الاستدلال السببي
    - تعلم طرق التقييم المتقدمة
    - فهم قضايا الصلاحية الداخلية والخارجية
    - تعلم تحليل الآثار غير المتجانسة والتعميم
    
    <span class="definition">المواضيع الرئيسية:</span>
    1. <span class="info">تقنيات متقدمة:</span> التحليل البنيوي، نماذج المعادلات الهيكلية، التعلم الآلي للاستدلال السببي
    2. <span class="info">تقييم السياسات:</span> تحليل التكلفة والعائد، تحليل الرفاهية، تعميم النتائج
    3. <span class="info">الآثار غير المتجانسة:</span> تحليل المجموعات الفرعية، التأثيرات الكمية، التأثيرات المحلية
    4. <span class="info">قضايا التصميم المتقدمة:</span> التعيين العشوائي المجموعي، التجارب الطولية، التجارب المتتالية
    5. <span class="info">القضايا المعاصرة:</span> البيانات الضخمة، الخصوصية، الأخلاقيات
    
    <span class="success">الموارد المقترحة:</span>
    - كتاب: "Causal Inference for Statistics, Social, and Biomedical Sciences" - Imbens & Rubin
    - كتاب: "Elements of Causal Inference" - Peters, Janzing & Schölkopf
    - أوراق بحثية حديثة في المجال
    
    <span class="warning">المهارات المتوقعة بنهاية المرحلة:</span>
    - القدرة على تطبيق تقنيات متقدمة في الاستدلال السببي
    - القدرة على تقييم السياسات بشكل شامل
    - القدرة على التعامل مع قضايا معقدة في التصميم والتحليل
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>مرحلة التطبيق العملي: المشاريع والبحوث</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">الأهداف التعليمية:</span>
    - تطبيق المعرفة النظرية على مشاريع عملية
    - تطوير مهارات البحث والتحليل
    - بناء ملف شخصي من المشاريع البحثية
    
    <span class="definition">الأنشطة المقترحة:</span>
    1. <span class="info">مشروع بحثي صغير:</span> تصميم وتنفيذ دراسة شبه تجريبية باستخدام بيانات متاحة
    2. <span class="info">إعادة تحليل:</span> إعادة تحليل دراسة منشورة باستخدام طرق مختلفة
    3. <span class="info">مراجعة نقدية:</span> مراجعة وتقييم منهجية دراسات منشورة
    4. <span class="info">محاكاة:</span> إجراء دراسات محاكاة لتقييم أداء طرق مختلفة
    5. <span class="info">مشروع جماعي:</span> العمل ضمن فريق على مشكلة بحثية معقدة
    
    <span class="success">الموارد المقترحة:</span>
    - مصادر البيانات المفتوحة: البنك الدولي، IPUMS، Dataverse
    - منصات المنافسات البحثية: Kaggle، DrivenData
    - مجتمعات الباحثين: GitHub، Stack Exchange، مجموعات البحث
    
    <span class="warning">المهارات المتوقعة بنهاية المرحلة:</span>
    - القدرة على إجراء بحث مستقل باستخدام المنهج التجريبي أو شبه التجريبي
    - القدرة على التواصل العلمي وعرض النتائج البحثية
    - امتلاك ملف شخصي من المشاريع البحثية
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>نصائح للدراسة الفعّالة</h3></div>', unsafe_allow_html=True)

    st.markdown("""
    <span class="important-concept">1. التعلم التدريجي:</span>
    - البدء بالمفاهيم الأساسية قبل الانتقال للموضوعات المتقدمة
    - التركيز على فهم الأساسيات بعمق
    - تخصيص وقت كافٍ لكل مرحلة قبل الانتقال للتالية
    
    <span class="important-concept">2. التعلم العملي:</span>
    - تطبيق ما تتعلمه على أمثلة واقعية
    - العمل على مشاريع صغيرة لتعزيز الفهم
    - استخدام البيانات الحقيقية كلما أمكن
    
    <span class="important-concept">3. التعلم التعاوني:</span>
    - الانضمام لمجموعات دراسية أو مجتمعات بحثية
    - مناقشة المفاهيم والتحديات مع الآخرين
    - المشاركة في ورش العمل والمؤتمرات
    
    <span class="important-concept">4. التعلم المستمر:</span>
    - متابعة التطورات الجديدة في المجال
    - قراءة الأوراق البحثية الحديثة
    - الاشتراك في النشرات الإخبارية والمدونات المتخصصة
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="success">ملاحظة مهمة:</span> هذه الخطة مرنة ويمكن تعديلها حسب احتياجاتك وخلفيتك الأكاديمية والوقت المتاح لديك. المهم هو الاستمرارية والتطبيق العملي لما تتعلمه.
    </div>
    """, unsafe_allow_html=True)

elif current_section == "resources":
    st.markdown('<div class="section-header"><h2>الموارد والمراجع</h2></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    فيما يلي قائمة شاملة بالموارد والمراجع لمساعدتك في تعلم المنهج التجريبي وشبه التجريبي في القياس الاقتصادي، مصنفة حسب نوع المرجع ومستوى الصعوبة.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الكتب الأساسية</h3></div>', unsafe_allow_html=True)

    books = [
        {
            "العنوان": "Mastering 'Metrics: The Path from Cause to Effect",
            "المؤلفون": "Joshua D. Angrist & Jörn-Steffen Pischke",
            "المستوى": "مبتدئ-متوسط",
            "الوصف": "كتاب ممتاز للمبتدئين، يشرح المفاهيم الأساسية للاستدلال السببي بأسلوب بسيط وأمثلة واقعية."
        },
        {
            "العنوان": "Mostly Harmless Econometrics: An Empiricist's Companion",
            "المؤلفون": "Joshua D. Angrist & Jörn-Steffen Pischke",
            "المستوى": "متوسط",
            "الوصف": "مرجع أساسي في المنهج التجريبي وشبه التجريبي، يركز على الطرق الإحصائية لتقدير الآثار السببية."
        },
        {
            "العنوان": "Causal Inference: The Mixtape",
            "المؤلفون": "Scott Cunningham",
            "المستوى": "متوسط",
            "الوصف": "كتاب حديث يجمع بين النظرية والتطبيق، مع أمثلة برمجية باستخدام Stata و R."
        },
        {
            "العنوان": "Introduction to Econometrics",
            "المؤلفون": "James H. Stock & Mark W. Watson",
            "المستوى": "مبتدئ",
            "الوصف": "كتاب مدرسي ممتاز يغطي أساسيات القياس الاقتصادي، مع فصول جيدة عن المنهج التجريبي."
        },
        {
            "العنوان": "Field Experiments: Design, Analysis, and Interpretation",
            "المؤلفون": "Alan S. Gerber & Donald P. Green",
            "المستوى": "متوسط",
            "الوصف": "مرجع شامل لتصميم وتحليل التجارب الميدانية في العلوم الاجتماعية."
        }
    ]

    for book in books:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{book['العنوان']}</span><br>
            <b>المؤلفون:</b> {book['المؤلفون']}<br>
            <b>المستوى:</b> <span class="info">{book['المستوى']}</span><br>
            <b>الوصف:</b> {book['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الكتب المتقدمة</h3></div>', unsafe_allow_html=True)

    advanced_books = [
        {
            "العنوان": "Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction",
            "المؤلفون": "Guido W. Imbens & Donald B. Rubin",
            "المستوى": "متقدم",
            "الوصف": "مرجع متقدم يقدم إطارًا نظريًا شاملاً للاستدلال السببي، مع تركيز على نموذج النتائج المحتملة."
        },
        {
            "العنوان": "Counterfactuals and Causal Inference: Methods and Principles for Social Research",
            "المؤلفون": "Stephen L. Morgan & Christopher Winship",
            "المستوى": "متقدم",
            "الوصف": "كتاب يربط بين النظريات الفلسفية للسببية والطرق الإحصائية لتقدير الآثار السببية."
        },
        {
            "العنوان": "Elements of Causal Inference: Foundations and Learning Algorithms",
            "المؤلفون": "Jonas Peters, Dominik Janzing & Bernhard Schölkopf",
            "المستوى": "متقدم",
            "الوصف": "كتاب يربط بين الاستدلال السببي والتعلم الآلي، مع تركيز على النماذج البيانية السببية."
        },
        {
            "العنوان": "Causal Inference in Statistics: A Primer",
            "المؤلفون": "Judea Pearl, Madelyn Glymour & Nicholas P. Jewell",
            "المستوى": "متوسط-متقدم",
            "الوصف": "مقدمة لنظرية Pearl في السببية، تركز على النماذج البيانية والتدخلات."
        }
    ]

    for book in advanced_books:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{book['العنوان']}</span><br>
            <b>المؤلفون:</b> {book['المؤلفون']}<br>
            <b>المستوى:</b> <span class="warning">{book['المستوى']}</span><br>
            <b>الوصف:</b> {book['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>الدورات عبر الإنترنت</h3></div>', unsafe_allow_html=True)

    courses = [
        {
            "العنوان": "Evaluating Social Programs",
            "المنصة": "edX (J-PAL)",
            "المستوى": "مبتدئ-متوسط",
            "الوصف": "دورة ممتازة من مختبر عبد اللطيف جميل لمكافحة الفقر (J-PAL) تركز على تقييم البرامج الاجتماعية باستخدام التجارب العشوائية."
        },
        {
            "العنوان": "Causal Inference",
            "المنصة": "Coursera (Columbia University)",
            "المستوى": "متوسط",
            "الوصف": "دورة شاملة تغطي أساسيات الاستدلال السببي والطرق المختلفة للتقييم."
        },
        {
            "العنوان": "A Crash Course in Causality: Inferring Causal Effects from Observational Data",
            "المنصة": "Coursera (University of Pennsylvania)",
            "المستوى": "متوسط",
            "الوصف": "دورة تركز على استنتاج الآثار السببية من البيانات الرصدية."
        },
        {
            "العنوان": "Econometrics: Methods and Applications",
            "المنصة": "Coursera (Erasmus University Rotterdam)",
            "المستوى": "مبتدئ-متوسط",
            "الوصف": "دورة تغطي أساسيات القياس الاقتصادي، مع تركيز على التطبيقات العملية."
        },
        {
            "العنوان": "Causal Diagrams: Draw Your Assumptions Before Your Conclusions",
            "المنصة": "edX (Harvard University)",
            "المستوى": "متوسط",
            "الوصف": "دورة تركز على استخدام الرسوم البيانية السببية لتوضيح الافتراضات وتحديد الاستراتيجيات المناسبة للتحليل."
        }
    ]

    for course in courses:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{course['العنوان']}</span><br>
            <b>المنصة:</b> {course['المنصة']}<br>
            <b>المستوى:</b> <span class="info">{course['المستوى']}</span><br>
            <b>الوصف:</b> {course['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>موارد برمجية</h3></div>', unsafe_allow_html=True)

    programming = [
        {
            "العنوان": "Causal Inference in Python",
            "اللغة": "Python",
            "الرابط": "https://github.com/microsoft/dowhy",
            "الوصف": "مكتبة DoWhy من Microsoft لتنفيذ تحليل سببي باستخدام بايثون."
        },
        {
            "العنوان": "Causal Inference: The Mixtape (R and Stata Code)",
            "اللغة": "R و Stata",
            "الرابط": "https://mixtape.scunning.com/",
            "الوصف": "الشيفرة المصاحبة لكتاب Causal Inference: The Mixtape."
        },
        {
            "العنوان": "Causal Inference in R",
            "اللغة": "R",
            "الرابط": "https://www.r-causal.org/",
            "الوصف": "مجموعة من حزم R للاستدلال السببي، بما في ذلك MatchIt و CausalImpact."
        },
        {
            "العنوان": "EconML",
            "اللغة": "Python",
            "الرابط": "https://github.com/microsoft/EconML",
            "الوصف": "مكتبة من Microsoft لتقدير الآثار غير المتجانسة باستخدام التعلم الآلي."
        },
        {
            "العنوان": "Python for Econometrics",
            "اللغة": "Python",
            "الرابط": "https://www.kevinsheppard.com/Python_for_Econometrics",
            "الوصف": "موارد تعليمية لاستخدام بايثون في القياس الاقتصادي."
        }
    ]

    for prog in programming:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{prog['العنوان']}</span><br>
            <b>لغة البرمجة:</b> {prog['اللغة']}<br>
            <b>الرابط:</b> <a href="{prog['الرابط']}" target="_blank">{prog['الرابط']}</a><br>
            <b>الوصف:</b> {prog['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المقالات والأوراق البحثية الأساسية</h3></div>', unsafe_allow_html=True)

    papers = [
        {
            "العنوان": "Identification of Causal Effects Using Instrumental Variables",
            "المؤلفون": "Joshua D. Angrist, Guido W. Imbens & Donald B. Rubin",
            "السنة": "1996",
            "الوصف": "ورقة أساسية توضح إطار النتائج المحتملة للمتغيرات الأداتية."
        },
        {
            "العنوان": "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania",
            "المؤلفون": "David Card & Alan B. Krueger",
            "السنة": "1994",
            "الوصف": "دراسة كلاسيكية تستخدم طريقة الفروق في الفروق لتقييم أثر زيادة الحد الأدنى للأجور."
        },
        {
            "العنوان": "Using Maimonides' Rule to Estimate the Effect of Class Size on Scholastic Achievement",
            "المؤلفون": "Joshua D. Angrist & Victor Lavy",
            "السنة": "1999",
            "الوصف": "دراسة مؤثرة تستخدم طريقة الانحدار المتقطع لتقدير أثر حجم الفصل على التحصيل الدراسي."
        },
        {
            "العنوان": "Does Compulsory School Attendance Affect Schooling and Earnings?",
            "المؤلفون": "Joshua D. Angrist & Alan B. Krueger",
            "السنة": "1991",
            "الوصف": "دراسة كلاسيكية تستخدم المتغيرات الأداتية لتقدير عوائد التعليم."
        },
        {
            "العنوان": "Making a Difference in Difference: Causal Inference and the Role of Institutional Knowledge",
            "المؤلفون": "Susan Athey & Guido W. Imbens",
            "السنة": "2022",
            "الوصف": "ورقة حديثة تناقش تطورات طريقة الفروق في الفروق والاعتبارات المؤسسية."
        }
    ]

    for paper in papers:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{paper['العنوان']}</span><br>
            <b>المؤلفون:</b> {paper['المؤلفون']}<br>
            <b>السنة:</b> {paper['السنة']}<br>
            <b>الوصف:</b> {paper['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>المواقع والمدونات</h3></div>', unsafe_allow_html=True)

    websites = [
        {
            "العنوان": "Causal Inference: The Mixtape (الموقع المصاحب للكتاب)",
            "الرابط": "https://mixtape.scunning.com/",
            "الوصف": "موقع يحتوي على محتوى الكتاب والشيفرة المصاحبة له وموارد إضافية."
        },
        {
            "العنوان": "The Difference-in-Differences Toolkit",
            "الرابط": "https://www.nber.org/papers/t0354",
            "الوصف": "مجموعة أدوات شاملة لطريقة الفروق في الفروق من المكتب الوطني للبحوث الاقتصادية."
        },
        {
            "العنوان": "Abdul Latif Jameel Poverty Action Lab (J-PAL)",
            "الرابط": "https://www.povertyactionlab.org/",
            "الوصف": "موقع يحتوي على موارد وأدلة وأمثلة للتجارب العشوائية في مجال مكافحة الفقر."
        },
        {
            "العنوان": "Causal Analysis in Theory and Practice (مدونة Judea Pearl)",
            "الرابط": "http://causality.cs.ucla.edu/blog/",
            "الوصف": "مدونة تناقش قضايا نظرية وعملية في الاستدلال السببي."
        },
        {
            "العنوان": "Statistical Modeling, Causal Inference, and Social Science (مدونة Andrew Gelman)",
            "الرابط": "https://statmodeling.stat.columbia.edu/",
            "الوصف": "مدونة تناقش قضايا في النمذجة الإحصائية والاستدلال السببي."
        }
    ]

    for website in websites:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{website['العنوان']}</span><br>
            <b>الرابط:</b> <a href="{website['الرابط']}" target="_blank">{website['الرابط']}</a><br>
            <b>الوصف:</b> {website['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="subsection-header"><h3>مصادر البيانات</h3></div>', unsafe_allow_html=True)

    data_sources = [
        {
            "العنوان": "Harvard Dataverse",
            "الرابط": "https://dataverse.harvard.edu/",
            "الوصف": "منصة لمشاركة البيانات البحثية، تحتوي على مجموعات بيانات من دراسات تجريبية وشبه تجريبية."
        },
        {
            "العنوان": "World Bank Microdata Library",
            "الرابط": "https://microdata.worldbank.org/",
            "الوصف": "مكتبة تحتوي على بيانات جزئية من مسوح الأسر والمنشآت في البلدان النامية."
        },
        {
            "العنوان": "IPUMS (Integrated Public Use Microdata Series)",
            "الرابط": "https://ipums.org/",
            "الوصف": "مصدر للبيانات الجزئية من التعدادات والمسوح السكانية حول العالم."
        },
        {
            "العنوان": "American Economic Association (AEA) RCT Registry",
            "الرابط": "https://www.socialscienceregistry.org/",
            "الوصف": "سجل للتجارب العشوائية المحكومة في العلوم الاجتماعية."
        },
        {
            "العنوان": "J-PAL Dataverse",
            "الرابط": "https://dataverse.harvard.edu/dataverse/jpal",
            "الوصف": "مجموعات بيانات من التجارب العشوائية التي أجراها باحثو J-PAL."
        }
    ]

    for source in data_sources:
        st.markdown(f"""
        <div style="margin-bottom: 15px;">
            <span class="definition">{source['العنوان']}</span><br>
            <b>الرابط:</b> <a href="{source['الرابط']}" target="_blank">{source['الرابط']}</a><br>
            <b>الوصف:</b> {source['الوصف']}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight-box">
    <span class="success">ملاحظة مهمة:</span> هذه القائمة ليست شاملة، وهناك العديد من الموارد الأخرى المتاحة. من المفيد متابعة المجلات العلمية الرائدة في الاقتصاد مثل American Economic Review و Econometrica و Journal of Political Economy للاطلاع على أحدث التطورات في مجال الاقتصاد التجريبي وشبه التجريبي.
    </div>
    """, unsafe_allow_html=True)

# ملخصات كاملة لكل طريقة
st.markdown('<div class="section-header"><h2>ملخصات كاملة للطرق الرئيسية</h2></div>', unsafe_allow_html=True)

st.markdown('<div class="subsection-header"><h3>التجارب العشوائية المحكومة (RCTs)</h3></div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<span class="definition">تعريف:</span> التجارب العشوائية المحكومة هي طريقة بحثية تعتمد على التعيين العشوائي للمشاركين بين مجموعات المعالجة والضبط لتقدير الأثر السببي لتدخل معين.
</div>

<span class="important-concept">المبادئ الأساسية:</span>

1. <span class="info">التعيين العشوائي:</span> توزيع المشاركين بشكل عشوائي بين المجموعات، مما يضمن توازن الخصائص الملحوظة وغير الملحوظة.
2. <span class="info">مجموعة الضبط:</span> مجموعة لا تتلقى المعالجة، تستخدم كخط أساس للمقارنة.
3. <span class="info">المعالجة:</span> التدخل المدروس الذي يتم تطبيقه على مجموعة المعالجة.

<span class="important-concept">النموذج الرياضي:</span>
""", unsafe_allow_html=True)

st.latex(r"Y_i = \alpha + \beta T_i + \varepsilon_i")

st.markdown("""
حيث:
- $Y_i$ = النتيجة للوحدة $i$
- $T_i$ = متغير ثنائي يشير إلى المعالجة (1 = معالجة، 0 = ضبط)
- $\beta$ = معامل الأثر السببي للمعالجة
- $\varepsilon_i$ = حد الخطأ

<span class="important-concept">خطوات التنفيذ:</span>

1. <span class="info">تحديد السؤال البحثي والفرضيات</span>
2. <span class="info">تحديد المجتمع المستهدف واختيار العينة</span>
3. <span class="info">تحديد حجم العينة المطلوب (Power Analysis)</span>
4. <span class="info">تصميم آلية التعيين العشوائي</span>
5. <span class="info">جمع البيانات الأولية (Baseline)</span>
6. <span class="info">تطبيق المعالجة على مجموعة المعالجة</span>
7. <span class="info">متابعة وجمع البيانات النهائية</span>
8. <span class="info">تحليل البيانات وتقدير الأثر</span>

<span class="important-concept">طرق التعيين العشوائي:</span>

1. <span class="info">التعيين العشوائي البسيط:</span> تعيين عشوائي كامل دون قيود.
2. <span class="info">التعيين العشوائي الطبقي:</span> تقسيم العينة إلى طبقات ثم إجراء التعيين داخل كل طبقة.
3. <span class="info">التعيين العشوائي المجموعي:</span> تعيين مجموعات كاملة (مدارس، قرى) بدلاً من الأفراد.
4. <span class="info">التعيين العشوائي المتوازن:</span> ضمان توازن خصائص معينة بين المجموعات.

<span class="important-concept">تقدير الأثر:</span>
""", unsafe_allow_html=True)

st.latex(r"\hat{\beta} = \bar{Y}_{\text{treatment}} - \bar{Y}_{\text{control}}")

st.markdown("""
<span class="important-concept">الفرضيات الأساسية:</span>

1. <span class="info">الاستقلالية:</span> التعيين العشوائي مستقل عن النتائج المحتملة.
2. <span class="info">عدم وجود آثار انتشار:</span> معالجة وحدة لا تؤثر على نتائج الوحدات الأخرى.
3. <span class="info">الالتزام بالمعالجة:</span> المشاركون يلتزمون بالمعالجة المخصصة لهم.

<span class="important-concept">التحديات والمشكلات:</span>

1. <span class="warning">عدم الامتثال:</span> بعض المشاركين لا يلتزمون بالمعالجة المخصصة لهم.
   <span class="info">الحل:</span> تحليل النية للمعالجة (ITT) أو تقدير أثر المعالجة على الملتزمين (LATE).

2. <span class="warning">التسرب:</span> فقدان بعض المشاركين أثناء الدراسة.
   <span class="info">الحل:</span> تحليل حساسية النتائج للتسرب، استخدام طرق تعويض البيانات المفقودة.

3. <span class="warning">انتشار المعالجة:</span> تأثر مجموعة الضبط بالمعالجة بشكل غير مباشر.
   <span class="info">الحل:</span> التصميم المجموعي، عزل المجموعات جغرافياً.

4. <span class="warning">تأثير هوثورن:</span> تغير سلوك المشاركين لمجرد علمهم بأنهم تحت المراقبة.
   <span class="info">الحل:</span> استخدام المعالجة الوهمية (Placebo) أو التعمية المزدوجة.

5. <span class="warning">التعميم الخارجي:</span> صعوبة تعميم النتائج خارج عينة الدراسة.
   <span class="info">الحل:</span> اختيار عينة ممثلة، تكرار الدراسة في سياقات مختلفة.

<span class="important-concept">متى تستخدم:</span>

- عند الحاجة لتقدير دقيق للأثر السببي
- عند توفر الموارد والقدرة على التحكم في المعالجة
- عند عدم وجود قيود أخلاقية أو عملية على التعيين العشوائي
- لاختبار فعالية تدخلات أو سياسات جديدة

<span class="important-concept">متى لا تستخدم:</span>

- عندما يكون التعيين العشوائي غير أخلاقي
- عند عدم القدرة على التحكم في المعالجة
- عند محدودية الموارد أو الوقت
- عند دراسة ظواهر طبيعية لا يمكن التلاعب بها
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-header"><h3>طريقة الفروق في الفروق (Difference-in-Differences)</h3></div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<span class="definition">تعريف:</span> طريقة الفروق في الفروق هي طريقة شبه تجريبية تستخدم التغير في النتائج عبر الزمن بين مجموعة تلقت المعالجة ومجموعة لم تتلق المعالجة لتقدير الأثر السببي.
</div>

<span class="important-concept">المبدأ الأساسي:</span>

تقارن DiD التغير في النتائج قبل وبعد المعالجة لمجموعة المعالجة مع التغير في النتائج لمجموعة الضبط خلال نفس الفترة الزمنية.

<span class="important-concept">النموذج الرياضي:</span>
""", unsafe_allow_html=True)

st.latex(r"Y_{it} = \alpha + \beta \cdot \text{Treatment}_i + \gamma \cdot \text{Post}_t + \delta \cdot (\text{Treatment}_i \times \text{Post}_t) + \varepsilon_{it}")

st.markdown("""
حيث:
- $Y_{it}$ = النتيجة للوحدة $i$ في الفترة الزمنية $t$
- $\text{Treatment}_i$ = متغير ثنائي يشير إلى مجموعة المعالجة (1 = معالجة، 0 = ضبط)
- $\text{Post}_t$ = متغير ثنائي يشير إلى الفترة الزمنية (1 = بعد المعالجة، 0 = قبل المعالجة)
- $\delta$ = معامل التفاعل، يمثل تقدير الأثر السببي للمعالجة

<span class="important-concept">تقدير الأثر:</span>
""", unsafe_allow_html=True)

st.latex(r"\hat{\delta} = (Y_{\text{treatment,after}} - Y_{\text{treatment,before}}) - (Y_{\text{control,after}} - Y_{\text{control,before}})")

st.markdown("""
<span class="important-concept">الفرضية الأساسية:</span>

<span class="info">فرضية الاتجاهات المتوازية (Parallel Trends):</span> لولا المعالجة، لكانت مجموعة المعالجة تتبع نفس اتجاه مجموعة الضبط مع مرور الوقت.
""", unsafe_allow_html=True)

st.latex(r"E[Y_{it}(0) - Y_{it'}(0) | T_i = 1] = E[Y_{it}(0) - Y_{it'}(0) | T_i = 0]")

st.markdown("""
<span class="important-concept">اختبار فرضية الاتجاهات المتوازية:</span>

1. <span class="info">فحص الاتجاهات قبل المعالجة:</span> مقارنة اتجاهات المجموعتين في الفترات السابقة للمعالجة.
2. <span class="info">اختبار الاتجاهات الزائفة:</span> تحليل "معالجات" وهمية في فترات ما قبل المعالجة الحقيقية.
3. <span class="info">مطابقة اتجاهات ما قبل المعالجة:</span> استخدام طرق المطابقة لاختيار وحدات ضبط تتبع اتجاهات مشابهة.

<span class="important-concept">امتدادات الطريقة:</span>

1. <span class="info">الفروق في الفروق متعددة الفترات:</span> تعميم الطريقة لأكثر من فترتين زمنيتين.
2. <span class="info">الفروق المزدوجة البديلة (Synthetic Control):</span> بناء مجموعة ضبط اصطناعية من مزيج موزون من الوحدات غير المعالجة.
3. <span class="info">الفروق في الفروق مع متغيرات ضبط:</span> إضافة متغيرات تحكم للنموذج لزيادة الدقة.
4. <span class="info">الفروق في الفروق مع التعيين المتدرج (Staggered DiD):</span> تعميم الطريقة عندما تتلقى المجموعات المعالجة في أوقات مختلفة.

<span class="important-concept">التحديات والمشكلات:</span>

1. <span class="warning">انتهاك فرضية الاتجاهات المتوازية:</span> اختلاف اتجاهات المجموعتين قبل المعالجة.
   <span class="info">الحل:</span> استخدام طرق مطابقة الاتجاه، إضافة متغيرات تحكم، اختبار الحساسية.

2. <span class="warning">الأحداث المتزامنة:</span> وقوع أحداث أخرى في نفس وقت المعالجة تؤثر على النتائج.
   <span class="info">الحل:</span> استخدام مجموعات ضبط متعددة، اختبار التصريف، تحليل الحساسية.

3. <span class="warning">التكوين المتغير للمجموعات:</span> تغير تكوين المجموعات مع مرور الوقت.
   <span class="info">الحل:</span> استخدام عينة متوازنة، تحليل التسرب.

4. <span class="warning">التعيين المتدرج للمعالجة:</span> تلقي المجموعات المعالجة في أوقات مختلفة.
   <span class="info">الحل:</span> استخدام طرق DiD المتقدمة مثل Callaway و Sant'Anna (2021).

<span class="important-concept">متى تستخدم:</span>

- عند وجود بيانات قبل وبعد تدخل معين
- عند وجود مجموعة ضبط لم تتلق التدخل
- عند عدم إمكانية إجراء تجربة عشوائية محكومة
- لتقييم آثار السياسات والإصلاحات على مستوى المناطق أو الدول

<span class="important-concept">متى لا تستخدم:</span>

- عند عدم وجود بيانات قبل المعالجة
- عند انتهاك واضح لفرضية الاتجاهات المتوازية
- عند وجود آثار انتشار كبيرة بين المجموعات
- عندما تكون هناك تغيرات كبيرة في تكوين المجموعات مع مرور الوقت
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-header"><h3>طريقة الانحدار المتقطع (Regression Discontinuity Design)</h3></div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<span class="definition">تعريف:</span> طريقة الانحدار المتقطع هي طريقة شبه تجريبية تستغل وجود عتبة محددة تفصل بين من يتلقى المعالجة ومن لا يتلقاها، وتقارن النتائج للوحدات القريبة من جانبي العتبة.
</div>

<span class="important-concept">المبدأ الأساسي:</span>

تستغل RDD حقيقة أن الوحدات القريبة جداً من عتبة التأهل على جانبي العتبة متشابهة في كل شيء تقريباً باستثناء تلقي المعالجة، مما يخلق "تجربة طبيعية" محلية حول العتبة.

<span class="important-concept">النموذج الرياضي (للانحدار المتقطع الحاد):</span>
""", unsafe_allow_html=True)

st.latex(r"Y_i = \alpha + \beta T_i + \gamma_1 (X_i - c) + \gamma_2 T_i \cdot (X_i - c) + \varepsilon_i")

st.markdown("""
حيث:
- $Y_i$ = النتيجة للوحدة $i$
- $T_i$ = متغير ثنائي يشير إلى المعالجة (1 إذا $X_i \geq c$، 0 خلاف ذلك)
- $X_i$ = متغير التعيين (Running Variable)
- $c$ = العتبة (Threshold)
- $\beta$ = معامل الأثر السببي للمعالجة عند العتبة

<span class="important-concept">أنواع الانحدار المتقطع:</span>

1. <span class="info">الانحدار المتقطع الحاد (Sharp RDD):</span> المعالجة محددة تماماً بواسطة متغير التعيين والعتبة.
   - $T_i = 1$ إذا $X_i \geq c$، و $T_i = 0$ إذا $X_i < c$

2. <span class="info">الانحدار المتقطع الضبابي (Fuzzy RDD):</span> متغير التعيين يؤثر على احتمالية المعالجة ولكن لا يحددها بشكل قاطع.
   - $P(T_i = 1 | X_i) $ تتغير بشكل غير مستمر عند $X_i = c$

<span class="important-concept">تقدير الأثر:</span>

<span class="info">للانحدار المتقطع الحاد:</span>
""", unsafe_allow_html=True)

st.latex(r"\hat{\beta} = \lim_{x \downarrow c} E[Y_i | X_i = x] - \lim_{x \uparrow c} E[Y_i | X_i = x]")

st.markdown("""
<span class="info">للانحدار المتقطع الضبابي:</span>
""", unsafe_allow_html=True)

st.latex(r"\hat{\beta} = \frac{\lim_{x \downarrow c} E[Y_i | X_i = x] - \lim_{x \uparrow c} E[Y_i | X_i = x]}{\lim_{x \downarrow c} E[T_i | X_i = x] - \lim_{x \uparrow c} E[T_i | X_i = x]}")

st.markdown("""
<span class="important-concept">الفرضيات الأساسية:</span>

1. <span class="info">فرضية الاستمرارية:</span> النتائج المحتملة تتغير بشكل مستمر مع متغير التعيين حول العتبة.
2. <span class="info">عدم التلاعب بمتغير التعيين:</span> الأفراد لا يستطيعون التحكم بدقة في قيمة متغير التعيين.
3. <span class="info">قابلية التعريف (للضبابي):</span> احتمالية المعالجة تتغير بشكل غير مستمر عند العتبة.

<span class="important-concept">اختبارات الفرضيات:</span>

1. <span class="info">اختبار استمرارية المتغيرات المتحكمة:</span> فحص استمرارية الخصائص الأخرى حول العتبة.
2. <span class="info">اختبار تراكم الكثافة:</span> فحص عدم وجود تراكم غير طبيعي للوحدات حول العتبة (اختبار McCrary).
3. <span class="info">اختبارات الحساسية:</span> تغيير عرض النطاق (Bandwidth) حول العتبة.

<span class="important-concept">اعتبارات التنفيذ:</span>

1. <span class="info">اختيار عرض النطاق (Bandwidth):</span> تحديد مدى البيانات حول العتبة المستخدمة في التحليل.
2. <span class="info">اختيار الشكل الوظيفي:</span> تحديد كيفية نمذجة العلاقة بين متغير التعيين والنتيجة.
3. <span class="info">الترجيح (Weighting):</span> إعطاء وزن أكبر للملاحظات الأقرب إلى العتبة.

<span class="important-concept">التحديات والمشكلات:</span>

1. <span class="warning">التلاعب بمتغير التعيين:</span> قدرة الأفراد على التحكم في قيمة متغير التعيين.
   <span class="info">الحل:</span> اختبار التراكم، استخدام متغيرات تعيين أقل عرضة للتلاعب.

2. <span class="warning">قلة البيانات حول العتبة:</span> عدد قليل من الملاحظات قريبة من العتبة.
   <span class="info">الحل:</span> زيادة عرض النطاق، استخدام أشكال وظيفية مرنة.

3. <span class="warning">تعدد العتبات:</span> وجود عتبات متعددة أو متداخلة تؤثر على النتيجة.
   <span class="info">الحل:</span> التحليل المنفصل لكل عتبة، نماذج أكثر تعقيداً.

4. <span class="warning">قابلية التعميم المحدودة:</span> الأثر المقدر ينطبق فقط على الوحدات قريبة العتبة.
   <span class="info">الحل:</span> تكامل مع طرق أخرى، مناقشة حدود التعميم.

<span class="important-concept">متى تستخدم:</span>

- عند وجود عتبة واضحة تحدد من يتلقى المعالجة
- عند عدم التلاعب بمتغير التعيين
- عند توفر بيانات كافية حول العتبة
- لتقييم برامج لها معايير أهلية محددة (منح دراسية، دعم للأسر الفقيرة، إلخ)

<span class="important-concept">متى لا تستخدم:</span>

- عند عدم وجود عتبة واضحة
- عند وجود أدلة على التلاعب بمتغير التعيين
- عند قلة البيانات حول العتبة
- عندما تكون قابلية التعميم خارج نطاق العتبة مهمة جداً للسؤال البحثي
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-header"><h3>طريقة المتغيرات الأداتية (Instrumental Variables)</h3></div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<span class="definition">تعريف:</span> طريقة المتغيرات الأداتية هي طريقة إحصائية تستخدم متغيراً ثالثاً (المتغير الأداتي) للتغلب على مشكلة الاندوجينية (الداخلية) في متغير المعالجة، وذلك لتقدير الأثر السببي.
</div>

<span class="important-concept">المبدأ الأساسي:</span>

تستخدم IV متغيراً خارجياً (الأداة) يؤثر على متغير المعالجة ولكن لا يؤثر على النتيجة إلا من خلال تأثيره على المعالجة، مما يسمح بعزل التغير الخارجي في المعالجة لتقدير أثرها السببي.

<span class="important-concept">النموذج الرياضي:</span>

<span class="info">المرحلة الأولى:</span>
""", unsafe_allow_html=True)

st.latex(r"T_i = \pi_0 + \pi_1 Z_i + \pi_2 X_i + \eta_i")

st.markdown("""
<span class="info">المرحلة الثانية:</span>
""", unsafe_allow_html=True)

st.latex(r"Y_i = \beta_0 + \beta_1 \hat{T}_i + \beta_2 X_i + \varepsilon_i")

st.markdown("""
حيث:
- $T_i$ = متغير المعالجة (قد يكون ثنائياً أو مستمراً)
- $Z_i$ = المتغير الأداتي
- $X_i$ = متجه المتغيرات المتحكمة
- $\hat{T}_i$ = القيمة المتنبأ بها لمتغير المعالجة من المرحلة الأولى
- $\beta_1$ = معامل الأثر السببي للمعالجة

<span class="important-concept">شروط المتغير الأداتي الصالح:</span>

1. <span class="info">الارتباط (Relevance):</span> المتغير الأداتي يرتبط بشكل قوي مع متغير المعالجة.
""", unsafe_allow_html=True)

st.latex(r"Cov(Z_i, T_i) \neq 0")

st.markdown("""
2. <span class="info">القيد الاستبعادي (Exclusion Restriction):</span> المتغير الأداتي لا يؤثر على النتيجة إلا من خلال تأثيره على المعالجة.
""", unsafe_allow_html=True)

st.latex(r"Cov(Z_i, \varepsilon_i) = 0")

st.markdown("""
3. <span class="info">الاستقلالية (Independence):</span> المتغير الأداتي مستقل عن المتغيرات غير الملحوظة التي تؤثر على النتيجة.
""", unsafe_allow_html=True)

st.latex(r"Z_i \perp\!\!\!\perp U_i")

st.markdown("""
4. <span class="info">الوحدانية (Monotonicity) (للأدوات الثنائية):</span> المتغير الأداتي يؤثر على جميع الوحدات في نفس الاتجاه.
""", unsafe_allow_html=True)

st.latex(r"T_i(z=1) \geq T_i(z=0) \quad \forall i \quad \text{أو} \quad T_i(z=1) \leq T_i(z=0) \quad \forall i")

st.markdown("""
<span class="important-concept">تقدير الأثر:</span>

<span class="info">طريقة المربعات الصغرى ذات المرحلتين (2SLS):</span>
""", unsafe_allow_html=True)

st.latex(r"\hat{\beta}_{IV} = \frac{Cov(Y_i, Z_i)}{Cov(T_i, Z_i)}")

st.markdown("""
<span class="important-concept">تفسير المعاملات:</span>

<span class="info">الأثر المحلي المتوسط للمعالجة (LATE):</span> في حالة الأدوات الثنائية والمعالجة الثنائية، يقدر IV الأثر على "الملتزمين" (Compliers) - الوحدات التي تغير حالة معالجتها استجابة للأداة.
""", unsafe_allow_html=True)

st.latex(r"\text{LATE} = E[Y_i(1) - Y_i(0) | \text{compliers}]")

st.markdown("""
<span class="important-concept">اختبارات الفرضيات:</span>

1. <span class="info">اختبار الارتباط:</span> اختبار قوة المرحلة الأولى (F-statistic > 10 كقاعدة عامة).
2. <span class="info">اختبارات زيادة التعريف (Overidentification):</span> اختبار صحة القيد الاستبعادي عند وجود أكثر من أداة (اختبار Sargan أو Hansen).
3. <span class="info">اختبار التوازن:</span> فحص ارتباط المتغير الأداتي بالخصائص الملحوظة.
4. <span class="info">اختبارات الدوال المخفضة (Reduced Form):</span> فحص العلاقة المباشرة بين الأداة والنتيجة.

<span class="important-concept">أنواع المتغيرات الأداتية الشائعة:</span>

1. <span class="info">الظواهر الطبيعية:</span> الطقس، الكوارث الطبيعية، الأوبئة.
2. <span class="info">السياسات والقوانين:</span> التغييرات في اللوائح التنظيمية، الإصلاحات، إدخال برامج جديدة.
3. <span class="info">المسافة الجغرافية:</span> المسافة إلى مؤسسات أو خدمات معينة.
4. <span class="info">العشوائية الطبيعية:</span> الترتيب الزمني للميلاد، نتائج اليانصيب.
5. <span class="info">الخصائص الوراثية:</span> الجينات كأدوات للسلوكيات أو الصفات.

<span class="important-concept">التحديات والمشكلات:</span>

1. <span class="warning">الأدوات الضعيفة:</span> ضعف الارتباط بين الأداة والمعالجة.
   <span class="info">الحل:</span> البحث عن أدوات أقوى، استخدام طرق تقدير متقدمة للأدوات الضعيفة.

2. <span class="warning">انتهاك القيد الاستبعادي:</span> تأثير الأداة على النتيجة من خلال مسارات أخرى.
   <span class="info">الحل:</span> التحكم في المسارات الأخرى، تحليل الحساسية، استخدام اختبارات زيادة التعريف.

3. <span class="warning">تباين تقديرات IV:</span> تقديرات IV عادة ما تكون أقل دقة من OLS.
   <span class="info">الحل:</span> زيادة حجم العينة، استخدام أدوات أقوى.

4. <span class="warning">تجانس الأثر:</span> IV تقدر LATE، الذي قد لا يكون ممثلاً للأثر على جميع الوحدات.
   <span class="info">الحل:</span> مناقشة محددات LATE، استخدام أدوات متعددة لتقدير آثار على مجموعات مختلفة.

<span class="important-concept">متى تستخدم:</span>

- عند وجود مشكلة اندوجينية في متغير المعالجة (تحيز في الاختيار، سببية عكسية، متغيرات محذوفة)
- عند توفر متغير أداتي يستوفي الشروط المطلوبة
- عندما تكون العلاقة السببية بين المعالجة والنتيجة محور الاهتمام

<span class="important-concept">متى لا تستخدم:</span>

- عند عدم وجود أداة قوية
- عندما يكون القيد الاستبعادي غير معقول
- عندما يكون الأثر المحلي (LATE) غير مهم للسؤال البحثي
- عندما تكون هناك طرق أبسط وأكثر كفاءة متاحة (مثل RCT)
""", unsafe_allow_html=True)

st.markdown('<div class="subsection-header"><h3>طريقة المطابقة (Matching Methods)</h3></div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<span class="definition">تعريف:</span> طرق المطابقة هي مجموعة من الأساليب شبه التجريبية التي تحاول إنشاء مجموعة مقارنة متشابهة مع مجموعة المعالجة في الخصائص الملحوظة، ثم تقارن النتائج بين المجموعتين لتقدير الأثر السببي.
</div>

<span class="important-concept">المبدأ الأساسي:</span>

لكل وحدة في مجموعة المعالجة، تبحث طرق المطابقة عن وحدة (أو أكثر) في مجموعة الضبط لها خصائص متشابهة، مما يقلل من التحيز الناتج عن الاختلافات في الخصائص الملحوظة.

<span class="important-concept">الفرضيات الأساسية:</span>

1. <span class="info">الاستقلالية الشرطية (Conditional Independence Assumption - CIA):</span> بعد التحكم في المتغيرات الملحوظة X، تصبح المعالجة مستقلة عن النتائج المحتملة.
""", unsafe_allow_html=True)

st.latex(r"\{Y_i(0), Y_i(1)\} \perp\!\!\!\perp T_i | X_i")

st.markdown("""
2. <span class="info">الدعم المشترك (Common Support):</span> لكل مجموعة من قيم X، هناك احتمال إيجابي للمعالجة وعدم المعالجة.
""", unsafe_allow_html=True)

st.latex(r"0 < P(T_i = 1 | X_i = x) < 1 \quad \forall x")

st.markdown("""
<span class="important-concept">أنواع طرق المطابقة:</span>

1. <span class="info">المطابقة المباشرة (Exact Matching):</span>
   - مطابقة دقيقة على جميع المتغيرات
   - بسيطة لكن صعبة التطبيق مع متغيرات متعددة (مشكلة الأبعاد)

2. <span class="info">مطابقة المسافة (Distance Matching):</span>
   - مطابقة الوحدات باستخدام مقياس للمسافة بين الخصائص
   - أنواع شائعة: المسافة الإقليدية، مسافة ماهالانوبيس

3. <span class="info">مطابقة درجة الميل (Propensity Score Matching - PSM):</span>
   - حساب احتمالية المعالجة (درجة الميل) لكل وحدة
   - مطابقة وحدات المعالجة مع وحدات الضبط ذات درجات ميل متشابهة

4. <span class="info">المطابقة الضبابية (Fuzzy Matching):</span>
   - السماح بعدم التطابق الدقيق باستخدام مقاييس تشابه
   - مفيدة للمتغيرات النصية أو الفئوية

5. <span class="info">المطابقة المرجحة (Weighted Matching):</span>
   - ترجيح الملاحظات بناءً على درجة التشابه
   - مثل: إعادة الترجيح بدرجة الميل، ترجيح كيرنل

<span class="important-concept">خطوات تنفيذ مطابقة درجة الميل (PSM):</span>

1. <span class="info">تقدير درجة الميل:</span> استخدام نموذج انحدار لوجستي أو بروبيت لتقدير احتمالية المعالجة.
""", unsafe_allow_html=True)

st.latex(r"p(X_i) = P(T_i = 1 | X_i)")

st.markdown("""
2. <span class="info">اختيار خوارزمية المطابقة:</span> أقرب جار (Nearest Neighbor)، رادياس (Radius)، كيرنل (Kernel)، إلخ.

3. <span class="info">التحقق من التوازن:</span> فحص توازن الخصائص بين المجموعات بعد المطابقة.

4. <span class="info">تقدير الأثر:</span> حساب الفرق في النتائج بين المجموعات المتطابقة.

<span class="important-concept">تقدير الأثر باستخدام PSM:</span>

<span class="info">متوسط الأثر على المعالجين (ATT):</span>
""", unsafe_allow_html=True)

st.latex(r"\text{ATT}_{PSM} = \frac{1}{N_T} \sum_{i:T_i=1} \left[ Y_i - \sum_{j:T_j=0} w(i,j) Y_j \right]")

st.markdown("""
حيث:
- $N_T$ = عدد وحدات المعالجة
- $w(i,j)$ = الوزن المعطى للوحدة الضابطة $j$ عند مطابقتها مع وحدة المعالجة $i$

<span class="important-concept">اختبارات التوازن والتشخيص:</span>

1. <span class="info">اختبار توازن الخصائص:</span> مقارنة متوسطات الخصائص بين المجموعات بعد المطابقة.
2. <span class="info">فحص التداخل في درجات الميل:</span> التأكد من وجود دعم مشترك كافٍ.
3. <span class="info">اختبار جودة المطابقة:</span> حساب الفرق المعياري المطلق، نسبة التباين.
4. <span class="info">تحليل الحساسية للاندوجينية المتبقية:</span> حدود روزنباوم، تحليل التحيز المحدود.

<span class="important-concept">التحديات والمشكلات:</span>

1. <span class="warning">الانحياز للمتغيرات غير الملحوظة:</span> CIA تفترض أن جميع المتغيرات المهمة ملحوظة.
   <span class="info">الحل:</span> تحليل الحساسية، دمج المطابقة مع طرق أخرى (DiD-Matching).

2. <span class="warning">مشكلة الأبعاد:</span> صعوبة المطابقة على متغيرات متعددة.
   <span class="info">الحل:</span> استخدام درجة الميل، تقليل الأبعاد.

3. <span class="warning">سوء تحديد نموذج درجة الميل:</span> خطأ في تقدير درجة الميل.
   <span class="info">الحل:</span> استخدام نماذج مرنة، التحقق من التوازن.

4. <span class="warning">نقص الدعم المشترك:</span> عدم وجود تداخل كافٍ بين المجموعات.
   <span class="info">الحل:</span> تقييد التحليل لمنطقة الدعم المشترك، مناقشة حدود التعميم.

<span class="important-concept">امتدادات متقدمة:</span>

1. <span class="info">المطابقة مع الانحدار (Matching with Regression):</span> دمج المطابقة مع تعديل الانحدار.
2. <span class="info">المطابقة مع الفروق في الفروق (DiD-Matching):</span> دمج المطابقة مع DiD للتحكم في الاختلافات غير الملحوظة الثابتة مع الزمن.
3. <span class="info">المطابقة المتعددة المستويات (Multilevel Matching):</span> للبيانات ذات البنية الهرمية.
4. <span class="info">المطابقة الوراثية (Genetic Matching):</span> استخدام خوارزميات وراثية لتحسين التوازن.

<span class="important-concept">متى تستخدم:</span>

- عند توفر بيانات غنية عن خصائص الوحدات
- عندما تكون فرضية الاستقلالية الشرطية معقولة
- عند وجود تداخل كافٍ بين المجموعات
- لتقليل التحيز في الاختيار عند مقارنة مجموعات غير عشوائية

<span class="important-concept">متى لا تستخدم:</span>

- عند وجود متغيرات غير ملحوظة مهمة تؤثر على كل من المعالجة والنتيجة
- عند عدم وجود دعم مشترك كافٍ
- عندما تكون البيانات عن الخصائص محدودة
- عندما تكون هناك طرق أكثر قوة متاحة (مثل RCT أو IV مع أداة قوية)
""", unsafe_allow_html=True)

# إضافة زر لتنزيل المحتوى كملف PDF
st.markdown("""
<div style="margin-top: 50px; text-align: center;">
    <h3>تنزيل المحتوى</h3>
    <p>يمكنك استخدام وظيفة الطباعة في المتصفح لحفظ المحتوى كملف PDF.</p>
    <ol style="text-align: right; display: inline-block;">
        <li>اضغط Ctrl+P (أو Command+P على Mac)</li>
        <li>اختر "حفظ كـ PDF" من خيارات الطباعة</li>
        <li>احفظ الملف على جهازك</li>
    </ol>
</div>
""", unsafe_allow_html=True)