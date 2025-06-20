# المنهج التجريبي وشبه التجريبي في القياس الاقتصادي (Experimental and Quasi-Experimental Methods in Econometrics)

هذا التطبيق هو دليل شامل للمبتدئين باللغة العربية، يشرح المنهج التجريبي وشبه التجريبي في مجال القياس الاقتصادي. تم بناء التطبيق باستخدام Streamlit ويهدف إلى توفير فهم عميق للمفاهيم الأساسية، الطرق المختلفة، الفرضيات، والتطبيقات العملية لهذه المناهج.

This is a comprehensive Arabic-language guide for beginners, explaining experimental and quasi-experimental methods in econometrics. The application is built using Streamlit and aims to provide a deep understanding of core concepts, various methods, assumptions, and practical applications of these approaches.

## 🌟 الميزات (Features)

*   **واجهة باللغة العربية:** تصميم كامل يدعم الاتجاه من اليمين إلى اليسار (RTL) لسهولة القراءة.
*   **محتوى تعليمي شامل:** يغطي التطبيق مجموعة واسعة من المواضيع، من المقدمات الأساسية إلى الطرق المتقدمة.
*   **تفاعلية:** استخدام عناصر Streamlit التفاعلية للتنقل بين الأقسام وعرض المحتوى.
*   **رسوم بيانية توضيحية:** استخدام Plotly لإنشاء رسوم بيانية تفاعلية لتوضيح المفاهيم الإحصائية والاقتصادية.
*   **صيغ رياضية:** عرض الصيغ الرياضية الهامة باستخدام LaTeX.
*   **أمثلة وتطبيقات:** تقديم أمثلة عملية وتطبيقات في مجالات اقتصادية متنوعة.
*   **خطة تعلم وموارد:** اقتراح خطة تعلم متكاملة وقائمة بالموارد والمراجع المفيدة.
*   **ملخصات للطرق الرئيسية:** توفير ملخصات مركزة للطرق التجريبية وشبه التجريبية الأساسية.
*   **تصميم مخصص:** استخدام CSS مخصص لتحسين تجربة المستخدم وتوضيح المفاهيم الهامة.

## 📚 الأقسام المغطاة (Sections Covered)

يتضمن التطبيق الأقسام التالية:

1.  **مقدمة:** نظرة عامة على أهمية المناهج التجريبية في الاقتصاد.
2.  **مفهوم المنهج التجريبي:** شرح المفاهيم الأساسية كالسببية، المعالجة، والمجموعات الضابطة.
3.  **البيانات التجريبية والرصدية:** الفروقات بين أنواع البيانات المختلفة المستخدمة.
4.  **التجارب العشوائية المحكومة (RCTs):** تصميم، تنفيذ، وتحليل التجارب العشوائية.
5.  **المنهج شبه التجريبي:** استعراض الطرق الرئيسية مثل:
    *   الفروق في الفروق (Difference-in-Differences - DiD)
    *   الانحدار المتقطع (Regression Discontinuity Design - RDD)
    *   المتغيرات الأداتية (Instrumental Variables - IV)
    *   طرق المطابقة (Matching Methods)
6.  **طرق التقييم والتحليل:** كيفية تقدير الآثار السببية واختبار الفرضيات.
7.  **الفرضيات الأساسية:** الفرضيات اللازمة لصحة كل طريقة.
8.  **التطبيقات في الاقتصاد:** أمثلة عملية من مجالات اقتصاد التنمية، العمل، التعليم، وغيرها.
9.  **خطة التعلم الشاملة:** دليل مقترح لتعلم هذه المناهج بشكل متدرج.
10. **الموارد والمراجع:** قائمة بالكتب، الدورات، والمقالات المفيدة.

## 🛠️ التقنيات المستخدمة (Technologies Used)

*   **Python:** لغة البرمجة الأساسية.
*   **Streamlit:** لإطار عمل التطبيق وتصميم الواجهة.
*   **Plotly:** لإنشاء الرسوم البيانية التفاعلية.
*   **Pandas:** لمعالجة البيانات وإنشاء الجداول.
*   **NumPy:** للعمليات الحسابية والرقمية.
*   **Pillow (PIL):** لمعالجة الصور (وإن لم تستخدم بشكل مباشر وواضح في الكود النهائي، إلا أنها قد تكون من الاعتمادات الضمنية أو للاستخدامات المستقبلية).
*   **HTML/CSS:** لتخصيص التصميم والمظهر.
*   **Mermaid:** لإنشاء المخططات (عبر خدمة `mermaid.ink` المدمجة).

## 🚀 كيفية تشغيل التطبيق (How to Run)

1.  **استنساخ المستودع (Clone the repository - hypothetical):**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **إنشاء بيئة افتراضية (Create a virtual environment - recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **تثبيت المكتبات المطلوبة (Install dependencies):**
    تأكد من وجود ملف `requirements.txt` في نفس المجلد الذي يحتوي على `rexp.py`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **تشغيل التطبيق (Run the Streamlit app):**
    ```bash
    streamlit run rexp.py
    ```
    سيتم فتح التطبيق في متصفح الويب الخاص بك.

## 📝 ملاحظات إضافية (Additional Notes)

*   تم تصميم هذا التطبيق ليكون مورداً تعليمياً باللغة العربية.
*   يتم استخدام خدمة `mermaid.ink` لعرض مخططات Mermaid، لذا يتطلب الأمر اتصالاً بالإنترنت لعرض هذه المخططات بشكل صحيح.
*   يمكن حفظ محتوى التطبيق كملف PDF باستخدام خاصية الطباعة في المتصفح (Ctrl+P أو Cmd+P ثم "Save as PDF").

## 🤝 المساهمة (Contributing)

المساهمات لتحسين هذا الدليل مرحب بها. يرجى فتح "issue" لمناقشة التغييرات المقترحة أو إرسال "pull request".

---

This README provides an overview of your Streamlit application, its features, how to run it, and the technologies used.
