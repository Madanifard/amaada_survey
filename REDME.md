# <a name="_aqvcach2dv7k"></a>ساختار پروژه:
دایرکتوری config : برای تنظیمات کلی جانگو استفاده شده است.

|<p>$ tree config</p><p>config</p><p>├── \_\_init\_\_.py</p><p>├── \_\_pycache\_\_</p><p>│   ├── \_\_init\_\_.cpython-312.pyc</p><p>│   └── settings.cpython-312.pyc</p><p>├── asgi.py</p><p>├── celery.py</p><p>├── settings.py</p><p>├── urls.py</p><p>└── wsgi.py</p>|
| :- |

فایل settings تنظیمات کلی وب سایت جانگویی است

فایل celery تنظیمات مربوط به استفاده از celery

فایل url تنظیمات کلی url ها

دایرکتوری survey:

کدهای مربوط به پرسشنامه در app قرار داده شده است

|<p>$ tree survey</p><p>survey</p><p>├── \_\_init\_\_.py</p><p>├── admin.py</p><p>├── apis</p><p>│   ├── \_\_init\_\_.py</p><p>│   ├── question.py</p><p>│   ├── responses.py</p><p>│   ├── survey.py</p><p>│   └── survey\_participants.py</p><p>├── apps.py</p><p>├── celery\_tasks</p><p>│   ├── \_\_init\_\_.py</p><p>│   └── response\_task.py</p><p>├── migrations</p><p>│   ├── 0001\_initial.py</p><p>│   ├── 0002\_alter\_options\_question\_alter\_questions\_survey.py</p><p>│   └── \_\_init\_\_.py</p><p>├── models</p><p>│   ├── \_\_init\_\_.py</p><p>│   ├── options.py</p><p>│   ├── questions.py</p><p>│   ├── responses.py</p><p>│   ├── survey\_participants.py</p><p>│   └── surveys.py</p><p>├── serializers</p><p>│   ├── \_\_init\_\_.py</p><p>│   ├── question\_serializer.py</p><p>│   ├── response\_serializer.py</p><p>│   ├── survey\_participants.py</p><p>│   └── survey\_serializer.py</p><p>├── tests</p><p>│   ├── \_\_init\_\_.py</p><p>│   ├── test\_model.py</p><p>│   ├── test\_question\_api.py</p><p>│   └── test\_survey\_api.py</p><p>└── urls.py</p>|
| :- |

دایرکتوری apis شامل تمامی API های مورد نیاز برای این تسک قرار داده شده است.

دایرکتوری models ـ مدل های مورد نیاز هر کدام در فایل جداگانه قرار داده شده است.

دایرکتوری serializers - برای سریالایزر های مورد نیاز هر کدام را در فایل جداگانه قرار داده شده.

دایرکتوری test نیز برای پیاده سازی تست های مورد نیاز است.

فایل urls تنظیمات url های مربوط به این بخش قرار داده شده است.

# <a name="_yo6im0yac8b9"></a>پیاده سازی API:
برای پیاده سازی API از کتابخانه DRF استفاده شده است و همچنین برای تولید داکیومنت های API ها (swager) از کتابخانه  drf-spectacular استفاده شده است

برای مشاهده داکیومنت API ها بعد از راه اندازی پروژه به آدرس زیر بروید

|http://localhost:8000/survey/api/swagger|
| :- |

# <a name="_epq3as4p0v85"></a>راه اندازی پروژه:
پروژه کاملا دایکرایز شده است 

ابتدا نیاز است که پسوند example فایل های زیر را بردارید : 

\*\* برای راحتی کار مقدارهای مورد نیاز قبلا قرار داده شده است ولی در صورت نیاز می توانید آن ها را تغییر دهید

|$ mv .env.db.example .emv.db|
| :- |
|$ mv .env.example .env|
| :- |



سپس با دستوراتی که در Makefile قرار داده شده است میتوانید پروژه را راه اندازی کنید

|<p>$ make</p><p>Usage: make <target></p><p>Available targets:</p><p>`  `build       	Build Docker images</p><p>`  `up          	Start Docker containers</p><p>`  `down        	Stop Docker containers</p><p>`  `clean       	Down Container and remove Volume and Network</p><p>`  `clean-all   	Remove Docker containers and images</p><p>`  `build-no-cache  Build Docker images without cache</p><p>`  `restart     	Restart Docker containers</p><p>`  `cli-web     	connect to web bash</p><p>`  `cli-db      	connect to db bash with postgres user</p><p>`  `test-cases  	connect to web bash for run test</p>|
| :- |


